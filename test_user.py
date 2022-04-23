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
        self.new_user.delete_User()
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()
        