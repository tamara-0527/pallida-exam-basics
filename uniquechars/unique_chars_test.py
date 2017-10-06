import unittest
import unique_chars

class UniqueCharsTest(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(unique_chars.unique_characters(""), False)

    def test_one_letter(self):
        self.assertEqual(unique_chars.unique_characters("b"), ["b"])

    def test_three_letter(self):
        self.assertEqual(unique_chars.unique_characters("dog"), ["d", "o", "g"])

    def test_three_letter_without_a(self):
        self.assertEqual(unique_chars.unique_characters("cat"), ["c", "t"])


if __name__ == '__main__':
    unittest.main()
