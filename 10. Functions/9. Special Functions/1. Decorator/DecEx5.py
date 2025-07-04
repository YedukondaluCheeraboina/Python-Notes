#Program for  accepting a Line of Text and convert into Both Upper and Lower by using decorators
#DecEx5.py
def convertLower(conv):
	def  conversion():
		line,uc=conv()
		lc=line.lower()
		return line,uc,lc
	return conversion

def convertUpper(GL):
	def  conversion():
		line=GL()
		uc=line.upper()
		return line,uc
	return conversion

@convertLower
@convertUpper
def getline():
	return input("Enter Line of Text:")


#Main Program
line,uc,lc=getline()
print("---------------------------------------------------")
print("Given Line of Text=",line)
print("Upper Case=",uc)
print("Lower Case=",lc)
print("---------------------------------------------------")