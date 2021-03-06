import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
   def test_Increment(self):
      self.assertEqual(fizzbuzz.increment(13), 14)

if __name__ == '__main__':
   unittest.main()
