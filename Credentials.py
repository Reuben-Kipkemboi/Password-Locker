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
    #*************************saving new account details*****************************************
    def save_Credentials(self):
        Credentials.accounts_list.append(self)
        
    #********************deleting credentials**************************
    def delete_Credentials(self):
        """
        removing credentails from accounts_list
        """
        Credentials.accounts_list.remove(self)
    