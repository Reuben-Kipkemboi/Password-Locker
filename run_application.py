#!/usr/bin/env python3.8 
#on top is shebang

from User import User

def create_user(firstname, lastname, username, passcode):
    new_user =User(firstname, lastname, username, passcode)
    return new_user

def save_user(User):
    User.save_user()
def delete_user(User):
    User.delete_user()
def search_user(passcode):
    return User.find_by_passcode()
def check_existing_user(passcode):
    return User.user_exist()
def display_users():
    return User.display_users()

def main():
    print("Hello \U0001F60D , Welcome to Password_Locker! No need to master your passcodes")
    print("\n")
    print("What would you like to do today?")
    
    print
if __name__ == "__main__":
    main()


