from abc import ABC,abstractmethod

from Customer import  customer
class BankBase(ABC):


    @abstractmethod
    def create_account(self,name,phone,deposit=0):
        pass
    @abstractmethod
    def create_bank(self,name,branch):
        pass

class Bank(BankBase):
    __account_serial = 1
    def __init__(self,name,branch):
        self.create_bank(name,branch)
        self.customers=[]



    def create_bank(self, name, branch):
        print('creating a bank')
        self.name=name
        self.branch=branch

    def create_account(self,name,phone,deposit=0):
        acc_number=Bank.__account_serial
        Bank.__account_serial+=1
        cust=customer.create_customer(name,phone,acc_number,deposit)
        self.customers.append(cust)
        return cust


    def get_customers(self):
        for cust in self.customers:
            print(cust.name)

    def all_customer_balance(self):
        total=0
        for cust in self.customers:
            total=total+cust.get_balance()
        print(total)










