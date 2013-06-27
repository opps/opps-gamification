#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from opps import gamification


install_requires = ["opps>=0.2"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Django",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except:
    long_description = gamification.__description__

setup(
    name='opps-gamification',
    namespace_packages=['opps', 'opps.gamification'],
    version=gamification.__version__,
    description=gamification.__description__,
    long_description=long_description,
    classifiers=classifiers,
    keywords='gamification opps cms django apps rules game magazines '
    'websites',
    author=gamification.__author__,
    author_email=gamification.__email__,
    url='http://oppsproject.org',
    download_url="https://github.com/opps/opps-gamification/tarball/master",
    license=gamification.__license__,
    packages=find_packages(exclude=('doc', 'docs',)),
    package_dir={'opps': 'opps'},
    install_requires=install_requires,
    include_package_data=True,
    package_data={
        'gamification': ['templates/*']
    }
)
