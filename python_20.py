'''Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.'''

#Tells user to input the saying 'merry christmas and happy new year'
card = input("This is a simple English-Swedish translator for christmas cards. Please type in the phrase 'Merry christmas and happy new year'. Punctuation at the end may be added: ").split()
#lowers all items in card to lowercase
card = [item.lower() for item in card]
#this is the dictionary which translates words from english to swedish
lexicon = {"merry":"God", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år", "year.":"år.", "year!":"år!"}
#function is defined
def translate(card):
  #this empty list will be used later on, to print the translation 
  empty_list = []
  #this goes through each item in card
  for item in card:
     #if the item is in the lexicon
     if item in lexicon:
        #add the lexicons value to the empty list
        empty_list.append(lexicon[item])
     else:
        #otherwise just add the item
        empty_list.append(item)
        #prints that some of the words are not in the lexicon
        print ("Some/All of those words were not in our English-Swedish translator!")
  #combines the empty list into a string
  print (" ".join(empty_list))       
#calls the string
translate(card)


