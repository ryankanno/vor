#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class PhoneNumberProvider(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(PhoneNumberProvider, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def get_phone_number(self):
        raise NotImplementedError  # pragma: no cover

# vim: filetype=python
