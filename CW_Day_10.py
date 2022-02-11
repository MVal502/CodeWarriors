'''
Description: Write a function that checks if a given string (case insensitive) is a palindrome.

Link: https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
'''

def is_palindrome(s):
  palindrome = False;
  s = list(s.lower());
  reverse = s[::-1];
  if s == reverse:
    palindrome = True;
#  print(s);
#  print(reverse);
  return palindrome

'''
Test Cases:

@test.describe('sample tests')

def sample_tests():

    test.assert_equals(is_palindrome('a'), True)

    test.assert_equals(is_palindrome('aba'), True)

    test.assert_equals(is_palindrome('Abba'), True)

    test.assert_equals(is_palindrome('malam'), True)

    test.assert_equals(is_palindrome('walter'), False)

    test.assert_equals(is_palindrome('kodok'), True)

    test.assert_equals(is_palindrome('Kasue'), False) 

'''