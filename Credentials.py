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
        
    #*******searching for a account using account name e.g instagram***************************** 
       
    @classmethod
    def find_by_accountname(cls, accountname): #cls takes the whole class
        for Credentials in cls.accounts_list:
            if Credentials.accountname == accountname:
                return Credentials
            
    #*************************check to see if the account  really exists*******************
    
    @classmethod
    def credentials_exists(cls,accountname):
        for Credentials in cls.accounts_list:
            if Credentials.accountname == accountname:
                return True
        return False
    
    #***************************display  account & credentials*************************************************
    @classmethod
    def display_credentials(cls):
        '''
        see our users in our userlist by returning the user list
        '''
        return cls.accounts_list

    
    