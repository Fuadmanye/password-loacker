import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''

     # Items up here .......

     # setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Fuad","12345") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Fuad")
        self.assertEqual(self.new_user.password,"12345")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''

        self.new_user.save_user()
        test_user = User("Fuad","12345") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)    


if __name__ == '__main__':
    unittest.main()

     