
from random import randint


class Bank:
    
    def __init__(self):
        self._account_list = {}
        
        print 
        pass
    
    def accountGenerator():
        account_number = randint(10000,99999)
        return account_number


number = Bank.accountGenerator()
#print(number)

#welcome message
menu = """

1. Press 1 If you are an existing customer
2. Press 2 If you are a new customer
3. Terminate Session
"""

#diplay message   
def main():
    while True:
        choice = input(menu)
        try:
            value = int(choice)
            if value in range(1,3):
                print("spot on")
                break
            elif value == 3:
                print("Session Terminated")
                break
        except ValueError:
            print("Please, choose a number between 1-3")
            continue

if __name__ == '__main__':
    main()
