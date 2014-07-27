#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import DateProvider
import datetime


class Oldest1900Provider(DateProvider):
    def __init__(self):
        super(Oldest1900Provider, self).__init__()

    def get_birthday(self):
        return self._get_birthday(datetime.datetime(year=1900, month=1, day=1))

# vim: filetype=python
