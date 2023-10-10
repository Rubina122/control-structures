
# a=int(input())
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
#     print(fact)
#
# Recursive -
# Calling a function with a another function within itself

# def rec(a,b):
#     for i in range(0, 1):
#      print(a+b)
#      rec(a, b)
# rec(10,20)



# def f(a):
#     print('I')
#     if a!=10:
#         f(a+1)
# f(1)


# def v(i):
#
#     print(i)
#     if i<5:
#         v(i + 1)
#
# #
# v(1)

# def u(i):
#     print(i)
#     if i==1:
#         return i
#     else:
#         u(i-1)
#
#
#
# u(5)




# def a(i):
#     print(i)
#     if i<5:
#         a(i+1)
#
# a(6)


# def s(i):
#     if i<5:
#         s(i+1)
#         return
#     else:
#         print(i + 1)
#
#
#
# s(1)


# def e(n):

def recur(n):
    if n==1:
        return 1
    return n * recur(n-1)
         # (f=1*(1*2*3)
n=int(input())
print(recur(n))


