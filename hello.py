# def multiply_and_great(*args, **kwargs):
#     for Key,value in kwargs.items():
#      print("The value  {} is {}" .format(Key,value))
    
#     multiply_and_great()
def multiply_and_great(*args,**kwargs):
    multiply=1
    for num in args:
        multiply*=num
        print(f"Hello {kwargs['name']} you are {kwargs['age']}  and you are from {kwargs['country']}.The result is {multiply}")