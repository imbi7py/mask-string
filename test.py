import unittest
import mask_string


class TestMaskString(unittest.TestCase):
    def testMask(self):
        self.assertEqual(mask_string('Hello world!', 2, 7, match_length=False), 'He****rld!')
        self.assertEqual(mask_string('Hello world!', 2, -1, match_length=False), 'He****')
        self.assertEqual(mask_string('Hello world!', 2, 7, mask='...', match_length=False), 'He...rld!')
        self.assertEqual(mask_string('Hello world!', 0, 7, mask='...', match_length=False), '...rld!')
        self.assertEqual(mask_string(''), '')
        self.assertEqual(mask_string(None), None)


if __name__ == '__main__':
    unittest.main()
