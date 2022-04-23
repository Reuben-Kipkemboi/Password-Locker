import unittest # importing the unittest module
from Credentials import Credentials #importing the user class to our test script

# class TestCredentials(unittest:unittest.TestCase):
#     """
#     subclass with unitest.testcase to help us in creation of testcases.
#     the subclass TestUser inherits from the unittest.TestCase
#     """
#     #run a test to see if an object is instantiated correctly
#     def setUp(self):
#         #creating our new user object
#         self.new_account = Credentials("twitter","0000") 
#     def tearDown(self):
#             '''
#             tearDown runs after every test case is complete.
#             '''
#             Credentials.credentials_list = []
            
#     def test_init(self):
#         self.assertEqual(self.new_account.,"Reuby")
#         self.assertEqual(self.new_user.lastname,"Doe")
