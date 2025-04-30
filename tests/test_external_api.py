import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):
    def setUp(self):
        self.transaction_rub = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}

        self.transaction_usd = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    def test_convert_rub_no_conversion(self):
        """Проверяет, что сумма в рублях не конвертируется"""
        result = convert_to_rub(self.transaction_rub)
        self.assertEqual(result, 1000.0)

    @patch("src.external_api.requests.get")
    @patch("src.external_api.API_TOKEN", "fake_token")
    def test_convert_usd_success(self, mock_get):
        """Проверяет успешную конвертацию USD → RUB"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 8900.0}
        mock_get.return_value = mock_response

        result = convert_to_rub(self.transaction_usd)

        mock_get.assert_called_once()
        self.assertEqual(result, 8900.0)

    def test_convert_invalid_transaction_structure(self):
        """Проверяет исключение при неверной структуре транзакции"""
        bad_transaction = {"wrong": "data"}

        with self.assertRaises(ValueError):
            convert_to_rub(bad_transaction)
