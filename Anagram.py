# a=input('Enter thr String: ')
# b=input('Enter the String: ')
# if len(a)!=len(b):
#     print('len of String is not same')
# elif sorted(a)==sorted(b):
#     print('Anagram')
# else:
#     print('Not Anagram')

# a=input('Enter the String: ')
# b=input('Enter the String: ')
# if len(a)!=len(b):
#     print('Given String Is Not a Anagram')
# if len(a)==len(b):
#     a,b=a.lower(),b.lower()
#     for c in a:
#         if c in b:
#             print('Given String is Anagram')
#             break
#         else:
#             print('Given String is Not a Anagram')
#             break

# a='car'
# b='rac'
# if len(a)==len(b):


# a=['car','bar']
# for i in range(len(a)):  #(0=car
#     for j in range(len(a)):  #(0,1)=(car,bar)
#         if a[j]>a[i]:
#             #a[1]>a[1]
#             a[i],a[j]=a[j],a[i]
# print(a)

# a=['car','bar']
# b=len(a)
# print(b)

# a=input('Enter the String : ')
# b=input('Enter the String: ')
# c=list(a)
# d=list(b)
# for i in range(len(c)):  #(0=car
#     for j in range(len(d)):  #(0,1)=(car,bar)
#         if d[j]>c[i]:
#             temp=c[i]
#             c[i]=d[j]
#             d[j]=temp
#             print('Anagram')
#             break
#     else:
#         print('not Anagram')
#         break

# a='car'
# b=list(a)
# print(b)

def anagram(c,d):  # c='car d='rac'
    a = list(c)    # a=['c','a','r']
    b = list(d)    # b=['r','a','c']
    for i in range(len(a)):  # (0,1,2) i=0 ie. c
        for j in range(len(b)):  # (0,1,2)=('r','a','c')
            if b[j] > a[i]:
                a[i], b[j] = b[j], a[i]
                return 'Anagram'
            return 'Not Anagram'
c=input('Enter the string : ')
d=input('Enter the String : ')
print(anagram(c,d))
