#create a funct that accpets a lot of arguments and can return the sum of the arg
# with one '*' it is called =positional argument= becoues we can access them py position as they are a tuple
# def add(*args):
#     print(args[2])
#     summ = 0
#     for n in args:
#         summ += n
#     print(summ)
    
    
# add(2,3,48,9)
# # the output
# # 48
# # 62


# create a func with '**' called =key word arguments=
# key ward args are a dictionary 
def calculate(n, **kwargs):
    n += kwargs["add"]# the value of the key=add is the number whitch will be added the number n
    n *= kwargs["multiply"]
    print(n)


calculate(2, add = 3, multiply = 5)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")     #is the same as -kw["make"]- but uses get if we dont want to specify the value of make
        self.model = kw.get("model")   #kw["model"]

my_car = Car(make = "Nissan", model = "GT-R")       
print(my_car.model)  

