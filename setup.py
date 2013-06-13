from setuptools import setup, find_packages

setup(
    name='django_testdriver',
    version='0.1.2',
	description='A custom JsTestDriver spec runner etc.',
    author='spenoir',
    author_email='aspence1@gmail.com',
    packages=find_packages(),
    url='http://github.com/spenoir/django_testdriver',

    long_description=open('README.md').read(),
    install_requires=[
        'pyyaml',
        'django-nose',
        'milkman',
        'mock',
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
)
