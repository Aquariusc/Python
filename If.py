#!/E/Lucifer/Python/Code
#!Filename:If.py
number=23
guess=int (input("Enter an integer:"))  #python3里raw_input()变成了input()

if guess==number:
    print('Congratulations , you guessed it.')
    print("but you do not win any prizes!")
elif guess<number:
    print('No , it is a little higher than that')
else:
    print('No , it is a little lower than that')

print('Done')
