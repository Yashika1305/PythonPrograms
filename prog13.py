temp=float(input("Enter Temperature in Celsius"))
if temp<0:
 print("Freezing weather")
elif temp>0 and temp<=10:
 print("Very Cold weather") 
elif temp>10 and temp<=20:
 print("Cold weather")
elif temp>20 and temp<=30:
 print("Normal in Temp")
elif temp>30 and temp<=40:
 print("Its Hot")
else:
	print("Its Very Hot")
