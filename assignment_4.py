def normal(func, *args):
	print(func(*args))

normal(lambda *args: sum(args), 0,1,1,2,3)