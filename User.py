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
        self.passcode = passcode
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
    #searching user by passcode
    @classmethod
    def find_by_passcode(cls, passcode): #cls takes the whole class
        for User in cls.user_list:
            if User.passcode == passcode:
                return User
            
    #check to see if the user really exists
    @classmethod
    def user_exist(cls,passcode):
        for User in cls.user_list:
            if User.passcode == passcode:
                return True
        return False
           
    #display users
    @classmethod
    def display_users(userlist):
        '''
        see our users in our userlist by returning the user list
        '''
        return userlist.user_list

        
    #searching for a user using the unique password     
        
        
        