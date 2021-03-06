import leapyear
import unittest

class TestCase(unittest.TestCase):
   def test1_div_by_4(self):
      self.assertEqual(leapyear.div_by_4(16), 1)
   def test2_div_by_4(self):
      self.assertEqual(leapyear.div_by_4(10), 0)
   def test1_div_by_100(self):
      self.assertEqual(leapyear.div_by_100(400), 1)
   def test2_div_by_100(self):
      self.assertEqual(leapyear.div_by_100(372), 0)
   def test1_div_by_400(self):
      self.assertEqual(leapyear.div_by_400(1600), 1)
   def test2_div_by_400(self):
      self.assertEqual(leapyear.div_by_400(432), 0)
   def test1_test_input(self):
      self.assertEqual(leapyear.check_input(300), 1)
   def test2_test_input(self):
      self.assertEqual(leapyear.check_input("Frog"), 0)

   def test1(self):
      self.assertEqual(leapyear.check_leapyear(2080), 1)
   def test2(self):
      self.assertEqual(leapyear.check_leapyear(2045), 0)
   def test3(self):
      self.assertEqual(leapyear.check_leapyear("Dog"), 0)



if __name__ == '__main__':
   unittest.main()
