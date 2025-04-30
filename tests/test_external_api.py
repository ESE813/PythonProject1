import unittest
from unittest.mock import Mock
from unittest.mock import patch

from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    def test_convert_to_rub_rub_currency(self):
        """Проверяет, что RUB не конвертируется"""
        result = convert_to_rub(100, "RUB")
        self.assertEqual(result, 100.0)

    @patch("src.external_api.requests.get")
    @patch("src.external_api.API_TOKEN", "fake_token")
    def test_convert_to_rub_usd_success(self, mock_get):
        """Проверяет успешную конвертацию через API"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 8900.0}
        mock_get.return_value = mock_response

        result = convert_to_rub(100, "USD")

        mock_get.assert_called_once()
        self.assertEqual(result, 8900.0)

    @patch("src.external_api.requests.get")
    @patch("src.external_api.API_TOKEN", "fake_token")
    def test_convert_to_rub_api_failure(self, mock_get):
        """Проверяет ошибку при статусе ответа != 200"""
        mock_response = Mock()
        mock_response.status_code = 403
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            convert_to_rub(100, "USD")

        self.assertIn("Currency conversion failed", str(context.exception))
