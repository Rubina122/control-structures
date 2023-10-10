
n=input('Choose the Number Please:''')
guess=0
trys=0
while guess!=n:
    trys=trys+1
    guess =input('Enter the Guessed Number:''')
    if (guess < n):
        print('Guess higher')
    elif (guess > n):
        print('Guess Lower')
    else:
        print(f'You Won in {trys} steps')

    if trys==5:
        print('game over')
        break





# #------- Number Guss --- using If And Nested if Function-----
# a=int(input("Enter the Input : "))
# b=int(input('enter the Guess Number :'))
# i=5
# if b < a:
#     print('guess higher')
# elif b > a:
#     print('Guess lower')
# elif b == a:
#     print('You won')
# else:
#     print('You lost')








