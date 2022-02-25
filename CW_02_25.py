#https://www.codewars.com/kata/586ec0b8d098206cce001141/solutions/python

def inverse_slice(items, a, b):
    # Your code here.
    slice = items[a:b]
    for i in slice:
        if i in items:
            items.remove(i)
    return items
    