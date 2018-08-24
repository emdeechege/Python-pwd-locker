import unittest # Importing the unittest module
from smaccounts import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours
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

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def test_confirm_user(self):
        '''
        Function to confirm login details to active user
        '''
        self.new_user = User("Tom","Chege","angry")
        self.new_user.save_user()
        userX= User("Tim","Chege","angry")
        userX.save_user()

        for user in User.users_list:
            if user.first_name == userX.first_name and user.password == userX.password:
                active_user = user.first_name
                return active_user
                self.assertEqual(active_user,Credential.confirm_user(userX.password,userX.first_name))

    def setUp(self):
        '''
        Function to create social media account credentials before each test
        '''
        self.new_credential = Credential("Ivan", "Facebook","ivan2","pwdhappy")

    def test__init__(self):
        '''
        Confirm that instance of credentials creation is as expected
        '''
        self.assertEqual(self.new_credential.user_name,"Ivan")
        self.assertEqual(self.new_credential.user_social_media,"Facebook")
        self.assertEqual(self.new_credential.user_account_name,"ivan2")
        self.assertEqual(self.new_credential.user_password,"pwdhappy")

        













































if __name__ == '__main__':
    unittest.main()
