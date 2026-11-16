# https://github.com/AidenK-Gity/lab10-AK-AC
# Partner 1: Aiden Kennedy
# Partner 2: Andrew Citra

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(50, 50), 100)
        self.assertEqual(add(-20, 30), 10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(30, 10), 20)
        self.assertEqual(subtract(-20, 30), -50)
        self.assertEqual(subtract(100, 7), 93)

    ######## Partner 1
     def test_multiply(self): # 3 assertions
         self.assertEqual(mul(3, 4), 12)
         self.assertEqual(mul(0, 3), 0)
         self.assertAlmostEqual(mul(0.2, 4), 0.8)

     def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(0.5, 2), 4)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
            

        
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3.0)
        self.assertEqual(logarithm(10, 1), 0.0)
        self.assertEqual(logarithm(2, 0.5), -1.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 8)

    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
         # call log function inside, example:
         # with self.assertRaises(<INSERT_ERROR_TYPE>):
         #     logarithm(0, 5)
        with self.assertRaises(ValueError):
             log(2, -8)

     def test_hypotenuse(self): # 3 assertions
         self.assertEqual(hypotenuse(3, 4), 5)
         self.assertEqual(hypotenuse(0, 0), 0)
         self.assertAlmostEqual(hypotenuse(1, 1), 1.414, places=3)

     def test_sqrt(self): # 3 assertions
         # Test for invalid argument, example:
         # with self.assertRaises(<INSERT_ERROR_TYPE>):
         #    square_root(NUM)
         # Test basic function
        with self.assertRaises(ValueError):
             square_root(-4)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.414, places=3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()