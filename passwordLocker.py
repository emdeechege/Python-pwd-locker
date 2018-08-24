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




















if __name__ == '__main__':
	main()
