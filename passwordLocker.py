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

def display_credentials(user_name):
    '''
    Function to display_credentials saved by user
    '''
    return Credential.display_credentials(user_name)

# def copy_credential(social_media):
#     '''
#     Function to copy credential details and paste then in clipboard
#     '''
#     return Credential.copy_credential(social_media)
def main():
    print('')
    print('Jambo! Karibu kwenye Password Locker.')
    while True:
        print(' ')
        print("-",*60)
        print('Use these codes to navigate: \n ca-Create an Account\n li-Log In \n ex-Exit')
        short_code = input('Please enter your choice: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-",*60)
            print(' ')
            print('Create New Account: ')
            first_name = input ('Enter your first name- ').strip()
            last_name = input ('Enter your flast name- ').strip()
            password = input ('Enter your password- ').strip()
            save_user(create_user(first_name,last_name,password))
            if user_exists === user_name:
                print(" ")
                print(f'Welcome {user_name}. Please choose an option to proceed.)
                print(' ')
                while True:
                    print("-",*60)
                    print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n ex-Exit')
					short_code = input('Enter your choice: ').lower().strip()
                    print("-",*60)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {user_name})
                        break
                elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						social_media = input('Enter the social media\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
                                    























if __name__ == '__main__':
	main()
