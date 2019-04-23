#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-04-22
Purpose: tests for palindrome
"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

palindrome = './palindrome.py'
palindrome2 = './palindrome.py foo'

def test_exists_palindrome():
    #test that palindrome.py exists
    assert os.path.exists(palindrome)

def test_usage():
    #test that tests for no arguments for usage
    rv, out = getstatusoutput('{}'.format(palindrome2)) 
    assert re.match('usage', out, re.IGNORECASE)

def answer(text):
    text_ns = text.replace(" ", "")
    if str(text_ns) != str(text_ns)[::-1]:
        text_mp = str(text_ns) + str(text_ns)[::-1]
        return('"{}" is not a palindrome, but {} is\n'.format(text, text_mp))
    else:
        return('"{}" is a palindrome\n'.format(text))

def test_yes_palindrome():
    assert answer('racecar') == '"racecar" is a palindrome\n'

def test_no_palindrome():
    assert answer('foo bar') == '"foo bar" is not a palindrome, but foobarraboof is\n'
