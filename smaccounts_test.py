import unittest # Importing the unittest module
import pyperclip#helps in copy and paste functions

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
        active_user = Credential.confirm_user("Tim","angry")
        self.assertTrue(active_user)

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
        self.assertEqual(self.new_credential.social_media,"Facebook")
        self.assertEqual(self.new_credential.account_name,"ivan2")
        self.assertEqual(self.new_credential.password,"pwdhappy")

    def test_save_credentials(self):
        '''
        Test and confirm that the new credential information is being saved
        '''
        self.new_credential.save_credentials()
        snapchat = Credential("Ivan","snapchat","ivyivy","f4578n")
        snapchat.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)

    def tearDown(self):
        '''
        tearDown method that executes a set of instructions after every test
        '''
        User.users_list = []
        Credential.credentials_list = []

    def test_display_credentials(self):
        '''
        Test to confirm user can view the correct credential details
        '''
        self.new_credential.save_credentials()
        snapchat = Credential("Ivan","snapchat","ivyivy","f4578n")
        snapchat.save_credentials()
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)

    def test_search_social_media(self):
        '''
        Test to confirm if the method returns the correct social media credential
        '''
        self.new_credential.save_credentials()
        snapchat = Credential("Ivan","snapchat","ivyivy","f4578n")
        snapchat.save_credentials()
        credential_exists = Credential.search_social_media("snapchat")
        self.assertEqual(credential_exists,snapchat)

    def test_copy_credential(self):
        '''
        Test to check if the copy credential method will copy the correct credential details
        '''
        self.new_credential.save_credentials()
        snapchat = Credential("Ivan","snapchat","ivyivy","f4578n")
        snapchat.save_credentials()
        find_credential = None
        for credential in Credential.credentials_list:
            find_credential = Credential.search_social_media(credential.social_media)
            return pyperclip.copy(find_credential.password)
        # credential.copy_credential(self.new_credential.social_media)
        self.assertEqual("f4578n",pyperclip.paste())
        print(pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
