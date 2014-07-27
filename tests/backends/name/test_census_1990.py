#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from nose.tools import raises
from vor.human import Gender
from vor.backends.name.census_1990 import Census1990Provider
import unittest


# TODO: Should mock these
class TestCensus1990(unittest.TestCase):

    def test_census_1990_provider(self):
        provider = Census1990Provider()
        ok_(len(provider.get_first_name(Gender.Male)) > 0)
        ok_(len(provider.get_first_name(Gender.Female)) > 0)
        ok_(len(provider.get_last_name()) > 0)

    @raises(ValueError)
    def test_census_1990_provider_with_invalid_gender(self):
        provider = Census1990Provider()
        provider.get_first_name(100)


# vim: filetype=python
