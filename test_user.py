import unittest # importing the unittest module
from User import User #importing the user class to our test script

class TestUser(unittest.TestCase):
    """
    subclass with unitest.testcase to help us in creation of testcases.
    the subclass TestUser inherits from the unittest.TestCase
    """
    #run a test to see if an object is instantiated correctly
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
        self.assertEqual(self.new_user.password,"0000")
        
    #saving our new user 
    def test_save_User(self):
        self.new_user.save_User()
        self.assertEqual(len(User.user_list),1)
        
    #Deleting the user and his details
    def test_delete_User(self):
        #To delete we save another user then later check if the list still has the other user
        self.new_user.save_User()
        another_user = User("John", "Doe", "JohnDoe", "1111")
        another_user.save_User()
        #Lets perform the delete function and assert to see if the list length will reduce
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    
    #we can find a user using his her password this will help us search for user account
    # def test_search_user(self):
    #     self.new_user.save_User()
    #     anothernew_user = User("mary", "Doe", "JohnDoe", "2222")
    #     anothernew_user.save_User()
        
    #     after_search = User.search_by_password("2222")
    #     self.assertEqual(anothernew_user.firstname, anothernew_user.firstname)
    
    #display our users
    def test_display_allour_users(self):
        '''
        we get the users saved in our list
        '''

        self.assertEqual(User.display_users(),User.user_list)

        
        
if __name__ == '__main__':
    unittest.main()
        