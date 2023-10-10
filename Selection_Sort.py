a=[4,0,2,1,3]
for i in range(len(a)):
    min_value=min(a[i:])
    min_val_index=a.index(min_value)
    a[i],a[min_val_index]=a[min_val_index],a[i]
    print(a)