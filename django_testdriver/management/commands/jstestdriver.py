from django_testdriver import settings
from django.core.management.base import BaseCommand

from django_testdriver.utils import JsTestDriverHandler

from optparse import make_option

# This management command doesn't do anything other than run JsTestDriver.jar it has the options etc.
# It just makes easier to run for the command line and settings are easily configurable if you are
# used to django. It would also make it easier to change settings for CI integration


class Command(BaseCommand):
    # define options
    option_list = BaseCommand.option_list + (
        make_option("-p", "--port", dest="port", default=settings.JSTD_PORT),
        make_option("-t", "--tests", dest="tests", default="all"),
        make_option("-r", "--reset", dest="reset", default=''),
        make_option("-o", "--testOutput", dest="output", default=settings.JSTESTDRIVER_OUTPUT),
        # can specify multiple browsers
        make_option("-b", "--browser", dest="browser", default=settings.JSTESTDRIVER_BROWSER_PATH),
        make_option("-g", "--genhtml", dest="genhtml", default=False, action="store_true"),
        # make_option("-v", "--verbose", dest="verbose", default=False),
        make_option("-l", "--plugins", dest="plugins", default=settings.JSTESTDRIVER_PLUGIN_PATHS),
    )
    """
        JsTestDriver full list of options available
        ----------------------------------------------
        --browser VAR             : The path to the browser executable
        --browserTimeout VAR      : The ms before a browser is declared dead.
        --captureConsole          : Capture the console (if possible) from the browser
        --config VAL              : Loads the configuration file
        --dryRunFor VAR           : Outputs the number of tests that are going to be run as well as their names for a set of expressions or all to see all the tests
        --help                    : Help
        --port N                  : The port on which to start the JsTestDriver server
        --preloadFiles            : Preload the js files
        --requiredBrowsers VAR    : Browsers that all actions must be run on.
        --reset                   : Resets the runner
        --server VAL              : The server to which to send the command
        --serverHandlerPrefix VAL : Whether the handlers will be prefixed with jstd
        --testOutput VAL          : A directory to which serialize the results of the tests as XML
        --tests VAR               : Run the tests specified by the supplied regular expression. Use '#' to denote the separation between a testcase and a test.
        --verbose                 : Displays more information during a run
        --plugins VAL[,VAL]       : Comma separated list of paths to plugin jars.
        --config VAL              : Path to configuration file.
        --basePath VAL            : Override the base path in the configuration file. Defaults to the parent directory of the configuration file.
        --runnerMode VAL          : The configuration of the logging and frequency that the runner reports actions: DEBUG, DEBUG_NO_TRACE, DEBUG_OBSERVE, PROFILE, QUIET (default), INFO
        --serverHandlerPrefix     : Prefix for all jstd paths (to avoid conflict with proxy)
    """

    def handle(self, **options):
        testdriver_server_path = "http://localhost:%s" % options.get('port')
        JsTestDriverHandler(testdriver_server_path, options)

