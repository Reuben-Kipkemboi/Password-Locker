class User:
    """
    initializes a new User class
    """
    user_list=[] #our list where we shall store our users
    def __init__(self, firstname, lastname, username, passcode):
        """
        the method here for defining properties of the object
        """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = passcode
    #saving new user
    def save_User(self):

        """
        save_User append the new user to our list
        """

        User.user_list.append(self)
    #deleting or removing our new user
    def delete_user(self):
        """
        removing user form the list
        """
        User.user_list.remove(self)
        
        
        