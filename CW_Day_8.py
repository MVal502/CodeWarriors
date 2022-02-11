'''
Description: 

Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Link: 
https://www.codewars.com/kata/53dc23c68a0c93699800041d
''' 
def smash(words):
    return " ".join(words) if len(words) >= 1 else ""

'''
Test Cases: 
import codewars_test as test
from solution import smash

@test.describe("smash")
def _():
    @test.it("Should return empty string for empty array.")
    def _():
        test.assert_equals(smash([]), "")
        
    @test.it("One word example should return the word.")
    def _():
        test.assert_equals(smash(["hello"]), "hello")
        
    @test.it("Multiple words should be separated by spaces.")
    def _():
        test.assert_equals(smash(["hello", "world"]), "hello world")
        test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
        test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")
'''