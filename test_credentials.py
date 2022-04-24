import unittest # importing the unittest module
from Credentials import Credentials #importing the user class to our test script

class TestCredentials(unittest.TestCase):
    """
    subclass with unitest.testcase to help us in creation of testcases.
    the subclass TestUser inherits from the unittest.TestCase
    """
    #run a test to see if an object is instantiated correctly
    def setUp(self):
        #creating our new accounts object
        self.new_credentails = Credentials("twitter", "Doe","0000") 
    def tearDown(self):
        '''
        tearDown runs after every test case is complete.
        '''
        Credentials.accounts_list = []
            
    def test_init(self):
        self.assertEqual(self.new_credentails.accountname,"twitter")
        self.assertEqual(self.new_credentails.accountusername,"Doe")
        self.assertEqual(self.new_credentails.accountpasscode,"0000")

if __name__ =="__main__":
    unittest.main()