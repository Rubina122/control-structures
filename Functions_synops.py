def add():
    a=int(input('enter the number : '))
    b = int(input('enter the number : '))
    c=a+b
    print(c)

def sub():
    a=int(input('enter the number : '))
    b = int(input('enter the number : '))
    c=a-b
    print(c)

def div():
    a=int(input('enter the number : '))
    b = int(input('enter the number : '))
    c=a/b
    print(c)

def mul():
    a=int(input('enter the number : '))
    b = int(input('enter the number : '))
    c=a*b
    print(c)

add()
# sub()
# div()
# mul()


def ball():
    while True:
        oper=input('Enter tbe Operation: ')
        if oper == 'add':
            a = int(input('enter the number:'))
            b = int(input('enter the number:'))
            print(a + b)
        elif oper=='sub':
            a = int(input('enter the number:'))
            b = int(input('enter the number:'))
            print(a-b)
        elif oper=='mul':
            a = int(input('enter the number:'))
            b = int(input('enter the number:'))
            print(a*b)
        elif oper=='div':
            a = int(input('enter the number:'))
            b = int(input('enter the number:'))
            print(a/b)
            break
        else:
            print('Invalid operation')











ball()


