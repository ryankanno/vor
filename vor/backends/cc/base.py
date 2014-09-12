#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class CreditCardProvider(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(CreditCardProvider, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def get_credit_card_number(self):
        raise NotImplementedError  # pragma: no cover

# vim: filetype=python
