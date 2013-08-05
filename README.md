=======
django-testdriver
=================

[![Build Status](https://travis-ci.org/spenoir/django-testdriver.png?branch=master)](https://travis-ci.org/spenoir/django-testdriver)
[![PyPi version](https://pypip.in/v/django_testdriver/badge.png)](https://crate.io/packages/django_testdriver/)
[![PyPi downloads](https://pypip.in/d/django_testdriver/badge.png)](https://crate.io/packages/django_testdriver/)

Django integration of JsTestDriver

Requirements
------------
To install:

    pip install django-testdriver

You will also need to install LCOV (if you want to see a coverage report) from here:

    http://sourceforge.net/projects/ltp/files/Coverage%20Analysis/LCOV-1.9/lcov-1.9.tar.gz/download

Installation
------------

Add django-testdriver to installed apps.

	INSTALLED_APPS = (
	...
	'django_testdriver',
	...
	)

Urls
----

Set up the django-testdriver urls. django-testdriver will own the url /test/.

	from django_testdriver import settings as django_testdriver_settings

	(r'^django-testdriver/', include('django_testdriver.urls')),
    (r'^test/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(django_testdriver_settings.MEDIA_ROOT) }),

Example
-------

You'll find an example test setup and suite in the example folder. Copy the 'js' dir and the .conf file
into your projects MEDIA_ROOT dir.
You can of course change the jsTestDriver.conf file paths to point to whatever tests you have.
The example uses Jasmine as a Test Runner although any JsTestDriver supported tests should work.

Management command
------------------
Run the following command to start the JsTestDriver server:

    python manage.py jstestdriver

This command also runs the jasmine specs specified
in jsTestDriver.conf. The management command captures Google Chrome by default, it is currently
set up for the default mac install path. This is configurable by setting the JSTESTDRIVER_BROWSER_PATH
setting in settings.py:

    JSTESTDRIVER_BROWSER_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

You can set multiple browsers separated by a comma, not a python list.


After you have ran the jstestdriver management command you should see something here:
http://localhost:9876/

Hit this url in a browser to capture that browser: http://localhost:9876/capture if Chrome and FF don't
open automatically. When you run the tests via the jstestdrier management command, the captured
browsers will each run the specs you have defined so if you have one test and two browsers captured,
JsTestDriver will show that two test were run.
Alternatively you can just specify the browsers in settings as described above.

Dashboard
---------
The Spec Runner and coverage report is available at this url /django-testdriver/jasmine/

You can refresh the Spec Runner page after writing or modifying a spec to see the result
in the runner. This is pretty much all you need for local testing, although you might want to
run the management command once in a while to get a coverage report update...

Coverage
--------
To update the coverage, you will need to run the management command as this is how the static
files are generated using genhtml. You will also need to install LCOV (see Requirements above).

Settings
--------
These settings are all just ported over from <a href="http://code.google.com/p/js-test-driver/">JsTestDriver</a>
jsTestDriver.conf settings

    JSTESTDRIVER_PATH = 'JsTestDriver.jar'
The path to JsTestDriver.jar relative to django root. It must be called 'JsTestDriver.jar'

    JSTESTDRIVER_CONFIG = 'jsTestDriver.conf'
The path to jsTestDriver.conf relative to django root. It must be called 'jsTestDriver.conf'

    JSTESTDRIVER_OUTPUT = 'assets/js/tests/output/'
Folder to which coverage reports get created

    JSTD_PORT = "9876"
Port number for JsTestDriver

    JSTESTDRIVER_BROWSER_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
You can specify multiple browsers - comma separated

    JSTESTDRIVER_PLUGIN_PATHS = "plugins/coverage-1.2.2.jar"
You can specify multiple plugins - comma separated
for coverage to work, the coverage jar must be placed in a folder one below JSTESTDRIVER_PATH

    JSTESTDRIVER_REMOVE_FROM_VIEW = ['assets/js/libs/jasmine-adapter.js']
A list of files to remove from custom spec runner view,
jasmine-adapter must be removed as it causes an error in spec runner, required for jasmine support in
jstestdriver

    COVERAGE_HTML_PATH = 'html/index.html'
path to LCOV html output, parses Coverage xml into html using the genhtml command

Still to Do / In the pipeline
-----------------------------

- Remove JsTestDriver.jar and the coverage plugin out of the project root and create an option
in the management command to download it.
