import unittest

from euler_001 import Euler001 

from euler_002 import Euler002 

class TestEuler1_10(unittest.TestCase):

  def test_Euler001(self):
      
    tests = [
        (1000, 233168),
        (49, 543),
        (8456, 16687353),
        (19564, 89301183),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler001(value), expected)


  def test_Euler002(self):

    tests = [
      (8, 10),
      (10, 10),
      (34, 44),
      (60, 44),
      (1000, 798),
      (100000, 60696),
      (4000000, 4613732),
    ]

    for value, expected in tests:
        with self.subTest(value=value):
            self.assertEqual(Euler002(value), expected)


	
if __name__ == '__main__':
    unittest.main()