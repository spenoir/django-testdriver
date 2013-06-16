import os
from django.conf import settings
import sys

_root = os.path.dirname(os.path.realpath(__file__))

# JsTestDriver settings
# see also jsTestDriver.conf
STATIC_URL = getattr(settings, 'STATIC_URL')
SITE_ROOT = getattr(settings, 'SITE_ROOT')
MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
STATIC_ROOT = getattr(settings, 'STATIC_ROOT')
JSTESTDRIVER_PATH = getattr(settings, 'JSTESTDRIVER_PATH',
                             os.path.join(_root, 'JsTestDriver.jar'))
JSTESTDRIVER_CONFIG = getattr(settings, 'JSTESTDRIVER_CONFIG',
                               os.path.join(MEDIA_ROOT, 'jsTestDriver.conf'))
JSTESTDRIVER_OUTPUT = getattr(settings, 'JSTESTDRIVER_OUTPUT',
                              os.path.join(MEDIA_ROOT, 'js/tests/output'))
JSTD_PORT = getattr(settings, 'JSTD_PORT', "9876")
# can specify multiple browsers - comma separated
JSTESTDRIVER_BROWSER_PATH = getattr(settings, 'JSTESTDRIVER_BROWSER_PATH',
                                    "/Applications/Firefox.app/Contents/MacOS/Firefox, /Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
# can specify multiple plugins - comma separated
# for coverage to work, the coverage jar must be placed in a folder relative to JSTESTDRIVER_CONFIG
JSTESTDRIVER_PLUGIN_PATHS = getattr(settings, 'JSTESTDRIVER_PLUGIN_PATHS',
                                    os.path.join(_root, "plugins/coverage-1.2.2.jar"))
# list of files to remove from custom spec runner view
# jasmine-adapter must be removed as it causes an error in spec runner
JSTESTDRIVER_REMOVE_FROM_VIEW = getattr(settings, 'JSTESTDRIVER_REMOVE_FROM_VIEW',
                                        ['js/libs/jasmine-adapter.js',])