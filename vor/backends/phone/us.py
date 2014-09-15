#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import PhoneNumberProvider


class UsPhoneNumberProvider(PhoneNumberProvider):
    def __init__(self, *args, **kwargs):
        super(PhoneNumberProvider, self).__init__(*args, **kwargs)

    def get_phone_number(self):
        raise NotImplementedError  # pragma: no cover


# vim: filetype=python
