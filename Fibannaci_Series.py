''' 0,1,1,2,3
a=0
b=1
c=a+b=0+1=1
d=b+c=1+1=2
e=c+d=3
f=d+e
a=0
b=1

'''
# 0,1,1,2,3,5,8,12,21,33
# n=int(input('Enter the Number:'))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n):
#     c=a+b
#     print(c)
#     a=b           #0+1=1
#     b = c          #a+b=c
                     #a+b=c
                       #a+b=c


# def add(a,b):
#     print(f"{a}+{b}= " + str(a+b))
# def fib(n):
#     a =input()
#     b =input()
#     print(a)
#     print(b)
#     else:
#
#     for i in range(2, n):
#         add(a,b)
#         print(c)
#         a = b  # 0+1=1
#         b = c
# fib(5)

# def add(a,b):
#     print(f"{a}+{b}= " + str(a+b))
# def fib(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2, n):
#         c = a + b
#         print(c)
#         a = b  # 0+1=1
#         b = c
#
# fib(5)





'''
0,1,1,2,3
a,b=c
  a=b=c
    a=b=c
'''
'''
a=input('Enter the number : ')
print(a)
'''



def fib(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input('enter the number: '))
for i in range(1,n+1):  #(1,2)
    print(fib(i))


