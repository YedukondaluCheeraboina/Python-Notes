#Program for demonstrating the Need of Global Variables
#GlobalVarEx1.py
def learnAI():
	sub1="AI" # Here sub1 is Called Local Variable
	print("\tTo develop '{}' Based Applications, we Use '{}' Programming Lang".format(sub1,lang))
def learnML():
	sub2="ML"  # Here sub2 is Called Local Variable
	print("\tTo develop '{}' Based Applications, we Use '{}' Programming Lang".format(sub2,lang))


#Main Program
lang="PYTHON" # Here lang is called Global Variable
learnAI()
learnML()