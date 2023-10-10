x={"name":"john","age":"30"}
a=x.keys()
print(a)
b=x.values()
print(b)
c=x.items()
print(c)
x.update({"name":"k"})
print(x)

x=['a','c','b','a','d','a']
count={}
for ele in x:
        count[ele] = count.get(ele,0) + 1
y=dict(x,5)
print(y)


x=['a','c','b','a','d','a']
y=x.count('a')
z=x.count('b')
print('a',y)
print('b',z)

x=[1,2,3,1]
count={}
for ele in x:
    count[ele]=count.get(ele,0)+1
    print(count)
y={"name":"John",'age':'30'}
a=y.keys()
print(a)
b=y.values()
print(b)
c=y.items()
print(c)
y.update({"sal":"k"})
print(y)
x=y

x=[1,2,2]

a = int(input('Enter the String : '))   --- Value error
b = int(input('Enter the String: '))
c = a + b
print(c)



a = input('Enter the String : ')    #-  Type error
b = input('Enter the String: ')
c = a * b
print(c)