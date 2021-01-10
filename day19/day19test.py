import unittest
from day19 import day19pt1, day19pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day19/input_test1.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day19pt1(x), 2)


    def testpt2(self):
        text_file = open("day19/input_test2.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day19pt2(x), 12)
    
   
if __name__ == "__main__":
    unittest.main()