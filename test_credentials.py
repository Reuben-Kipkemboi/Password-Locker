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
        
    #4.********************** we can find credentials using the account name
    
    def test_search_credentials(self):
        self.new_credentials.save_Credentials()
        new_credentials = Credentials("Instagram", "Doe","2222")
        new_credentials.save_Credentials()
        
        after_search = Credentials.find_by_accountname("Instagram")
        self.assertEqual(after_search.accountname, new_credentials.accountname)
        
    #5. **********************checking if credentials really do  exist**********************
    
    def test_account_existence(self):
        '''
        check existence of accounts.
        '''
        self.new_credentials.save_Credentials()
        anothernew_credentials = Credentials("Instagram", "Doe","2222")
        anothernew_credentials.save_Credentials()

        credentials_exists = Credentials.credentials_exists("Instagram")

        self.assertTrue(credentials_exists)
        
    #6.********************** display all accounts and credentials**********************************
    
    def test_display_all_our_credentials(self):
        '''
        we display all the accounts and credentials saved in our list
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.accounts_list)
        
#Main unittest
if __name__ =="__main__":
    unittest.main()