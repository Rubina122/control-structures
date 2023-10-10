# a=input("Enter the Name : ")
# b=(a[::-1])
# if a==b:
#     print('The Given String is Pallindrome')
# else:
#     print('The Given String is not Pallindrome')
#
# # for i in range(1,10):
# #     if(i%2==0):
# #         print(i)

# a='malayalam'
# first=0
# last=len(a)-1
# print(a[first])
# print(a[last])


# a=input('Enter the string : ').lower()
# first=0
# last=len(a)-1  # ------- [0,len(string)-1]---indexing---ex:Mam [0,1,2]
# while first!=last:
#     if (a[first] == a[last]):  #(ex: mam first=m and last =m  true goes for next iteration) else (if false stops the iterarion)
#         first = first + 1  # first=0+1=1
#         last = last - 1  # last=4-1=3
#         print('Given string is pallindrome')
#         break
#     else:
#         print('Gven String is not pallindrome')
#         break

a=input('Enter the string : ').lower()
first=0
last=len(a)-1  # ------- [0,len(string)-1]---indexing---ex:Mam [0,1,2]
while first!=last:
    if a[first] == a[last]:  #(ex: mam first=m and last =m  true goes for next iteration) else (if false stops the iterarion)
        first = first + 1  # first=0+1=1
        last = last - 1  # last=4-1=3
    else:
        print('Gven String is not pallindrome')
        break
else:
    print('Given string is pallindrome ')


# a=input('enter the string : ')
# i=0
# length=len(a)
# if len(a)%2==0:
#     length=len(a)+1
# for i in range(length):
#     if a[i]!=a[-1-i]:
#         print('Given string is not a pallindrome')
#         break
# else:
#     print('Given string is a pllindrome')

