from random import randint
import sys

class Bank:  
    def __init__(self):
        #holds acount information [account_key][0] => user_name ; [account_key][1] => balance
        self._accounts = {} 
    
    def _accountGenerator(self):
        account_number = randint(10000,99999)
        return account_number
    
    def _authenticateAccount(self, user: str, account_number: int) -> bool:
        if account_number in self._accounts.keys():
            if self._accounts[account_number][0] == user:
                return True
            else:
                return False
        else:
            return False
        
    def addAccount(self, account_number: int, user: str, amount: float):
        """Add account information to account dictionary
        
        Args:
            user: User name input
            accr_num: Account number input
            
        Returns:
            bool: If account information exists return True, False otherwise
        """
        self._accounts[account_number] = [user, amount]
        
    def balance(self, account_number: int):
        """Get balance from account dictionary 
        
        Args:
            account_number: account number 
            
        Returns:
            Looks for account number and returns balance
        """        
        return self._accounts[account_number][1]
    
    def deposit(self, account_number: int, deposit: float):
        """Deposit value into an account's balance 
        
        Args:
            account_number: account number
            deposit: deposit value from user
            
        Returns:
            Adds the deposit amount to the account's balance
        """ 
        self._accounts[account_number][1] += deposit
        
    def withdraw(self, account_number: int, withdrawal: float) -> bool:
        """Checks for funds and withdraws accordingly
        
        Args:
            account_number: account number
            withdrawal: withdrawal value from user
            
        Returns:
            If there's not enough funds return False, 
            otherwise deduct the amount from balance and return True
        """ 
        if (withdrawal <= self._accounts[account_number][1]):
            self._accounts[account_number][1] -= withdrawal
            return True
        else:
            return False
            

class Interface(Bank): 
    def displayMainMenu(self):
        choice  = -1
        menu = """
        Enter choice (1-3)
        1. Create a new account
        2. Access account
        3. Exit
        """
        
        while True:
            choice = input(menu)
            try:
                value = int(choice)
                if (value == 1):
                    print("Adding new user..")
                    self._createAccount()
                elif (value == 2):
                    print("Acessing new account..")
                    self._accessAccount()
                elif (value == 3):
                    print("Thank you for using Py bank!")
                    break
                else:
                    print("Choose a number from 1-3")
            except ValueError:
                print("Invalid input")
                continue
    
    def _displayAcctMenu(self):
        menu = """
        Enter choice (1-3)
        1. Make a deposit
        2. Make a withdrawal
        3. Display Balance
        4. Log Out
        """        
        while True:
            choice = input(menu)
            try:
                value = int(choice)
                if (value == 1):
                    print("Making a deposit..")
                    amount = self.getDeposit()
                    if not amount:
                        return
                    self.deposit(self.acct_num, amount)
                    print(f"Deposit was successful, your new balance is: ${self.balance(self.acct_num):,.2f}")
                elif (value == 2):
                    print("Making a withdrawal")
                    withdraw = self.getWithdrawal()
                    if self.withdraw(self.acct_num, withdraw) == True:
                        print(f"Withdrawal was sucessful, your new balance is ${self.balance(self.acct_num):,.2f}")
                    else:
                        print(f"Not enough enough funds, your current balance is ${self.balance(self.acct_num):,.2f}")
                elif (value == 3):
                    print(f"Your current balance is: ${self.balance(self.acct_num):,.2f}")
                elif (value == 4):
                    print(f"Goodbye, {self.user}!")
                    break
                else:
                    print("Choose a number from 1-3")
            except ValueError:
                print("Invalid input")
                continue

    def _createAccount(self):
        acct_num = self._accountGenerator()
        
        user = self.getUsername()
        if not user:
            return
        amount = self.getDeposit()
        if not amount:
            return
        
        self.addAccount(acct_num, user, amount)
        print(f"\nWelcome to Py Bank, {user}! Your account number is {acct_num}")
        print(f"Thank you for your initial deposit of ${amount:,.2f}")
        print(f"\nHIDDEN (show accounts as they are created) : {self._accounts}")
    
    def _accessAccount(self):
        self.acct_num = self.getAccountNumber()
        if not self.acct_num:
            return
        self.user = self.getUsername()
        if not self.user:
            return
        
        #If account is authenticated, diplay account menu
        authentication = self._authenticateAccount(self.user, self.acct_num)
        if authentication == True:
            self._displayAcctMenu()
        else:
            print("Account Number or Username are incorrect")
    
    def getUsername(self):
        user_name = input("Enter user name or press enter to 'cancel': ").strip().lower()
        if not user_name:
            print("Cancelled Request")
            return None
        else:
            return user_name
        
    def getAccountNumber(self):
        acct_num = input("Enter 5 digit account number: ")
        if not acct_num.isnumeric():
            print("Invalid account number.")
            return None
        elif len(acct_num) != 5:
            print("Account number must be 5 digits")
            return None
        else:
            return int(acct_num) 
 
    def getDeposit(self):
        value = input("Enter the amount of deposit: ")
        amount = value.replace(',', '') #strip possible commas 
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount, deposit must be greater than 0")
                return None
        except ValueError:
            print("Invalid Input")
            return None
        return amount
    
    def getWithdrawal(self):
        value = input("Enter the amount of withdrawal: ")
        amount = value.replace(',', '') #strip possible commas 
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount, deposit must be greater than 0")
                return None
        except ValueError:
            print("Invalid Input")
            return None
        return amount

def main():
    console = Interface()
    console.displayMainMenu()
    

if __name__ == '__main__':
    main()