import unittest
import unique_chars

class UniqueCharsTest(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(unique_chars.unique_characters(""), False)


if __name__ == '__main__':
    unittest.main()
