class Credentials:
    """
    initializes a new credentials class
    """
    user_list=[] #our list where we shall store our users
    def __init__(self, accountname, accountusername, accountpasscode):
        """
        the method here for defining properties of the object
        """
        self.accountname = accountname
        self.accountusername = accountusername
        self.accountpasscode = accountpasscode
    