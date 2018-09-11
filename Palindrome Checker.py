#This program takes a string as input, reverses it, and checks it
#against itself to determine if it is a palindrome.

from string import punctuation
from string import whitespace

print('This will check if what you input is a palindrome.')

def palindrome():
    print()
    s = input('Please provide a word, sentence, or number to check: ')
    s = s.translate({ord(k):"" for k in punctuation}).lower()
    s = s.translate({ord(k):"" for k in whitespace})
    print(s)
    print(s[::-1])

    if s == s[::-1]:
        print('Yes, this is a palindrome!')
    else:
        print('No, this is not a palindrome.')

def again():
    again = input('Try again? (y/n)').lower()
    while again == 'y':
        palindrome()
    else:
        quit

palindrome()
again()


