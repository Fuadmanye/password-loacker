class User:
    """
    Class that generates new instances of users
    """
    contact_list = [] # Empty contact list


    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
        