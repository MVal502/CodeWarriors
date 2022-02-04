'''
Code Warriors Day 4

Link: https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/python

 

Description: When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

 '''

 #Function

def switch_it_up(number: int) -> str:

    #your code here

    dict_num = {

        0: 'Zero',

        1: 'One',

        2: 'Two',

        3: 'Three',

        4: 'Four',

        5: 'Five',

        6: 'Six',

        7: 'Seven',

        8: 'Eight',

        9: 'Nine'

        }

    return dict_num.get(number)

 
'''
Test cases:

import codewars_test as test

from solution import switch_it_up

 

@test.describe("Fixed Tests")

def fixed_tests():

    @test.it('Basic Test Cases')

    def basic_test_cases():

        test.assert_equals(switch_it_up(0), "Zero")

        test.assert_equals(switch_it_up(9), "Nine")
'''