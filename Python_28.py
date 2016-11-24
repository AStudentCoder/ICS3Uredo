#Write a function find_longest_word() that takes a list of words and returns the length
#of the longest one. Use only higher order functions.
 
lst = [len(x) for x in input("Please input a list of words with spaces between each word. It will return the length of the longest word: ").split()]
#Turns all the words into integers representing their len() values
from functools import reduce
#Imports the reduce function
def max_in_list(lst):
   return reduce(max, lst)
print (max_in_list(lst), "is the length of the longest word.")
