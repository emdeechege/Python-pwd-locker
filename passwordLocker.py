#! /usr/bin/env python3
import pyperclip
from smaccounts import User, Credential

def create_user(fstname,lstname,password):
    '''
    Function to create user ac
    '''
    new_user = User(fstname,lstname,password)
    return new_user

def save_user(user):
    '''
    Function to save new users
    '''
    User.save_user(user)

def authenticate_user(fstname,password):
    '''
    Function to verify user is enabled before launching the credentials
    '''
    confirm_user = Credential.confirm_user(first_name,password)
    return confirm_user

# def generate_password():
#     '''
#     Function to automatically gen password
#     '''
#     gen_pwd = Credential.generate_password()
#     return gen_pwd

def create_credential(user_name,social_media,account_name,password):
    '''
    Function creating new credentials
    '''
    new_credential = Credential(user_name,social_media,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    Saves new credentials
    '''
    Credential.save_credentials(credential)

def 

















if __name__ == '__main__':
	main()
