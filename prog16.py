ch=input("Enter the Character")
if ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
	print("alpbhabet")
elif (ch>='0' and ch<='9'):
	print("Digit")
else:
	print("Special Character")