def shop():
	price=None
	total=0
	menu()
	print("Welcome")
	item=eval(input("type 1-5 from menu"))
	if item==1:
		price=40
		dis()
	elif item==2:
		price=80
		dis()
	elif item==3:
		price=150
		dis()
	else:
		print("no discount")

def menu():
	print("select item")
	print("1. maggi")
	print("2. dal")
	print("3. rice")
	print("4. almond")
	print("5. chocolate")
def dis():
	price=price-0.05
	print(price)
	for i in price:
		total=total + price
	print(total)
shop()