class Customer:
    '''This class developed by shubham and describes the bank operations'''

    bankname = 'State Bank Of India'

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("after deposit balance is : ", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("after withdraw balance is : ", self.balance)
        else:
            print("insufficient fund cannot perform this operations")
print('welcome to ', Customer.bankname)
name = input("enter your name : ")
customer = Customer(name)
while True:
    print('d-deposit\nw-withdraw\ne- exit')
    option = input('select your option : ')

    if option.lower() == 'd':
        amount = float(input('enter deposit amount : '))
        customer.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('enter withdraw amount : '))
        customer.withdraw(amount)
    elif option.lower() == 'e':
        print("Thanks for banking")
        break
    else:
        print('your option is invalid please select valid option')




