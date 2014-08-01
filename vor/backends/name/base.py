#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

PROVIDERS = {}


class NameProvider(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(NameProvider, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def get_first_name(self, gender):
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    def get_last_name(self):
        raise NotImplementedError  # pragma: no cover

# vim: filetype=python
