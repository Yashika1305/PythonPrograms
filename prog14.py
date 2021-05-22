s1=int(input("Enter side 1"))
s2=int(input("Enter side 2"))
s3=int(input("Enter side 3"))
if s1==s2==s3:
	print("Equilatoral Triangle")
if s1!=s2 and s2!=s3 and s1!=s3:
	print("Scalene Triangle")
else:
	print("Isosceles Triangle")