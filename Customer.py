
class customer:

    __private_constructor=True

    def __init__(self,name,phone,acc_number,deposit):
        if customer.__private_constructor:
            raise PermissionError('Cant Create Instance for this object')

        if type(deposit) != int:
            raise ValueError('Deposit Should be type number')

        self.name=name
        self.phone=phone
        self.acc_number=acc_number
        self.__balance=deposit


    @classmethod
    def create_customer(cls, name, phone,acc_number, deposit):
        cls.__private_constructor=False
        cust=customer(name, phone,acc_number,deposit)
        cls.__private_constructor=True
        return cust
    def deposit(self,amount):
        if isinstance(amount,(int,float)):
            self.__balance+=amount
        else:
            print("Invalid amount")
    def get_balance(self):
        print(f"Balance for {self.name} is {self.__balance}")
        return self.__balance

    def withdraw(self,amount):
        if isinstance(amount,(int,float)):
           if self.__balance>amount:
               print(f"with drawing {amount}")
               self.__balance-=amount
               print(f"updated Balance {self.__balance}")
           else:
               print("Insufficient Funds")
        else:
            print('Invalid Amount')


    def transfer(self,to_account,amount):
        if self.__balance<amount:
            print('Insuffient funds')
        if isinstance(to_account,customer):
            print(f"Transferring {amount} from {self.name} with acc_no {self.acc_number} \n  to customer {to_account.name} with acc_number {to_account.acc_number}")
            self.__balance=self.__balance-amount
            to_account.deposit(amount)





