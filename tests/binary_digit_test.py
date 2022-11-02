from unittest import TestCase
from bin_digits import BinaryDigit


class TestBinaryDigits(TestCase):
    def test_init(self):
        data = {
            '1010': 10,
            '1': 1,
            '0': 0,
            '1111': 15,
            '0000': 0
        }
        for binary, decimal in data.items():
            self.assertEqual(BinaryDigit(binary).dec, decimal)

    def test_from_decimal(self):
        data = {
            '1010': 10,
            '1': 1,
            '0': 0,
            '1111': 15
        }
        for binary, decimal in data.items():
            self.assertEqual(BinaryDigit.from_decimal(decimal).data, binary)

    def test_negative(self):
        from_binary_to_decimal = {
            '-101': -5,
            '-0': 0,
            '-1111': -15
        }
        for binary, decimal in from_binary_to_decimal.items():
            self.assertEqual(BinaryDigit(binary).dec, decimal)

        from_decimal_to_binary = {
            '-101': -5,
            '0': 0,
            '-1111': -15
        }
        for binary, decimal in from_decimal_to_binary.items():
            self.assertEqual(str(BinaryDigit.from_decimal(decimal)), binary)

    def test_operations(self):
        data = {
            (4, 2): [6, 2, 8, 2, 16, 1],
            (50, 3): [53, 47, 150, 16, 400, 6]
        }
        for entered, waited_results in data.items():
            first = BinaryDigit.from_decimal(entered[0])
            second = BinaryDigit.from_decimal(entered[1])
            plus = first + second
            minus = first - second
            mul = first * second
            div = first / second
            shl = first << second
            shr = first >> second
            results = [plus, minus, mul, div, shl, shr]
            for result in results:
                self.assertEqual(result.dec, waited_results[results.index(result)])
