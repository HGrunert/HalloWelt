

#ist 2 < 3  ? true
#ist 4 < 4  ? false
#ist 3 <= 3 ? true
#ist 3 >= 3 ? true
#ist 3 >= 4 ? false
#ist 3 == 3 ? true
#ist 4 == 3 ? false

#ist 4 != 3 ? true
#ist 3 != 3 ? false

teststring = "abcdefghijklm"

durchlauf = 1
abbruch = len(teststring)
while durchlauf <= abbruch :
      cnr = durchlauf - 1
      charx = teststring[cnr]
      print("hallo " + durchlauf.__str__() + " " + charx )
      durchlauf += 1

print("dies kommt nach der schleife")




