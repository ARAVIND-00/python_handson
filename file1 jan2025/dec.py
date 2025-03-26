# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self._balance=balance
#     @property
#     def balance(self):
#         return self._balance
    
#     @balance.setter
#     def balance(self,amount):
#         if amount<0:
#             raise ValueError("Balance must be greater than or equal to 0")
#             self._balance=amount
            
#         else:
#            return print('Enter number greater than 0')
#     @property    
#     def interest(self):

#         return self._balance*0.05


# c=BankAccount('aravind',1000)
# print(c.interest)
# d=c.balance=1500
# print(d)        

def log_function_call(func):
    def wrapper(*args, **kwargs):
        # Print the name of the function
        print(f"Calling function: {func.__name__}")
        
        # Print the arguments passed to the function
        print(f"Arguments: {args}, {kwargs}")
        
        # Call the original function and get its return value
        result = func(*args, **kwargs)
        
        # Print the return value
        print(f"Return value: {result}")
        
        return result  # Return the result of the original function
    return wrapper

# Test the decorator
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Example usage
print(add(3, 5))  # Logs details about the call
greet("Alice", greeting="Hi")  # Logs details about the call
