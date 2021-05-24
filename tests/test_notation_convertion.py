import unittest
from convertion.notation_convertion import ConvertNotation


class TestNotationConvertion(unittest.TestCase):
    def setUp(self) -> None:
        self.cn = ConvertNotation()

    def test_decimal_to_binary(self):
        result = self.cn.number_to_base('3')
        self.assertEqual('11', result)

    def test_binary_to_decimal(self):
        result = self.cn.number_to_base('111', 2, 10)
        self.assertEqual(result, '7')

    def test_negative_number(self):
        result = self.cn.number_to_base('-3')
        self.assertEqual(result, '-11')

    def test_negative_number_from_binary_to_decimal(self):
        result = self.cn.number_to_base('-111', 2, 10)
        self.assertEqual(result, '-7')

    def test_from_14_to_7(self):
        result = self.cn.number_to_base('10', 14, 7)
        self.assertEqual(result, '20')

    def test_from_hex_to_binary(self):
        result = self.cn.number_to_base('AAFF', 16, 2)
        self.assertEqual(result, '1010101011111111')

    def test_zero(self):
        result = self.cn.number_to_base('0', 16, 2)
        self.assertEqual(result, '0')

    def test_no_base(self):
        self.assertRaises(ValueError, self.cn.number_to_base, 'FF')


if __name__ == '__main__':
    unittest.main()
