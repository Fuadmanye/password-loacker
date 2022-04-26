#!/usr/bin/env python3.10
from Credentials import Credentials
from user import User 
import random
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_credentials(account_name,account_password):
    '''
    Function to create a new credentials
    '''
    new_credentials = create_credentials(account_name,account_password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    Credentials.delete_credentials()

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def get_credentials(account_name):
    """
    A function that finds and returns a credential
    """
    return Credentials.get_credentials(account_name)



def main():
            print("Hello Welcome to your password locker. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cu - create a new user, cc - create credentials, du - display user, gp - generate password,  del - delete users,  ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("User name ....")
                            user_name = input()

                            print("Password  ...")
                            password = input()

                           

                            save_user(create_user(user_name,password)) # create and save new contact.
                            print ('\n')
                            print(f"New User {user_name} {password} created")
                            print ('\n')

                    if short_code == "cc":
                                print("Enter  account  you want to store, e.g twitter" )
                                print("Account Name: ")
                                account_name = input()
                                print("Enter the password for the account you have created ")
                                account_password = input()
                                print("\n")
                                print("You have successfully added a password to your account!")
                                print(f"Account: {account_name}  Password: {account_password}")
                                print("\n")
                                save_credentials(create_credentials(account_name, account_password))
                                           

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.user_name}  .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                #     elif short_code == 'del':

                #             if del_user():
                #                     print("Are you sure you want to delete")
                #                     print('\n')

                #                     for user in del_user():
                #                             print(f"{user.user_name} {user.password} .....")

                #                     print('\n')
                #             else:
                #                     print('\n')
                #                     print("Deleted successully")
                #                     print('\n')            
                        
                              
                    elif short_code == "del":
                        print("Enter the account name you want to delete below, e.g Twitter")
                        search_account = input()
                        search_account = get_credentials(account_name)
                        del_credentials(get_credentials(account_name))
                        print("\n")
                        print(f"Your account for {search_account.account_name} has been deleted successfully!")

                    elif short_code == "gp":
                                    print(" Generate your password.")
                                    print(" Enter the account you wish to have a password for e.g Instagram, and we will generate a new password ")
                                    account_name = input()
                                    account_password = random.randint(1000, 9999)
                                    print("\n")
                                    print(f"Your generated password is {account_password}")
                                    save_credentials(create_credentials(account_name, account_password)) 
                                    print("\n")       
        

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes") 
                            
if __name__ == '__main__':

 main()

                                  