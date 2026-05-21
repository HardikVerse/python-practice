'''Problem: Create a decorator to print the function name 
and the values of its arguments every time the function 
is called.'''


def decorator(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key} : {value}" for key, value in kwargs.items())
        print(f"Calling: {func.__name__} function with args {args_value} and kwargs {kwargs_value}.")
        return func(*args, **kwargs)
    return wrapper



@decorator
def intro(name, greet = "Hello"):
    print(f"{greet}, {name}")

intro("Hardik")

