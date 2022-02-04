'''
CodeWarrirors Day 2

Link: https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/python

Description:

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.


'''

#function
def quarter_of(month): 
	return (month + 2) // 3

'''

/** Test Cases **/

import codewars_test as test

from solution import quarter_of

 

@test.describe("Fixed Tests")

def basic_tests():

    @test.it('Basic Test Cases')

    def basic_test_cases():

        test.assert_equals(quarter_of(3), 1)

        test.assert_equals(quarter_of(8), 3)

        test.assert_equals(quarter_of(11), 4)

 

@test.describe("Random Tests")

def random_tests():

   

    import math

    from random import randint

       

    def solution(month):

        return math.ceil(month / 3)

 

    for _ in range(100):

        num = randint(1, 12)

        @test.it(f"Testing for quarter_of({num})")

        def test_case():

             test.assert_equals(quarter_of(num), solution(num), "It should work for random inputs too")

'''




