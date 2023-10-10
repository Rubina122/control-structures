import Bank

sbi=Bank.Bank("Sbi",'Bang')

cust1=sbi.create_account("Raj",12345,100)
print(cust1.acc_number)
print(cust1.get_balance())
cust1.deposit(500)
cust1.withdraw(100)
print(cust1.get_balance())

cust2=sbi.create_account("Raju",12345,5000)
print(cust2.acc_number)
print(cust2.get_balance())
cust2.deposit(500)
print(cust2.get_balance())

sbi.get_customers()
sbi.all_customer_balance()

print(cust1.get_balance())
print(cust2.get_balance())

cust2.transfer(cust1,500)
print(cust1.get_balance())
