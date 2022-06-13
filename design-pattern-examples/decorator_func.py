def entry_exit(func):
    def wrapped_func():
        print(f"Entering {func.__name__}")
        func()
        print(f"Exiting {func.__name__}")

    return wrapped_func


@entry_exit
def my_func():
    print("Inside my_func")


my_func()
