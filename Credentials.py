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
        save_credential method saves credentials objects into credentials_list
        '''

        Credentials.crededentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_user method deletes a new credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list  
        

