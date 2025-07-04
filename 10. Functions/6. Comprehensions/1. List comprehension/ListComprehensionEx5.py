#Program for Reading Number of Values dynamically from KBD and display by using List Comprehension
#ListComprehensionEx5.py
lst=[ float(val)  for val in input("Enter List of Values Separated by Comma:\n").split(",")  if float(val) > 0 ]
print("Given List of Values=",lst)