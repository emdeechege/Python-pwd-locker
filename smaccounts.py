class User:
    '''
    Class to create new user accounts and save the same to help in accesssing the pwd locker
    '''

    def _init_(self,first_name,last_name,password):
        '''
        Method to define the properties of the object
        '''
    def save_user(self):
        '''
        save user details method into users_list
        '''

        User.users_list.append(self)
