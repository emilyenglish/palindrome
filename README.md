# palindrome
This program checks if a word or phrase is a palindrome.
1.This program uses user input to determine if a word or phrase is a palindrome. 
2. It tells you if you have entered a palindrome or not. 
3. If you have not entered a palindrome, the program will turn what you entered into a palindrome. 
4. The program will ask if you would like to enter another word or phrase.

# Examples
This is what it should look like:
```
$ ./palindrom.py
Enter a word or phrase to check if it is a palindrome:
racecar
"racecar" is a palindrome

Would you like to try another word or phrase? (y/n)
y
Enter a word or phrase to check if it is a palindrome:
foo bar
"foo bar" is not a palindrome, but foobarraboof is

Would you like to try another word or phrase? (y/n)
n
Goodbye
```

This program does not accept any arguments. If arguments are attempted a usage statement is printed:
```
$ ./palindrome foo
Usage: Try again with no arguments
```

# Tests
There are four tests in the test.py to make sure the program is running correctly. They test that the program exists, usage statement works, and it outputs the correct response if the word or phrase entered is a palindrome or not. 
A passing test suite looks like this:
```
$ make test
python3 -m pytest -v test.py
===================== test session starts ======================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- /rsgrps/bh_class/conda/bin/python3
cachedir: .pytest_cache
rootdir: /home/u20/emilyenglish/palindrome, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
collected 4 items                                              

test.py::test_exists_palindrome PASSED                   [ 25%]
test.py::test_usage PASSED                               [ 50%]
test.py::test_yes_palindrome PASSED                      [ 75%]
test.py::test_no_palindrome PASSED                       [100%]

=================== 4 passed in 0.11 seconds ===================
```
# Author
Emily English emilyecenglish@gmail.com
