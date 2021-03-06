import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
   def test_Increment(self):
      self.assertEqual(fizzbuzz.increment(13), 14)
   def test_Mult_3_1(self):
      self.assertEqual(fizzbuzz.check_multiple_of_3(9), 1)
   def test_Mult_3_2(self):
      self.assertEqual(fizzbuzz.check_multiple_of_3(4), 0)
   def test_Mult_5_1(self):
      self.assertEqual(fizzbuzz.check_multiple_of_5(15), 1)
   def test_Mult_5_2(self):
      self.assertEqual(fizzbuzz.check_multiple_of_5(16), 0)

if __name__ == '__main__':
   unittest.main()
