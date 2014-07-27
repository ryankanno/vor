#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import NameProvider
from .base import PROVIDERS
from vor.human import Gender
from py_utilities.decorators import run_once
import os
import random


class Census1990Provider(NameProvider):

    KEYS = {
        'provider': 'Census1990',
        'm_first': 'male:first_name',
        'f_first': 'female:first_name',
        'last': 'all:last_name'
    }

    def __init__(self):
        super(Census1990Provider, self).__init__()
        self.load_provider_data()

    @run_once
    def load_provider_data(self):
        for (data_source_path, key) in self._get_data_source_keys():
            names = []
            with open(data_source_path) as data_file:
                for line in data_file:
                    name, _, _, _ = line.split()
                    names.append(name.upper())
                PROVIDERS[self._get_prefixed_key(key)] = names

    def get_first_name(self, gender):
        key = self._get_first_name_key_from_gender(gender)
        return random.choice(PROVIDERS[key]).title()

    def get_last_name(self):
        key = self._get_last_name_key()
        return random.choice(PROVIDERS[key]).title()

    def _get_prefixed_key(self, key):
        return "{0}:{1}".format(self.KEYS['provider'], key)

    def _get_first_name_key_from_gender(self, gender):
        if gender == Gender.Male:
            return self._get_prefixed_key(self.KEYS['m_first'])
        elif gender == Gender.Female:
            return self._get_prefixed_key(self.KEYS['f_first'])
        else:
            raise ValueError("Unsupported value in gender enum")

    def _get_last_name_key(self):
        return self._get_prefixed_key(self.KEYS['last'])

    def _get_data_source_keys(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        full_path = lambda x: os.path.join(cwd, x)
        source_keys = [
            ('../../data/1990_census/dist.all.last', self.KEYS['last']),
            ('../../data/1990_census/dist.male.first', self.KEYS['m_first']),
            ('../../data/1990_census/dist.female.first', self.KEYS['f_first'])
        ]
        return [(full_path(source), keys) for source, keys in source_keys]

# vim: filetype=python
