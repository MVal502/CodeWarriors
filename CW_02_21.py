#https://www.codewars.com/kata/56786a687e9a88d1cf00005d
 
def validate_word(word):
    word = word.lower()
    return len(set(word.count(c) for c in word)) == 1