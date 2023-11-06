from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def test_str(self):
        actual = fit_transform(['abc', 'def', 'abc'])
        expected = [('abc', [0, 1]), ('def', [1, 0]), ('abc', [0, 1])]
        self.assertEqual(actual, expected)

    def test_int(self):
        actual = fit_transform([1, 2, 3])
        expected = [(1, [0, 0, 1]), (2, [0, 1, 0]), (3, [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_empty_str(self):
        actual = fit_transform('')
        expected = [('', [1])]
        self.assertEqual(actual, expected)

    def test_output_type(self):
        self.assertIsInstance(fit_transform('abc'), list)

    def test_raises(self):
        with self.assertRaises(TypeError):
            fit_transform()
