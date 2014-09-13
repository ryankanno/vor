#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import CreditCardProvider
from .gencc import amexPrefixList
from .gencc import credit_card_number
from random import Random


class AmexProvider(CreditCardProvider):
    def __init__(self, *args, **kwargs):
        super(AmexProvider, self).__init__(*args, **kwargs)

    def get_credit_card_number(self):
        return credit_card_number(Random().seed(), amexPrefixList, 15, 5)

# vim: filetype=python
