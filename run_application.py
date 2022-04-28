#!/usr/bin/env python3.8 
#on top is shebang
import random
import string #to be used in password generation
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
    
def find_by_passcode(passcode):
    return User.find_by_passcode(passcode)

def check_existing_user(passcode):
    return User.user_exist(passcode)

def display_users():
    return User.display_users()

#Account details ******************************************Account Details

def create_account(accountname, accountusername, accountpasscode):
    new_account =Credentials(accountname, accountusername, accountpasscode)
    return new_account

def save_Credentials(Credentials):
    """
    saving account credentials
    """
    Credentials.save_Credentials()
    
def delete_Credentials(Credentials):
    """
    Delete credentials
    """
    Credentials.delete_Credentials()
    
def search_credentials(accountname):
    """
    search credentials
    """
    return Credentials.find_by_accountname(accountname)

def check_existing_credentials(accountname):
    """
    Check existing credentials
    """
    return Credentials.credentials_exists(accountname)

def display_credentials():
    """
    displaying our account credentials
    """
    return Credentials.display_credentials()

#Main running appplication *********************
def main():
        print("Welcome to Password_Locker\U0001F512!!! No need to master your passcodes.")
        print("               ____                          _                    _           ")
        print("              |  _ \                        | |                  | |         ")
        print("              | |_) )  ____  ___   ___      | |      _____   _   | |      ____     _ _   ")
        print("              |  __/  / _  |/ __  / __      | |     /  _  \ /    | |     / __ \   | '_|    ")
        print("              | |    / (_| |\__ \ \__ \     | |___ (  (_)  (  (  | |/ / | (___/   | |    ")
        print("              |_|    \_____| ___/  ___/     |_____) \_____/ \__  |_|\ \  \____    |_| ....    ")
        print("**"*60)
             
    #User selection options
        while True: 
            print("Lets create an account or Exit.CA to Create Account or EXIT to exit password Locker ")
            user_input =input()
            if user_input =="CA":
                print("Proceed to create your password Locker Account")
                print("--"*20)
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
                print("Your password-locker account created successfully...please proceed to login")
                print("--" *20)
                print(f"FullNames -> {firstname}{lastname} \n User Name -> {username} \nPasscode/password -> {passcode}")
                print("\n")
                print(" _______"*5 + "Lets login" + " _______"*5 )     
                print("Please provide your user Name")
                usernameaccount = input()
                print("Provide your passcode or Password")
                passcode = input()
                if usernameaccount == username and passcode ==passcode:
                    print("Successfully Logged In..welcome.......")
                    print("--"*20)
                pass
                while True:
                    print("Use the following initials to create, view and delete accounts")
                    print("CRE to create new credential account")
                    print("SAVE to save existing credentials account details")
                    print("VIEW to view credential account")
                    print("FIND to find user credentails")
                    print("DEL to delete credential account")
                    print("EXIT to exit password locker")
                    
                    user_input = input()
                    if user_input == "CRE":
                        print("Now creating a new credentials account details...")
                        print("*-")
                        
                        print("Enter the account type e.g Twitter , linkedin...")
                        accountname = input()
                        
                        print("Enter your username...")
                        accountusername = input()

                        print("Can we generate a password for you ..Y/N Y(yes) and N(No)")
                        accountpasscode = input()
                        if accountpasscode == "Y":
                            print("provide the length of your passcode e.g 10")
                            passcode_length = int(input())
                            passcodecharacters = string.ascii_letters +string.digits
                            accountpasscode = "".join(random.choice(passcodecharacters )for i in range(passcode_length))
                        elif accountpasscode == "N":
                            print("Please provide your security passcode ....")
                            accountpasscode = input()
                        else:
                            print("check your input once more")
                        
                        save_Credentials(create_account(accountname, accountusername, accountpasscode))
                        print("\n")
                        print("*-"*30)
                        print(f"Your account name -> {accountname} \n Account User Name ->  {accountusername} \n Account Passcode ->  {accountpasscode} ")
                        print("*-"*30)
                        print("\n")
                    elif user_input == "SAVE":
                        print("Lets save your credentials...")
                        print("*-"*30)
                        
                        print("Enter Account type name e.g Linkedin..")
                        accountname = input()
                        
                        print("Enter Account username e.g JohnDoe..")
                        accountusername = input()
                        
                        print("Enter your account security passcode..")
                        accountpasscode = input()
                        
                        save_Credentials(create_account(accountname, accountusername, accountpasscode))
                        print("\n")
                        print(f"hello {accountusername} your credentails saved successfully")
                        print("\n")  
                    elif user_input == "VIEW":
                        if display_credentials():
                            print("hello, your credentials are as follows:...")
                            for Credentails in display_credentials():
                                print("-----"*20)
                                print(f"Account Type -> {accountname}")
                                print(f"Your{accountname} details are as follows:")
                                print("--"*20)
                                print(f"Account Username -> {accountusername}")
                                print("--"*20)
                                print(f"Account Passcode -> {accountpasscode}")
                                print("\n")                                
                        else:
                            print("\n")
                            print("Seems we have no such credentials")
                            print("\n")
                    elif user_input == "DEL":
                        print("Provide the account Name to be deleted")
                        accountname = input()
                        if search_credentials(accountname):
                            accountname = search_credentials(accountname)
                            accountname.delete_Credentials()
                            print("Hello your Account Credentials deleted Successfully")
                            print("--"*50)
                        else:
                            print("Such Account credentials do not exist")
                            
                    elif user_input == 'FIND':
                        print("Enter the account name you want to search for")
                        searchaccountname = input()
                        if check_existing_credentials(searchaccountname):
                            search_credentialsname = search_credentials(searchaccountname)
                            print(f"Account Type Name -> {search_credentialsname.accountname} \n Account UserName -> {search_credentialsname.accountusername} \n Account passcode -> {search_credentialsname.accountpasscode}")
                            print('-'*20)
                           
                        else:
                            print("No such account and credentials")            
                                    
                    elif user_input == "EXIT":
                        print("See you next time..Good day fella")
                        print("---"*20)
                        print("\n")    
                        break   
                else:
                    print("Wrong credentials")
                    
            else:
                print("create and account")
if __name__ == "__main__":
    main()


