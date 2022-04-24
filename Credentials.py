class Credentials:
    """
    initializes a new credentials class
    """
    accounts_list=[] #our list where we shall store our account details
    def __init__(self, accountname, accountusername, accountpasscode):
        """
        the method here for defining properties of the object
        """
        self.accountname = accountname
        self.accountusername = accountusername
        self.accountpasscode = accountpasscode
    