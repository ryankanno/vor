#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

PROVIDERS = {}


class NameProvider(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_first_name(self, gender):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_name(self):
        raise NotImplementedError

# vim: filetype=python
