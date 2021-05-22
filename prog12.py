r=int(input("enter the rollno"))
n=input("Enter the name")
p=int(input("Enter marks of Physics"))
c=int(input("Enter marks of Chemistry"))
ca=int(input("Enter marks of Computer Application"))
total=p+c+ca
per=total/300*100
if per>=90:
	print("First Division")
elif per<90 and per>=70:
	print("Second Division")
elif per<70 and per>=50:
	print("Third Division")
else:
	print("fail")	
