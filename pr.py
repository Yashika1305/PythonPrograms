class A:   #accessing property of class A in class B
           #without using inheritance(has-a relationship/composition)
	
	def ma(self):
		print("hello")
class B:
	def mb(self):
		a=A()
		a.ma()
		print("welcome")

b=B()
b.mb()
