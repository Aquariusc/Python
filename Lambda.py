#!/E/Lucifer/Python/Code
#!Filename:Lambda.py

def make_repeater(n):
    return lambda s:s*n

twice=make_repeater(2)

print(twice('world'))
print(twice(5))
