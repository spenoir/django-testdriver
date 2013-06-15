import codecs
import os
from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django_testdriver',
    version=__import__('django_testdriver').__version__,
    description='A custom JsTestDriver spec runner etc.',
    author='spenoir',
    author_email='aspence1@gmail.com',
    packages=find_packages(),
    url='http://github.com/spenoir/django_testdriver',

    long_description=read('README.md'),
    install_requires=[
        'pyyaml',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
)
