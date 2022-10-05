#python script for pythagorean theorem
import math
def cmiss():
	a = float(input("a = "))
	b = float(input("b = "))
	return(math.sqrt(a*a+b*b))
def amiss():
	b = float(input("b = "))
	c = float(input("c = "))
	return(math.sqrt(c*c-b*b))

def bmiss():
	a = float(input("a = "))
	c = float(input("c = "))
	return(math.sqrt(c*c-a*a))

def choice():
	global miss
	miss = input("Which side is missing?")
	if(miss=="a"):
		return(miss," = ",amiss())
	if(miss=="b"):
		return(miss," = ",bmiss())
	if(miss=="c"):
		return(miss," = ",cmiss())
	else:
		print("That's not a standard designator!")
		return(choice())
print("Pythagorean calculator")
print(choice())
