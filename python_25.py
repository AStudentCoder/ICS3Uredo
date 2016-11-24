#Your task in this exercise is to define a function make_ing_form() which given a verb
#in infinitive form returns its present participle form. Test your function
#with words such as lie, see, move and hug. However, you must not expect such simple
#rules to work for all cases.

verb = input("Please input a verb in the infinitive form. This verb will be converted to present participle tense: ") 
#This is where the user shall input the infinitive word such as lie, see, move, hug
import re
#This will allow for the use of re.sub
consonant = "bcdfghjklmnpqrstvwxyz"
#This will be used later on during one of the elif statements
vowel = "aeiou"
#This will be used later on during one of the elif statements
def make_ing_form(verb):
    if verb == 'be' or verb == 'see' or verb == 'flee' or verb == 'knee':
        #This if statement is used for cases that do are exceptions to the rule, for words ending with e
       return verb + "ing"
    else:
       if verb.endswith("ie"):
           #if the verb ends with ie, then remove ie and add y and ing
          new_verb = re.sub('ie$', 'y', verb)
          return new_verb + "ing"
       elif verb.endswith("e"):
           #elif the verb ends with e, then remove the e and add ing
          new_verb = re.sub('e$', 'ing', verb)
          return new_verb
       elif verb[-2] in vowel and verb[-1] in consonant and verb[-3] in consonant and verb[-1] != 'w':
           #elif the verb ends with consonant, vowel, consonant
          new_verb = verb + verb[-1] + 'ing'
          return new_verb
       else:
           #if the verb does not fit in any of the other categories
          return verb + "ing"
  

print (make_ing_form(verb))
