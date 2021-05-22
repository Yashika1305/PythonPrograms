def ma():
	print("outer")
	def mb():
		print("inner")
	return mb()
t=ma #function aliasing
t()