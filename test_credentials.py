import unittest # importing the unittest module
from Credentials import Credentials #importing the user class to our test script

class TestCredentials(unittest.TestCase):
    """
    subclass with unitest.testcase to help us in creation of testcases.
    the subclass TestUser inherits from the unittest.TestCase
    """
    #1. run a test to see if an object is instantiated correctly
    def setUp(self):
        #creating our new accounts object
        self.new_credentials = Credentials("twitter", "Doe","0000") 
    def tearDown(self):
        '''
        tearDown runs after every test case is complete.
        '''
        Credentials.accounts_list = []
            
    def test_init(self):
        self.assertEqual(self.new_credentials.accountname,"twitter")
        self.assertEqual(self.new_credentials.accountusername,"Doe")
        self.assertEqual(self.new_credentials.accountpasscode,"0000")
        
    #2. **********************saving our new account details **********************
    def test_save_Credentials(self):
        self.new_credentials.save_Credentials()
        self.assertEqual(len(Credentials.accounts_list),1)
        
    #3.********************** Deleting the account details**********************
    def test_delete_Credentials(self):
        #To delete we save another user then later check if the list still has the other user
        self.new_credentials.save_Credentials()
        new_credentials = Credentials("Facebook", "Doe", "1111")
        new_credentials.save_Credentials()
        #Lets perform the delete function and assert to see if the list length will reduce
        self.new_credentials.delete_Credentials()
        self.assertEqual(len(Credentials.accounts_list),1)

if __name__ =="__main__":
    unittest.main()