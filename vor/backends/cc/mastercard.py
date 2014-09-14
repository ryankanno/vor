#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import CreditCardProvider
from .gencc import mastercardPrefixList
from .gencc import credit_card_number
from random import Random


class MastercardProvider(CreditCardProvider):
    def __init__(self, *args, **kwargs):
        super(MastercardProvider, self).__init__(*args, **kwargs)

    def get_credit_card_number(self):
        return credit_card_number(
            Random().seed(), mastercardPrefixList, 16, 10)

# vim: filetype=python
