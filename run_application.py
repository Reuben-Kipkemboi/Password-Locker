#!/usr/bin/env python3.8 
#on top is shebang

from click import option
from User import User
from Credentials import Credentials
#User details.......*******************User details ***************** userdetails ****
def create_user(firstname, lastname, username, passcode):
    new_user =User(firstname, lastname, username, passcode)
    return new_user

def save_User(User):
    User.save_User()
    
def delete_user(User):
    User.delete_user()
    
def search_user(passcode):
    return User.find_by_passcode()

def check_existing_user(passcode):
    return User.user_exist()

def display_users():
    return User.display_users()

#Account details ******************************************Account Details

def create_account(accountname, accountusername, accountpasscode):
    new_account =Credentials(accountname, accountusername, accountpasscode)
    return new_account

def save_Credentials(Credentials):
    Credentials.save_Credentials()
    
def delete_Credentials(Credentials):
    Credentials.delete_Credentials()
    
def search_credentials(accountname):
    return Credentials.find_by_accountname()

def check_existing_credentials(accountname):
    return Credentials.credentials_exists()

def display_Credentials():
    return Credentials.display_credentials()

#Main running appplication &&&&&&&&&***************_____
def main():
        print("Hello \U0001F60D, Welcome to Password_Locker\U0001F512!!! No need to master your passcodes.")
        print("**"*35)
        
        
    #User selection options
        while True: 
            print("Lets create an account or Login to proceed. Use IN to login or CA to Create Account")
            print("lets proceed use IN or CA")
            user_input =input()
            if user_input =="CA":
                print("Proceed to create your password Locker Account")
                print("--"*40)
                print("Enter your First Name")
                firstname = input()
                print("Enter your Last Name")
                lastname = input()
                print("Enter your User Name")
                username = input()
                print("Set your Account passcode/password")
                passcode = input()
                #Saving the user created credentials
                save_User(create_user(firstname, lastname, username, passcode))
                print("Your password-locker account created successfully")
                print("--" *40)
                print(f"FullNames -> {firstname} {lastname} \nUsername -> {username} \nPasscode/password -> {passcode}")
                
            
        
    
    
    
if __name__ == "__main__":
    main()


