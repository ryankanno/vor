#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import datetime
from datetime import timedelta
from random import randint


class DateProvider(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(DateProvider, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def get_birthday(self):
        raise NotImplementedError  # pragma: no cover

    def _get_birthday(self, start, end=None):
        end = end or datetime.datetime.combine(datetime.date.today(),
                                               datetime.time(0, 0))
        assert end >= start
        diff_seconds = int(self._total_seconds(end - start))
        return start + timedelta(seconds=randint(0, diff_seconds))

    def _total_seconds(self, td):
        if hasattr(td, 'total_seconds'):
            return td.total_seconds()
        else:
            return td.days * 24 * 60 * 60 + td.seconds

# vim: filetype=python
