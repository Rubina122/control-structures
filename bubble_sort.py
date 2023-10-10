# a=[4,5,1,2,3]
# b=(a[::-1])
# print(b)


# a=[2,4,3,1]
# print(a)
# for i in range(len(a)):     #(i=0,1,2,3)
#     for j in range(len(a)-i-1):  #(4-0-1)=(3)=(0,1,2)
#         if a[j] >a[j + 1]:
#             a[j],a[j + 1]=a[j+1],a[j]
#             print(a)

a=[2,4,3,1]
for i in range(len(a)):  #[i=0,1,2,3]
    if a[i]>a[i+1]:
        a[i],a[i + 1] = a[i + 1], a[i]
        print(i,a)









a=[3,1,2]
a.sort()
print(a)




