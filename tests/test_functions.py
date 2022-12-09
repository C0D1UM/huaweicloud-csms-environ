import unittest
from unittest import mock

import csms


@mock.patch('csms.functions.services.Csms')
class LoadEnvTest(unittest.TestCase):

    def test_input_only_secret_name(self, mock_csms):
        csms.load_env('secret')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.load_env.assert_called_once_with('secret', 'latest')

    def test_input_secret_name_and_version_id(self, mock_csms):
        csms.load_env('secret', 'v1')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.load_env.assert_called_once_with('secret', 'v1')

    def test_input_only_version_id(self, mock_csms):
        csms.load_env(version_id='v1')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.load_env.assert_called_once_with(None, 'v1')

    def test_no_arg(self, mock_csms):
        csms.load_env()

        mock_csms.assert_called_once_with()
        mock_csms.return_value.load_env.assert_called_once_with(None, 'latest')


@mock.patch('csms.functions.services.Csms')
class GetTest(unittest.TestCase):

    def test_input_only_secret_name(self, mock_csms):
        csms.get('secret')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.get_raw_secret.assert_called_once_with('secret', 'latest')

    def test_input_secret_name_and_version_id(self, mock_csms):
        csms.get('secret', 'v1')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.get_raw_secret.assert_called_once_with('secret', 'v1')

    def test_output(self, mock_csms):
        mock_csms.return_value.get_raw_secret.return_value = 'test'

        self.assertEqual(csms.get('secret'), 'test')


@mock.patch('csms.functions.services.Csms')
class GetJsonTest(unittest.TestCase):

    def test_input_only_secret_name(self, mock_csms):
        csms.get_json('secret')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.get_json_secret.assert_called_once_with('secret', 'latest')

    def test_input_secret_name_and_version_id(self, mock_csms):
        csms.get_json('secret', 'v1')

        mock_csms.assert_called_once_with()
        mock_csms.return_value.get_json_secret.assert_called_once_with('secret', 'v1')

    def test_output(self, mock_csms):
        mock_csms.return_value.get_json_secret.return_value = {'key': 'value'}

        self.assertEqual(csms.get_json('secret'), {'key': 'value'})
