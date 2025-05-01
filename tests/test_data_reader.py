import unittest
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
from src.data_reader import read_transactions_from_csv, read_transactions_from_excel


class TestDataReader(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="id,amount,currency\n1,100,USD\n2,200,RUB")
    @patch("pathlib.Path.exists", return_value=True)
    def test_read_transactions_from_csv_success(self, mock_exists, mock_file):
        result = read_transactions_from_csv("data/transactions.csv")
        expected = [{"id": "1", "amount": "100", "currency": "USD"}, {"id": "2", "amount": "200", "currency": "RUB"}]
        self.assertEqual(result, expected)

    @patch("builtins.open", side_effect=OSError("File error"))
    @patch("pathlib.Path.exists", return_value=True)
    def test_read_transactions_from_csv_error(self, mock_exists, mock_file):
        result = read_transactions_from_csv("data/transactions.csv")
        self.assertEqual(result, [])

    @patch("pandas.read_excel")
    @patch("pathlib.Path.exists", return_value=True)
    def test_read_transactions_from_excel_success(self, mock_exists, mock_read_excel):
        mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel("data/transactions_excel.xlsx")
        expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        self.assertEqual(result, expected)

    @patch("pandas.read_excel", side_effect=Exception("Read error"))
    @patch("pathlib.Path.exists", return_value=True)
    def test_read_transactions_from_excel_error(self, mock_exists, mock_read_excel):
        result = read_transactions_from_excel("data/transactions_excel.xlsx")
        self.assertEqual(result, [])

    @patch("pathlib.Path.exists", return_value=False)
    def test_read_transactions_from_excel_file_not_found(self, mock_exists):
        result = read_transactions_from_excel("data/transactions_excel.xlsx")
        self.assertEqual(result, [])
