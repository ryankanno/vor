#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mock import patch
from nose.tools import ok_
from vor.human import Gender
from vor.human import RandomFemale
from vor.human import RandomHuman
from vor.human import RandomMale
import unittest


class TestHuman(unittest.TestCase):

    def _prepare_mock_provider(self, mock_provider):
        mock_provider.get_first_name.return_value = "Bob"
        mock_provider.get_last_name.return_value = "Jones"
        return mock_provider

    @patch('vor.backends.name.base.NameProvider')
    def test_human_get_full_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        human = RandomHuman(mock_provider)
        human.full_name
        mock_provider.get_first_name.assert_called_with(human.gender)
        mock_provider.get_last_name.assert_called_once_with()

    @patch('vor.backends.name.base.NameProvider')
    def test_human_get_first_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        human = RandomHuman(mock_provider)
        human.first_name
        mock_provider.get_first_name.assert_called_with(human.gender)
        ok_(mock_provider.get_last_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    def test_human_get_last_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        human = RandomHuman(mock_provider)
        human.last_name
        mock_provider.get_last_name.assert_called_once_with()
        ok_(mock_provider.get_first_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    def test_male_get_full_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        male = RandomMale(mock_provider)
        male.full_name
        mock_provider.get_first_name.assert_called_with(Gender.Male)
        mock_provider.get_last_name.assert_called_once_with()

    @patch('vor.backends.name.base.NameProvider')
    def test_male_get_first_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        male = RandomMale(mock_provider)
        male.first_name
        mock_provider.get_first_name.assert_called_with(Gender.Male)
        ok_(mock_provider.get_last_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    def test_male_get_last_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        male = RandomMale(mock_provider)
        male.last_name
        mock_provider.get_last_name.assert_called_once_with()
        ok_(mock_provider.get_first_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    def test_female_get_full_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        female = RandomFemale(mock_provider)
        female.full_name
        mock_provider.get_first_name.assert_called_with(Gender.Female)
        mock_provider.get_last_name.assert_called_once_with()

    @patch('vor.backends.name.base.NameProvider')
    def test_female_get_first_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        female = RandomFemale(mock_provider)
        female.first_name
        mock_provider.get_first_name.assert_called_with(Gender.Female)
        ok_(mock_provider.get_last_name.called is False)

    @patch('vor.backends.name.base.NameProvider')
    def test_female_get_last_name_with_mock_provider(self, mock_provider):
        mock_provider = self._prepare_mock_provider(mock_provider)
        female = RandomFemale(mock_provider)
        female.last_name
        mock_provider.get_last_name.assert_called_once_with()
        ok_(mock_provider.get_first_name.called is False)

# vim: filetype=python
