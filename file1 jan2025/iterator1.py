# my_list=[10, 20, 30, 40, 50]

# iterator=iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# with open("empty.txt") as file:
#     iter=iter(file)

#     print(next(iter))

def fibonacci_sqe():

    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

num=fibonacci_sqe()

for i in range(5,10):
    print(next(num))



# func to count number of given word
# def print_even(test_string):
#     for i in test_string:
#         if i == "geeks":
#             yield i


# # initializing string
# test_string = " There are many geeks around you, \
#               geeks are known for teaching other geeks"

# # count numbers of geeks used in string
# count = 0
# print("The number of geeks in string is : ", end="")
# test_string = test_string.split()

# for j in print_even(test_string):
    
#     count = count + 1

# print(count)
