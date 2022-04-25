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
    Credentials.save_Credentials()
    
def delete_Credentials(Credentials):
    Credentials.delete_Credentials()
    
def search_credentials(accountname):
    return Credentials.find_by_accountname()

def check_existing_credentials(accountname):
    return Credentials.credentials_exists()

def display_credentials():
    return Credentials.display_credentials()

#Main running appplication &&&&&&&&&*********************
def main():
        print("Hello \U0001F60D, Welcome to Password_Locker\U0001F512!!! No need to master your passcodes.")
        print("**"*35)
             
    #User selection options
        while True: 
            print("Lets create an account or Login to proceed. Use IN to login or CA to Create Account")
            # print("lets proceed use IN or CA")
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
                
                print("Please provide your user Name")
                username = input()
                print("Provide your passcode or Password")
                passcode = input()
                if username == username and passcode ==passcode:
                    print("Successfully Logged In..welcome.......")
                    print("*_#"*20)
                print("\n")
                pass
                while True:
                    print("Use the following initials to create, view and delete accounts")
                    print("CRE to create new credential account")
                    print("SAVE to save existing credentials account details")
                    print("VIEW to create new credential account")
                    print("DEL to create new credential account")
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
                    elif user_input == "SAV":
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
                            print("hello, your credentials list is as follows:...")
                            print("\n")
                            
                            for Credential in display_credentials():
                                print(f"Your{accountname} is as follows:")
                                print("*-"*10)
                                print(f"Account Username ->{accountusername}")
                                print("*-"*10)
                                print(f"Account Passcode ->{accountpasscode}")
                                print("\n")
                                
                        else:
                            print("\n")
                            print("Seems we have no such credentials")
                            print("\n")
                    elif user_input == "DEL":
                        print("Provide the account Name to be deleted")
                        accountname = input()
                        if check_existing_credentials(accountname):
                            account_delete = search_credentials(accountname)
                            delete_Credentials(accountname)
                            print("Account Credentials deleted Successfully")
                        else:
                            print("Such credentials do not exist")
                    
                    elif user_input == "EXIT":
                        print("See you next time..Good day")
                        print("---"*20)
                        print("\n")
                    else:
                        print("do a quick check")
                        print("\n")
                # else:
                #     print("Wrong credentials")
            elif user_input == "IN":
                print("proceed to login")
                
                print("Provide Your Username,....")
                username= input()
                
                print("Passcode....")
                passcode = input()
                if username == username and passcode ==passcode:
                    print("Successfully Logged In..welcome.......")
                    print("*--"*20)
                print("\n")
                  
                
                            
                        
                            
                    
                    
                                
                                
                                
                                
                        
                        
                        
                        
                        
                        
                            
                        
                                    
                
            # elif user_input == "IN":
            #     print("Please provide your user Name")
            #     username = input()
            #     print("Provide your passcode or Password")
            #     passcode = input()
            #     if check_existing_user(passcode):
            #         print("\n")
            #         print("Successfully logged in ...Please go ahead and create(C)and view (V)your different account credentials")
            #         print("*-"*40)
            #         print('C or V')
            #         user_selection = input()
            #         print('\n')
            #         if user_selection == "C":
            #             print("Create your various accounts e.g social media")
            #             print("*-"*40)
            #             print("Provide Account name")
            #             accountname = input()
            #             print("*-"*40)
            #             accountusername = username
            #             print("*-"*40)
            #             print("Provide your account security passcode(CP) or Use Generated Password(GP)")
            #             generatedpassword = input()
            #             if generatedpassword == "GP":
            #                 passwordcharacters = string.ascii_letters +string.digits
            #                 accountpasscode = "".join(user_selection(passwordcharacters )for i in range(6,16))
            #                 print(f"Passcode -> {accountpasscode}")
            #             elif generatedpassword == "CP":
            #                 print("Provide your security key or passcode")
            #                 accountpasscode = input()
            #             else:
            #                 print("provide a better selection")
            #             save_Credentials(create_account(accountname, accountusername, accountpasscode))
            #             print("\n")
            #             print(f"Your account name -> {accountname} \n Account User Name ->  {accountusername} \n Account Passcode ->  {accountpasscode} ")
            #         elif user_selection == "V":
            #             if  display_credentials():
            #                 print("Your Accounts and credentials are as follows:")
            #                 print("*-"*20)
            #                 for credentials in display_credentials(accountname):
            #                     print(f"Account:{accountname} \nPassword/Passcode: {accountpasscode}\n")
            #                 else:
            #                     print("Seems you have no credentials")    
            #             else:
            #                 print('please Try Again and create Account with credentials')     
            #         else:
            #             print("Try again kindly")
            #     else:
            #         print("Check User again")
            # elif user_input == "ex":
            #     print("don't master them anymore, Tell a friend")
            #     break
            # else:
            #     print("make use of shortcodes")
                               
if __name__ == "__main__":
    main()


