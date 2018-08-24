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

def authenticate_user(first_name,password):
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
        print("-",)
        print('Use these codes to navigate: \n ca-Create an Account\n li-Log In \n ex-Exit')
        short_code = input('Please enter your choice: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-",)
            print(' ')
            print('Create New Account: ')
            first_name = input ('Enter your First name- ').strip()
            last_name = input ('Enter your Last name- ').strip()
            password = input ('Enter your password- ').strip()
            save_user(create_user(first_name,last_name,password))
            print(" ")
            print(f'New Account Created for: {first_name} {last_name} using password: {password}')
        elif short_code == 'li':
            print("-"*60)
            print(' ')
            print('To login, enter your account details:')
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = authenticate_user(user_name,password)
            if user_exists == user_name:
                print(f'Welcome {user_name}. Please choose an option to proceed.')
                print(' ')
                while True:
                    print("-",)
                    print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n ex-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-",)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {user_name}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        social_media = input('Enter the social media\'s name- ').strip()
                        account_name = input('Enter your account\'s name - ').strip()
                        while True:
                            print(' ')
                            print("-")
                            print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                            psw_choice = input('Enter an option: ').lower().strip()
                            print("-")
                            if psw_choice == 'ep':
                                print(" ")
                                password = input('Enter your password: ').strip()
                                break
                            elif psw_choice == 'gp':
                                password = generate_password()
                                break
                            elif psw_choice == 'ex':
                                break
                            else:
                                print('Check! Wrong option entered. Try again.')
                                save_credential(create_credential(user_name,social_media,account_name,password))
                                print(' ')
                                print(f'Credential Created: Social Media: {social_media} - Account Name: {account_name} - Password: {password}')
                                print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):
                            print('Great! Here is a list of all your credentials')
                            print(' ')
                            for credential in display_credentials(user_name):
                                print(f'Social Media: {credential.social_media} - Account Name: {credential.account_name} - Password: {credential.password}')
                                print(' ')
                            else:
                                print(' ')
                                print("You don't seem to have any credentials saved yet")
                                print(' ')
                        else:
                            print(' ')
                            print('Check! Wrong details entered. Try again or Create an Account.')
                    # else:
                    #     print("-")
                    #     print(' ')
                    #     print('Check! Wrong option entered. Try again.')

if __name__ == '__main__':

    main()
