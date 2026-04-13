import unittest
from calculator import add, subtract, multiply, divide, modulo, power, square_root


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_negative(self):
        self.assertEqual(add(-2, -5), -7)

    def test_add_mixed(self):
        self.assertEqual(add(-3, 10), 7)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-3, -2), -1)

    def test_subtract_to_negative(self):
        self.assertEqual(subtract(2, 9), -7)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)


class TestMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_both_negative(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(99, 0), 0)


class TestDivide(unittest.TestCase):
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(divide(-9, 3), -3)

    def test_divide_float_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestModulo(unittest.TestCase):
    def test_modulo_basic(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_even(self):
        self.assertEqual(modulo(8, 4), 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(5, 0)


class TestPower(unittest.TestCase):
    def test_power_positive(self):
        self.assertEqual(power(2, 10), 1024)

    def test_power_zero_exp(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exp(self):
        self.assertAlmostEqual(power(2, -1), 0.5)

    def test_power_zero_base(self):
        self.assertEqual(power(0, 5), 0)


class TestSquareRoot(unittest.TestCase):
    def test_sqrt_perfect_square(self):
        self.assertEqual(square_root(25), 5)

    def test_sqrt_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_sqrt_float_result(self):
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == '__main__':
    unittest.main()
