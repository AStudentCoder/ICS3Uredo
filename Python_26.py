#Using the higher order function reduce(), write a function max_in_list() that takes a
#list of numbers and returns the largest one. Then ask yourself: why define and call a
#new function, when I can just as well call the reduce() function directly?

lst = [int(x) for x in input("Please input a list of words with spaces between them: ").split()]
from functools import reduce #imports the higher order function reduce
def max_in_list(lst):
    return reduce(max, lst)
print (max_in_list(lst))    
