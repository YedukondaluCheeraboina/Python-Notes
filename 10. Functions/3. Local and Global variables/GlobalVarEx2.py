#Program for demonstrating the Need of Global Variables
#GlobalVarEx2.py
def learnAI():
	sub1="AI" # Here sub1 is Called Local Variable
	print("\tTo develop '{}' Based Applications, we Use '{}' Programming Lang".format(sub1,lang))
def learnML():
	sub2="ML"  # Here sub2 is Called Local Variable
	print("\tTo develop '{}' Based Applications, we Use '{}' Programming Lang".format(sub2,lang))

#Main Program
#learnAI()----We can't access  global Variable 'lang' in learnAI() Function bcoz It is defined after this function
lang="PYTHON" # Here lang is called Global Variable
learnML()