
# class Test:

# 	# Constructor
# 	def __init__(self, limit):
# 		self.limit = limit

# 	# Creates iterator object
# 	# Called when iteration is initialized
# 	def __iter__(self):
# 		self.x = 10
# 		return self

# 	# To move to next element. In Python 3,
# 	# we should replace next with __next__
# 	def __next__(self):

# 		# Store current value ofx
# 		x = self.x

# 		# Stop iteration if limit is reached
# 		if x > self.limit:
# 			raise StopIteration

# 		# Else increment and return old value
# 		self.x = x + 1;
# 		return x

# # Prints numbers from 10 to 15
# for i in Test(15):
# 	print(i)

# # Prints nothing
# for i in Test(5):
# 	print(i)

# t=Test(12)
# print(t.__iter__())

# Python code demonstrating
# basic use of iter()
listA = ['a','e','i','o','u']

iter_listA = iter(listA)

try:
    print( next(iter_listA)) 
    print( next(iter_listA)) 
    print( next(iter_listA)) 
    print( next(iter_listA)) 
    print( next(iter_listA))
    print( next(iter_listA)) #StopIteration error
except:
    pass