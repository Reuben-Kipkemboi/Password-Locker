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
        