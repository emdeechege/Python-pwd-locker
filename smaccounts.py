import pyperclip
global users
class User:
    '''
    Class to create new user accounts and save the same to help in accesssing the pwd locker
    '''

    users_list = []

    def __init__(self,first_name,last_name,password):
        '''
        Method to define the properties of the object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password= password

    def save_user(self):
        '''
        save user details method into users_list
        '''
        User.users_list.append(self)

class Credential:
    '''
    Class that holds and saves user login details, social media a/c credentials, passwords
    '''
    # Class Variables
    credentials_list =[]
    user_credentials_list = []

    @classmethod
    def confirm_user(cls,first_name,password):
        '''
		Method that checks if the name and password entered match entries in the users_list
		'''
        active_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                active_user = user.first_name
        return active_user

    def __init__(self,user_name,social_media,account_name,password):
        '''
        Method defining the properties each object will hold
        '''

        self.user_name = user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save new user credentials
        '''
        Credential.credentials_list.append(self)

    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display the list of saved credentials
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
                return user_credentials_list

    @classmethod
    def search_social_media(cls, social_media):
        '''
        Method that acccepts social media name and returns credentials matching the site name
        '''
        for credential in cls.credentials_list:
            if credential.social_media == social_media:
                return credential

    # @classmethod
    # def copy_social_media(cls,social_media):
    #     '''
	# 	Class method that copies a credential's info after the credential's site name is entered
	# 	'''
	# 	find_credential = Credential.search_social_media(social_media)
    #     return pyperclip.copy(find_credential.password)
