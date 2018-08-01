#For this assignment:
#1. In the main, create an account called JohnSmith with the following
#initializations:
#('John Smith', '19371554951', 20000)
#2. Deposit $1000
#3. Withdraw $4000
#4. Withdraw $3500
#5. Print the balance
#See PDF for more details.

class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = int(initial_amount)

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!\n")
        else:
            self._balance -= amount

    def get_balance(self):
        #self._balance = '${:,.2f}'.format(self._balance)
        return self._balance

    def dump(self):
        print ("Dump Account Info:", end =' ')
        s = '%s, %s, balance: %s\n' % (self._name, self._no, '${:,.2f}'.format(self._balance))
        print (s)
        
# Main
print ("Assignment 15 - written by Gabrielle Sudik & Matt Weisfeld\n")

#initialize customer account:
john = AccountP("John Smith", "19371554951", 20000)

#print(john)
#print(john._name)
#print(john._no)
#print(john._balance)

#deposit 1000:
john.deposit(1000)
#print(john._balance)

#withdraw 4000:
john.withdraw(4000)
#print(john._balance)

#withdraw 3500:
john.withdraw(3500)
#print(john._balance)

#call account info:
john.dump()

#print final balance:
print("Final balance: " + str('${:,.2f}'.format(john.get_balance())) + "\n")

#try to withdraw more than is in account:
john.withdraw(50000)

#reprint all account info:
john.dump()

#print final balance:
print("Final balance: " + str('${:,.2f}'.format(john.get_balance())) + "\n")

