import unittest
from richardson_extrapolation import RichardsonExtrapolation

class TestRichardsonExtrapolation(unittest.TestCase):

    def test_select_stepsize_with_provided_stepsizes(self):
        h = [1, 0.5, 0.25]
        with self.assertRaises(ValueError):
            RichardsonExtrapolation.select_stepsize(h, 2)

        h0 = [1, 0.5, 0.25]
        h = RichardsonExtrapolation.select_stepsize(h0, 3)
        self.assertEqual(h, h0, 'returns original h')

    def test_select_stepsize_without_provided_stepsizes(self):
        h = RichardsonExtrapolation.select_stepsize(4, 3)
        self.assertEqual(h, [4, 2, 1], 'returns original h')

        h = RichardsonExtrapolation.select_stepsize(4, 2)
        self.assertEqual(h, [4, 2], 'returns original h')

        h = RichardsonExtrapolation.select_stepsize(4, 1)
        self.assertEqual(h, [4], 'returns original h')

    def test_richardson_extrapolation(self):
        f = 5.5
        n = 3.8
        c = 1.2
        func = lambda h: f + c * pow(h, n)

        with self.assertRaises(NotImplementedError):
            RichardsonExtrapolation.richardson(func, 1)

        result = RichardsonExtrapolation.richardson(func, [1, 0.5], {'f': f})
        self.assertAlmostEqual(result['n'], n, places=5, msg='calculates n')
        self.assertAlmostEqual(result['c'], c, places=5, msg='calculates c')

        result = RichardsonExtrapolation.richardson(func, [1, 0.5], {'n': n})
        self.assertAlmostEqual(result['f'], f, places=5, msg='calculates f')
        self.assertAlmostEqual(result['c'], c, places=5, msg='calculates c')

        result = RichardsonExtrapolation.richardson(func, 1, {'f': f})
        self.assertAlmostEqual(result['n'], n, places=5, msg='calculates n')
        self.assertAlmostEqual(result['c'], c, places=5, msg='calculates c')

        result = RichardsonExtrapolation.richardson(func, 1, {'n': n})
        self.assertAlmostEqual(result['f'], f, places=5, msg='calculates f')
        self.assertAlmostEqual(result['c'], c, places=5, msg='calculates c')

if __name__ == '__main__':
    unittest.main()
