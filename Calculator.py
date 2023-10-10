def add(a,b):
    print(f"{a}+{b}= "+str(a+b))

def sub(a,b):
    print(f"{a}-{b}= "+str(a-b))

def calculator():
    opp = input('enter the operation: ')
    a=int(input('Enter the Number:'))
    b= int(input('Enter the Number:'))
    if opp=="add":
        add(a,b)
    elif opp=='sub':
        sub(a,b)
    else:
        print('invalid')

if __name__=="__main__":
    calculator()


