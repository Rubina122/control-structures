l=[10,20,30]
x=l[1:2]
print(x)

a=int(input())
l=[1,2,a]
for a in range(len(l)):
    if a==l:
        print(a)
    else:
        print('false')

def a(n)
n=input().isalnum
l=[1,2,3]
x=l
if a in l:
    return n
a(1)

def h(a):
    l = [10, 20.02,True,4,'a',100]
    b=str(l)
    if a in b:
        return True
    return False
a=input('Enter a string: ')
print(h(a))

x1=[1,2,3]
x2=[3,2,1]
x1.extend(x2)
print(x1)
print(x2)x1.pop
a



# h(0)



a=[1,2,3]
b=a
print(b)

a=['a','b','a','b']
b=a.count('a')
c=a.count('b')
print('a',b)
print('b',c)
b=a.list()
print(b)
b=a[0]
print(b)

a=[1,2,3]
a.append(5)
print(a)
a.insert(1,5)
print(a)
a.remove(5)
print(a)
a.remove(5)
print(a)
a.pop()
print(a)
a.sort()
print(a)
b=a.index(1)
print(b)
a.extend([1,2,3])
print(a)
a.clear()
print(a)
del a
print(a)

a=[4,5,2,3]
min_val=min(a)
min_ind=a.index(min_val)
print(min_val)
print(min_ind)
for i in range (len(a)):
    min_val=min(a[i:])
    min_index=a.index(min_val)
    a[i],a[min_index]=a[min_index],a[i]
    print(a)


