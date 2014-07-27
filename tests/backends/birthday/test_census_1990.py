#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from nose.tools import ok_
from vor.backends.birthday.oldest_1900 import Oldest1900Provider
import unittest


# TODO: Should mock these
class TestOldest1900(unittest.TestCase):

    def test_oldest_1900_provider(self):
        provider = Oldest1900Provider()
        base = datetime.datetime(year=1900, day=1, month=1)
        for x in xrange(1000):
            ok_(provider.get_birthday() > base)


# vim: filetype=python
