import json
import unittest
from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import get_transaction_amount
from src.utils import read_json_file


class TestTransactionFunctions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
    @patch("os.path.exists", return_value=True)
    def test_read_json_file_valid(self, mock_exists, mock_file):
        result = read_json_file("fake_path.json")
        self.assertEqual(result, [{"id": 1}])

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    @patch("os.path.exists", return_value=True)
    def test_read_json_file_not_list(self, mock_exists, mock_file):
        result = read_json_file("fake_path.json")
        self.assertEqual(result, [])

    @patch("os.path.exists", return_value=False)
    def test_read_json_file_not_found(self, mock_exists):
        result = read_json_file("fake_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    @patch("os.path.exists", return_value=True)
    def test_read_json_file_invalid_json(self, mock_exists, mock_file):
        result = read_json_file("fake_path.json")
        self.assertEqual(result, [])

    def test_get_transaction_amount_invalid(self):
        transaction = {"operationAmount": {"amount": None}}
        with self.assertRaises(ValueError):
            get_transaction_amount(transaction)
