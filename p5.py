a=int(input("Enter the number "))
if a>=1500 and a<=2700:
	if(a%5==0 and a%7==0):
		print("correct no")
	else:
		print("not div")
else:
	print("enter num in range")