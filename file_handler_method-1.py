def s(n):
    try:
        while True:
            opp = input('Enter The Mode: write,read,append,r+,w+: ').lower()
            if opp == 'write':
                file = open(n, 'w')
                file.write(input('Enter the content:'''))
                file.close()
            elif opp == 'read':
                file = open(n, 'r')
                c = file.read()
                print(c)
                file.close()
            elif opp == 'append':
                file = open(n, 'a')
                file.write('\n')
                file.write(input('Enter the content:'''))
                file.close()
            elif opp=='r+':
                file=open(n,'r+')
                c=file.read()
                print(c)
                file.write('\n')
                file.write(input('enter the content:'''))
                file.seek(0)
                c = file.read()
                print(c)
                file.close()
            elif opp=='w+':
                file=open(n,'w+')
                file.write(input('Enter the content:'''))
                file.seek(0)
                c=file.read()
                print(c)
                file.close()
            else:
                print('Na')
                break
    except FileNotFoundError:
        print('Error To Be Handled')

n=input('Enter the Filepath: ' )
print(s(n))


