import re
import os
import urllib2
import glob
from subprocess import Popen, PIPE

import yaml

from . import settings


class ParseTestDriverYaml(object):
    """
    This is for parsing the JsTestDriver yaml config file
    """

    def __init__(self, file_path, *args, **kwargs):
        self.parse_testdriver_conf(file_path, **kwargs)

    def parse_testdriver_conf(self, file_path, **kwargs):
        """
        parses the testdriver config file which is used by JsTestDriver.jar.
        It is just a basic yaml parser that takes a required file_path arg
        and accepts kwargs for adding extra config items if neccessary
        """
        conf_file = open(file_path, 'r')
        # parse JsTestDriver.conf for file paths to pass over to custom jasmine spec runner

        conf = yaml.load(conf_file)
        if kwargs:
            conf.update(kwargs)
        star = '\*'
        for group, paths in conf.items():
            if group in ['load', 'test', 'serve']:
                conf[group] = []
                for file_path in paths:
                    if not file_path in settings.JSTESTDRIVER_REMOVE_FROM_VIEW:
                        # search for * modifier
                        if re.search(star, file_path):
                            conf[group] = [
                                path.split(settings.MEDIA_ROOT)[1].lstrip('/')
                                for path in glob.glob(os.path.join(settings.MEDIA_ROOT, file_path))
                            ]
                        else:
                            conf[group].append(file_path)
        self.conf = conf

        return self.conf


class JsTestDriverHandler(object):
    """
    This is a handler for running
    """

    def __init__(self, testdriver_server_path, options, *args, **kwargs):

        self.output_dir = os.path.join(settings.SITE_ROOT, settings.JSTESTDRIVER_OUTPUT)
        self.start_jstestdriver_server(testdriver_server_path, options)

    def download_jstestdriver_jars(self, options):
        Popen(['wget', 'https://code.google.com/p/js-test-driver/downloads/detail?name=JsTestDriver-1.3.5.jar&can=2&q=', '-O', 'JsTestDriver.jar'])
        Popen(['mkdir', 'plugins'])
        Popen(['wget', '-P', 'plugins/', 'https://code.google.com/p/js-test-driver/downloads/detail?name=coverage-1.3.5.jar&can=2&q=', '-O',
               'coverage.jar'])

        self.downloaded_jars = True

    def start_jstestdriver_server(self, testdriver_server_path, options):

        # try to ping the jstestdriver server
        self.testdriver_server_path = testdriver_server_path
        try:
            urllib2.urlopen(testdriver_server_path)
            html = urllib2.urlopen(testdriver_server_path).read()
            regex = re.compile('Captured\ Browsers\:\ \(([0-9])\)')

            # if you have at least one captured browser
            if int(re.search(regex, html).group(1)) > 0:
                print "Server already running at http://localhost:%s" % options.get('port')
                print "Running tests..."
                self.run_jstestdriver_tests(options)
            # if there are no captured browsers
            else:
                print "You have no browsers captured. at %s/capture/" % testdriver_server_path
                print "Configured browsers are: %s" % settings.JSTESTDRIVER_BROWSER_PATH

        # start the server if there is not one running
        except urllib2.URLError:
            Popen(['java', '-jar', settings.JSTESTDRIVER_PATH,
                   '--port', options.get('port'),
                   '--browser', options.get('browser'),
            ])

            print "Server started at %s" % testdriver_server_path
            print "Please wait for the captured browser window to open before running tests"
            pass

        return None

    def run_jstestdriver_tests(self, options):
        """
        Run the jasmine specs on local jstestdriver server
        """
        suite = Popen(['java', '-jar', settings.JSTESTDRIVER_PATH,
                       '--tests', options.get('tests'),
                       '--server', self.testdriver_server_path,
                       '--reset', options.get('reset'),
                       '--testOutput', options.get('output'),
                       '--verbose',
                       '--config', settings.JSTESTDRIVER_CONFIG,
                       '--captureConsole', ],
                      stdout=PIPE, stderr=PIPE)

        stdout, stderr = suite.communicate()
        print stdout
        print stderr

        # generate the coverage report
        if options.get('genhtml'):
            return self.generate_coverage_html()
        else:
            return None

    def generate_coverage_html(self, output_dir=None):
        # generate coverage report with LCOV

        if output_dir:
            self.output_dir = output_dir

        print "Generating Coverage Report..."

        coverage_html = Popen(['genhtml', os.path.join(self.output_dir, 'jsTestDriver.conf-coverage.dat'),
                               '-o', os.path.join(settings.JSTESTDRIVER_OUTPUT, 'html')],
                              stdout=PIPE, stderr=PIPE)

        stdout, stderr = coverage_html.communicate()
        print stdout
        print stderr

        return None