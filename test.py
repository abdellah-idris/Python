import unittest
def fibonacci(n):
    if n <= 1:
        return n
    else:
        #recurssion
        return fibonacci(n-1) + fibonacci(n-2)

class MyTestCase(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fibonacci(10), 55 , "this is the correct value" )  # add assertion here
    def test_fiboEroor(self):
        self.assertEqual(fibonacci(9), 55, "the value expected is 34")  # add assertion here


if __name__ == '__main__':
    unittest.main()
