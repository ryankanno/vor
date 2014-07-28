#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(name='vor',
      version='0.0.2',
      description='A tiny Python api to return randomized data',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=['vor'],
      package_dir={'vor': 'vor'},
      package_data={'vor': ['data/*.*']},
      url="https://github.com/ryankanno/vor",
      install_requires=['enum34', 'py_utilities'],
      license='MIT',
      tests_require=['flake8', 'mock', 'nose', 'nosexcover'])

# vim: filetype=python
