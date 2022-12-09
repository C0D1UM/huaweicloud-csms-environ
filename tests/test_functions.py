import os
import unittest
from unittest import mock

import csms


@mock.patch('csms.functions.services.CsmsService')
class LoadEnvTest(unittest.TestCase):

    def test_input_only_secret_name(self, mock_service):
        csms.functions.load_env('secret')

        mock_service.assert_called_once_with()
        mock_service.return_value.get_json_secret.assert_called_once_with('secret', 'latest')

    def test_input_secret_name_and_version_id(self, mock_service):
        csms.functions.load_env('secret', 'v1')

        mock_service.assert_called_once_with()
        mock_service.return_value.get_json_secret.assert_called_once_with('secret', 'v1')

    def test_secret_name_in_env(self, mock_service):
        os.environ['HUAWEICLOUD_SECRET_NAME'] = 'secret'

        csms.functions.load_env()

        mock_service.assert_called_once_with()
        mock_service.return_value.get_json_secret.assert_called_once_with('secret', 'latest')

    def test_no_arg(self, mock_service):
        self.assertRaises(AssertionError, csms.functions.load_env)

        mock_service.assert_not_called()
        mock_service.return_value.get_json_secret.assert_not_called()

    def test_setting_single_env(self, mock_service):
        mock_service.return_value.get_json_secret.return_value = {'KEY': 'VALUE'}

        csms.functions.load_env('secret')

        self.assertEqual(os.environ.get('KEY'), 'VALUE')

    def test_setting_multiple_env(self, mock_service):
        mock_service.return_value.get_json_secret.return_value = {
            'KEY1': 'VALUE1',
            'KEY2': 'VALUE2',
        }

        csms.functions.load_env('secret')

        self.assertEqual(os.environ.get('KEY1'), 'VALUE1')
        self.assertEqual(os.environ.get('KEY2'), 'VALUE2')
