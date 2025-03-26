
def counter(func):
    def wrapper(*args,**kwargs):
        wrapper.count +=1
        result=func(*args,**kwargs)
        print('ll',wrapper.count)
        return result
    wrapper.count = 0 
    return wrapper
    
@counter
def myfunction():
    print("func called")
myfunction()
myfunction()

print(myfunction.count)