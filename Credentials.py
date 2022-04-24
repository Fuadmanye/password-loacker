class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = [] # Empty credential list

    def __init__(self,account_name,account_password):

        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):

        '''
        save_user method saves credentials objects into credentials_list
        '''

        Credentials.crededentials_list.append(self)

