#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from mock import patch
from nose.tools import ok_
from vor.human import Gender
from vor.human import RandomFemale
from vor.human import RandomHuman
from vor.human import RandomMale
import unittest


class TestHuman(unittest.TestCase):

    def _prepare_mock_name_provider(self, mock_name_provider):
        mock_name_provider.get_first_name.return_value = "Bob"
        mock_name_provider.get_last_name.return_value = "Jones"
        return mock_name_provider

    def _prepare_mock_birthday_provider(self, mock_birthday_provider):
        mock_birthday_provider.get_birthday.return_value = \
            datetime.datetime(year=1978, month=10, day=3)
        return mock_birthday_provider

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_human_get_full_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        human = RandomHuman(mock_name, mock_birthday)
        human.full_name
        mock_name.get_first_name.assert_called_with(human.gender)
        mock_name.get_last_name.assert_called_once_with()

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_human_get_first_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        human = RandomHuman(mock_name, mock_birthday)
        human.first_name
        mock_name.get_first_name.assert_called_with(human.gender)
        ok_(mock_name.get_last_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_human_get_last_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        human = RandomHuman(mock_name, mock_birthday)
        human.last_name
        mock_name.get_last_name.assert_called_once_with()
        ok_(mock_name.get_first_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_male_get_full_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        male = RandomMale(mock_name, mock_birthday)
        male.full_name
        mock_name.get_first_name.assert_called_with(Gender.Male)
        mock_name.get_last_name.assert_called_once_with()

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_male_get_first_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        male = RandomMale(mock_name, mock_birthday)
        male.first_name
        mock_name.get_first_name.assert_called_with(Gender.Male)
        ok_(mock_name.get_last_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_male_get_last_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        male = RandomMale(mock_name, mock_birthday)
        male.last_name
        mock_name.get_last_name.assert_called_once_with()
        ok_(mock_name.get_first_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_female_get_full_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        female = RandomFemale(mock_name, mock_birthday)
        female.full_name
        mock_name.get_first_name.assert_called_with(Gender.Female)
        mock_name.get_last_name.assert_called_once_with()

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_female_get_first_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        female = RandomFemale(mock_name, mock_birthday)
        female.first_name
        mock_name.get_first_name.assert_called_with(Gender.Female)
        ok_(mock_name.get_last_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    @patch('vor.backends.birthday.base.DateProvider')
    def test_female_get_last_name_with_mock_name_provider(
            self, mock_name_provider, mock_birthday_provider):
        mock_name = self._prepare_mock_name_provider(mock_name_provider)
        mock_birthday = self._prepare_mock_birthday_provider(
            mock_birthday_provider)
        female = RandomFemale(mock_name, mock_birthday)
        female.last_name
        mock_name.get_last_name.assert_called_once_with()
        ok_(mock_name.get_first_name.called is False)

# vim: filetype=python
