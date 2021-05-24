import unittest

from telegram.symbol_convertion import get_numbers_from_telegram_string


class TestGetNumbers(unittest.TestCase):
    def test_get_numbers(self):
        number, from_base, to_base = get_numbers_from_telegram_string('115 из 66 в 82')
        self.assertEqual(number, '115')
        self.assertEqual(from_base, '66')
        self.assertEqual(to_base, '82')

    def test_get_numbers_2(self):
        number, from_base, to_base = get_numbers_from_telegram_string('115(66)82')
        self.assertEqual(number, '115')
        self.assertEqual(from_base, '66')
        self.assertEqual(to_base, '82')

    def test_get_numbers_3(self):
        number, from_base, to_base = get_numbers_from_telegram_string('115 from 66 to 82')
        self.assertEqual(number, '115')
        self.assertEqual(from_base, '66')
        self.assertEqual(to_base, '82')

    def test_get_numbers_4(self):
        number, from_base, to_base = get_numbers_from_telegram_string('115')
        self.assertEqual(number, '115')
        self.assertIsNone(from_base)
        self.assertIsNone(to_base)
