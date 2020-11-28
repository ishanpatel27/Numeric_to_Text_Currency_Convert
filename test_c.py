# test file
#author Ishan Patel

import unittest2
from currconvert import currency

a= currency(3850)
b= currency(500)
c="Rs.Fifty   ONLY"

class test_c(unittest2.TestCase):

      def setUp(self):
              pass
            
      def test_curr1(self):
            result=currency(3850)
            self.assertEqual(result,a)

      def test_curr2(self):
            result=currency(500)
            self.assertEqual(result,b)

      def test_curr3(self):
            result=currency(50)
            self.assertEqual(result,c)

      
            

if __name__ == '__main__':
    unittest2.main()

    



