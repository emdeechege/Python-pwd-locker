import unittest # Importing the unittest module
from smaccounts import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def setUp(self):
        '''
        Function to help create user a/c details before each test
        '''
        self.new_user = User("Tom","Chege","angry")

    def test_init_(self):
        '''
        Test to check creation of new user instance
        '''
        self.assertEqual(self.new_user.first_name,"Tom")
        self.assertEqual(self.new_user.last_name,"Chege")
        self.assertEqual(self.new_user.password,"angry")

    def test_save_user(self):
        '''
        Test to check if New user information is saved into the users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def tearDown(self):
        '''
        tearDown method that executes a set of instructions after every test
        '''
        User.users_list = []














































if __name__ == '__main__':
    unittest.main()
