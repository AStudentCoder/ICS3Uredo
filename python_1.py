'''Find the largest of two numbers'''
'''Prompt user to enter two numbers.'''
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
'''define function'''
def mx(firstNumber, secondNumber):
   if firstNumber > secondNumber:
      print (str(firstNumber) + " is the greater number")
   elif firstNumber == secondNumber:
      print ("%s and %s are equal" %(firstNumber, secondNumber))
   else:
      print (str(secondNumber) + " is the greater number")
      '''print out the largest'''
mx(firstNumber, secondNumber)

