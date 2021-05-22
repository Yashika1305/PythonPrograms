x=int(input("please enter the number"))
y=int(input("please enter the number"))
if x>0 and y>0:
	print("First Quadrant")
elif x>0 and y<0:
	print("Second Quadrant")
elif x<0 and y>0:
	print("Third Quadrant")
else:
	print("Fourth Quadrant")
