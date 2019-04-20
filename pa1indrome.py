#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-04-20
Purpose: palindromes
"""

import os
import sys


# --------------------------------------------------
def main():
    text = input("Enter a word or phrase to check if it is a palindrome:\n")
    text_ns = text.replace(" ", "")
 
    if str(text_ns) != str(text_ns)[::-1]:
        text_mp = str(text_ns) + str(text_ns)[::-1]
        print('"{}" is not a palindrome, but {} is\n'.format(text, text_mp))
    else:
        print('"{}" is a palindrome\n'.format(text))
    while True:
        play = input("Would you like to try another word or phrase? (y/n)\n")
        if play in ('y','Y','n','N'):
            break
        print('answer y or n')
    if play == 'y' or play == 'Y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print('Goodbye')
        
            
        
  

# --------------------------------------------------
main()
