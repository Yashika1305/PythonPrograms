a=int(input("Enter number:(1-3)"))
if a==1:
  r=int(input("Enter the radius of circle"))
  area=3.14*r*r
  print(area)        
elif a==2:
  l=int(input("Input length of the rectangle:"))
  w=int(input("Input width of the rectangle:"))
  area=l*w 
  print(area)
elif a==3:
  b=int(input("Input base of the triangle:"))
  h=int(input("Input height of the triangle:"))
  area=.5*b*h;
  print(area)
else:
  print("Invalid area")
                  