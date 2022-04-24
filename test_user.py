import unittest # *********************importing the unittest module***************************
from User import User #***************************importing the user class to our test script***************************

class TestUser(unittest.TestCase):
    """
    subclass with unitest.testcase to help us in creation of testcases.
    the subclass TestUser inherits from the unittest.TestCase
    """
    #1. ***************************run a test to see if an object is instantiated correctly**********************
    def setUp(self):
        #creating our new user object
        self.new_user = User("Reuby","Doe","DoeReuby","0000") 
    def tearDown(self):
        '''
        tearDown runs after every test case is complete.
        '''
        User.user_list = []

    def test_init(self):
        self.assertEqual(self.new_user.firstname,"Reuby")
        self.assertEqual(self.new_user.lastname,"Doe")
        self.assertEqual(self.new_user.username,"DoeReuby") 
        self.assertEqual(self.new_user.passcode,"0000")
        
    #2. **********************saving our new user **********************
    def test_save_User(self):
        self.new_user.save_User()
        self.assertEqual(len(User.user_list),1)
        
    #3.********************** Deleting the user and his details**********************
    def test_delete_User(self):
        #To delete we save another user then later check if the list still has the other user
        self.new_user.save_User()
        new_user = User("John", "Doe", "JohnDoe", "")
        new_user.save_User()
        #Lets perform the delete function and assert to see if the list length will reduce
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    
    #4.********************** we can find a user using his her password this will help us search for user account
    def test_search_user(self):
        self.new_user.save_User()
        new_user = User("Mary", "Doe", "MaryDoe", "2222")
        new_user.save_User()
        
        after_search = User.find_by_passcode("2222")
        self.assertEqual(after_search.passcode, new_user.passcode)
        
    #5. **********************checking if user really exists**********************
    def test_user_existence(self):
        '''
        check existence of user.
        '''

        self.new_user.save_User()
        anothernew_user = User("Mary", "Doe", "MaryDoe", "2222")
        anothernew_user.save_User()

        user_exists = User.user_exist("2222")

        self.assertTrue(user_exists)

    
    #6.********************** display our users**********************************
    def test_display_all_our_users(self):
        '''
        we get the users saved in our user list
        '''
        self.assertEqual(User.display_users(),User.user_list)
        
    

        
        
if __name__ == '__main__':
    unittest.main()
        