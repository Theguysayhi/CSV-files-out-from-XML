import unittest
from CSVextractor import xmlManager as XM

class MyTestCase(unittest.TestCase):
    def setUp(self):
        var = 'foolbar'

    def test_pass(self):
        self.assertEqual(True, False)

    def test_incorrectStartFormat(self):
        self.assertEqual(True, False)

    def test_incorrectEndFormat(self):
        self.assertEqual(True, False)

    def test_whitespaces(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
