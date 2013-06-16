import os
import urllib2
from django_testdriver import settings
from django.test import TestCase
from django.core.urlresolvers import reverse
from django_testdriver.utils import ParseTestDriverYaml, JsTestDriverHandler

_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
settings.JSTESTDRIVER_CONFIG = os.path.join(_root, 'example/jsTestDriver.conf')
settings.JSTESTDRIVER_OUTPUT = os.path.join(_root, 'js/tests/output')

class YamlParseTests(TestCase):
    """
        At the moment these test rely on jsTestDriver.conf but you could
        easily create a test yaml file for absolute test independence and
        pass it in as first arg to parse_testdriver_conf()
    """

    def test_dashboard_loads(self):
        response = self.client.get(reverse('custom_spec_runner'))
        self.assertEqual(response.status_code, 200)

    def test_yaml_parse(self):
        conf = ParseTestDriverYaml(settings.JSTESTDRIVER_CONFIG)

        self.assertEqual(conf.conf.get('test')[0], 'js/tests/setup.js')
        self.assertEqual(conf.conf.get('serve')[0], 'js/tests/fixtures/test.json')

    def test_parse_conf_int_kwarg(self):
        conf = ParseTestDriverYaml(settings.JSTESTDRIVER_CONFIG, test_int=90)

        self.assertTrue(conf.conf.has_key('test_int'))
        self.assertTrue(conf.conf.has_key('timeout'))


class JsTestDriverHandlerTests(TestCase):
    """
    Tests helpers called from jstestdriver.py management command.
    The java processes called from these methods could perhaps be
    mocked at some point
    """
    def setUp(self):
        self.options = {"port": settings.JSTD_PORT,
                        "tests":"all", "reset": '',
                        "output": settings.JSTESTDRIVER_OUTPUT,
                        "browser": settings.JSTESTDRIVER_BROWSER_PATH,
                        "genhtml": True,
        }
        self.testdriver_server_path = "http://localhost:%s" % self.options.get('port')
        JsTestDriverHandler(self.testdriver_server_path, self.options)

    def test_server_running(self):
        response = urllib2.urlopen(self.testdriver_server_path)
        self.assertEquals(response.code, 200)

    def test_jstestdriver_jar_exists(self):
        self.assertTrue(open(settings.JSTESTDRIVER_PATH))

    def test_jstestdriver_config_exists(self):
        self.assertTrue(open(settings.JSTESTDRIVER_CONFIG))

    def test_coverage_report_html(self):
        self.assertTrue(
            'index.html' in
                os.listdir(
                    os.path.join(settings.JSTESTDRIVER_OUTPUT,'html')
                )
        )