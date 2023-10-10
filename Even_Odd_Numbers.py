# To Print Even Numbers ----
'''
for i in range(2,10,2):
    print(i)
'''

# Factorial Series

# a=int(input('enter the number : '))
# fact=1
# for i in range(1,a+1):  #(for example: a=3 range(1,3+1)=range(1,4)=(1,2,3)
#     fact=fact*i #(f=1*(1*2*3)
#     print(fact)

# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,9):
#     c=a+b
#     print(c)


def recur(n):
    if n==1:
        return 1
    return n * recur(n-1)
         # (f=1*(1*2*3)
n=int(input())
print(recur(n))




# recur(5)
