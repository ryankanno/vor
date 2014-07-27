#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import RandomNameBase
from enum import Enum
from enum import unique
import random


@unique
class Gender(Enum):
    Male = 1
    Female = 2


class RandomHuman(RandomNameBase):
    def __init__(self, name_provider, gender=None):
        self._birthday = None
        self._first_name = None
        self._last_name = None
        self._name_provider = name_provider

        self.gender = gender or random.choice([Gender.Male, Gender.Female])
        assert self.gender in list(Gender)

    @property
    def birthday(self):
        if not self._birthday:
            self._birthday = self._birthday_provider.get_birthday()
        return self._birthday

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def first_name(self):
        if not self._first_name:
            self._first_name = self._name_provider.get_first_name(self.gender)
        return self._first_name

    @property
    def last_name(self):
        if not self._last_name:
            self._last_name = self._name_provider.get_last_name()
        return self._last_name

    @property
    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)


class RandomMale(RandomHuman):
    def __init__(self, name_provider):
        super(RandomMale, self).__init__(name_provider, Gender.Male)


class RandomFemale(RandomHuman):
    def __init__(self, name_provider):
        super(RandomFemale, self).__init__(name_provider, Gender.Female)


# vim: filetype=python
