#Program for Reading Number of Values dynamically from KBD and display by using List Comprehension
#ListComprehensionEx4.py
print("Enter List of Values Separated by Comma:")
lst=[ float(val)  for val in input().split(",") ]
print("Given List of Values=",lst)