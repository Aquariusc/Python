#!/E/Lucifer/Python/Code
#!Filename:While.py
number=23
running=True

while running:
    guess=int(input("Enter an integer:"))

    if guess==number:
        print('Congratulation , you guessed it.')
        running=False #this causes the while loop to stop
    elif guess<number:
        print('No , it is a little higher')
    else:
        print('No , it is a little lower')
else:
    print('the while loop is over.')
print('done')
