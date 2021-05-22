m=int(input("Enter marks in maths"))
p=int(input("Enter marks in physics"))
c=int(input("Enter marks in chemistry"))
if (m>=65 and p>=55 and c>=50 and m+p+c>=180 and m+p>=140 and m+c>=140):
	print("Eligible for course")
else:
	print("not eligible")

