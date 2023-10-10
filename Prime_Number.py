a=int(input('Enter the number : '))
if a>1:
    for i in range(2,a): #(ex: a=6 range(2,6)=(2,3,4,5)
        if(a%i)==0:  #(6%(2,3,4,5)==0 is divisble by 2 and 4 it is not prime)
            print(a,'is not a prime number')
            break  # To treminate the loop or control the loop
        else:
            print(a,'is a prime number')

