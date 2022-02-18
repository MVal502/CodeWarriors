'''
Description: You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

	#Examples:

	Kata.getMiddle("test") should return "es"

	Kata.getMiddle("testing") should return "t"

	Kata.getMiddle("middle") should return "dd"

	Kata.getMiddle("A") should return "A"

Link: 
''' 

def get_middle(s):
    #your code here
    return s[(len(s)-1)//2:(len(s)+2)//2]

'''
Test Cases: 
test.assert_equals(get_middle("test"),"es")
test.assert_equals(get_middle("testing"),"t")
test.assert_equals(get_middle("middle"),"dd")
test.assert_equals(get_middle("A"),"A")
test.assert_equals(get_middle("of"),"of")

'''