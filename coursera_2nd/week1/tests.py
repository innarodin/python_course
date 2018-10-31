def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """Проверка, что типы float и str (значения 'string', 1.5) вызывают исключение TypeError."""
        for x in ['string', 1.5]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        """Проверка, что для отрицательных чисел -1, -10 и -100 вызывается исключение ValueError."""
        for x in [-1, -10, -100]:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, i)

    def test_zero_and_one_cases(self):
        """Проверка, что для числа 0 возвращается кортеж (0,), а для числа 1 кортеж (1,)"""
        for x, y in [(0, (0,)), (1, (1,))]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), y)

    def test_simple_numbers(self):
        """Проверка, что для простых чисел 3, 13, 29 возвращается кортеж, содержащий одно данное число."""
        for x, y in [(3, (3,)), (13, (13,)), (29, (29,))]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), y)

    def test_two_simple_multipliers(self):
        """Проверка, что для чисел 6, 26, 121 возвращаются соответственно кортежи (2, 3), (2, 13) и (11, 11)."""
        for x, y in [(6, (2, 3)), (26, (2, 13)), (121, (11, 11))]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), y)

    def test_many_multipliers(self):
        """Проверка, что для чисел 1001 и 9699690 возвращаются соответственно кортежи (7, 11, 13) и (2, 3, 5, 7, 11, 13, 17, 19)."""
        for x, y in [(1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19))]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), y)
