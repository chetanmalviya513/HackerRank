"""def is_leap(year):
	leap = False
	


#year = int(input("Enter year : "))

if (year % 400 ==0) and (year % 100 == 0) :
	leap = True :

	#print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
	leap = True
	#print("{0} is a leap year".format(year))

else:
	leap = False
	#print("{0} is a not leap year".format(year))
	return leap

year = int(input())
print(is_leap(year))
"""
#print(is_leap(year))

def is_leap(year) :
	leap = False

	if year % 400 == 0 and year % 100 == 0 :
		leap = True

	elif year % 4 == 0 and year % 100 != 0 :
		leap = True
		
	return is_leap

year = int(input())
print(is_leap(year))
