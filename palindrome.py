num=int(input("Enter the number"))
temp=num
rev=0
while num>0:
	r=num%10
	rev=rev*10+r
	num=num//10
print("reverse is%d"%rev)
if temp==rev:
	print("It is palindrome")
else:
	print("It is not palindrome")