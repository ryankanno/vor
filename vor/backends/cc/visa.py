#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import CreditCardProvider
from .gencc import visaPrefixList
from .gencc import credit_card_number
from random import Random


class VisaProvider(CreditCardProvider):
    def __init__(self, *args, **kwargs):
        super(VisaProvider, self).__init__(*args, **kwargs)

    def get_credit_card_number(self):
        return credit_card_number(Random().seed(), visaPrefixList, 16, 10)

# vim: filetype=python
