file=open('f1.txt','w')
txt=file.write('hello')
file.close()

india=open('team.txt','r')
for i in india:
    print(i)
# print("\n[h:)]")
# input()

n=int(input('enter the input : '))
f=open('u203.txt','w')
for i in range(0,n+1):
    f.write(str(i))
    f.write('\n')
f.close()

def s():
        while True:
            opp=input('Enter The File_Handler:Write,Read,append : ')
            if opp=='write':
                 file=open('g.txt','w')
                 file.write('Apple\n')
                 file.write('Banana')
            elif opp == 'read':
                file = open('g.txt', 'r')
                c=file.read()
                print(c)
            elif opp == 'append':
                file = open('g.txt', 'a')
                file.write('\n')
                file.write('Grape')
            else:
                print('Na')
                break


s()











