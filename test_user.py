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
    def test_init(self):
        self.assertEqual(self.new_user.firstname,"Reuby")
        self.assertEqual(self.new_user.lastname,"Doe")
        self.assertEqual(self.new_user.username,"DoeReuby") 
        self.assertEqual(self.new_user.password,"0000")
        
    #saing our new user 
    def test_save_User(self):
        self.new_user.save_User()
        self.assertEqual(len(User.user_list),1)
if __name__ == '__main__':
    unittest.main()
        