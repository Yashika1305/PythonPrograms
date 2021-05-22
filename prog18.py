cp=int(input("Enter the cost price"))
sp=int(input("Enter the selling price"))
if sp>cp:
	profit=sp-cp
	print("The Profit amount is %d"%profit)
else:
	loss=cp-sp
	print("The Loss amount is %d"%loss)