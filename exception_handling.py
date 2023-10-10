a=int(input())   # Value Error ---- It is Programmed to allow only integer values otherwise it will throw value error
print(a)
a="Anantapur"
b=a.index('x')
print(b)

a=10              # Zero divison error  --- It will throw error because Number cannot divided by zero
b=0
c=a/b
print(c)

a='abc'            #Type error  --- It will Throw Type Error
a[1]='x'
print(a)

a=10                 #name error  -- If requried name is not present it will throw name error
del a
print(a)


a=10                   #syntax Error --- If there is error in program it will throw Synntax error
for i in a
    print(i)

x=(1,2,3)              #attribute Error -- Tuple Object will not support because it is immutable
x.remove(4)
print(x)


x={1,2}                  #Key Error ---- If the Value is Not Present in Given set it will give key error
y=x.remove(3)
print(y)



# while True:
#     opp = input('Enter The Operation:add,div,sub,mul: ')
#     try:
#         if opp == 'add':
#             a = int(input('Enter the String : '))
#             b = int(input('Enter the String: '))
#             c = a + b
#             print(c)
#     except:
#         print('Value Error')
#     try:
#         if opp == 'sub':
#             a = int(input('Enter the String : '))
#             b = int(input('Enter the String: '))
#             c = a - b
#             print(d)
#     except:
#         print('Name Error')
#     try:
#         if opp=='div':
#             a = int(input('Enter the String : '))
#             b = int(input('Enter the String: '))
#             c = a/b
#             print(c)
#     except:
#         print('Zero division error')
#     try:
#         if opp == 'mul':
#             a = input('Enter the String : ')
#             b = input('Enter the String: ')
#             c = a * b
#             print(c)
#     except:
#         print('Type error ')


# try:
#     a=.1
# except:
#     print

# try:
#     a = [2, 4, 3, 1]
#     for i in range(len(a)):  # [i=0,1,2,3]
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
#             print(i, a)
# except:
#     print('Index error')






def test():
    try:
        x = [1, 2]
        y = x[10]
    except IndexError:
        print('Index')
    try:
        x = [1, 2]
        y = x[10]
    except IndexError:
        print('Index')
test()












