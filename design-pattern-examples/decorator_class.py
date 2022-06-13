class EntryExit:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(f"Entering {self.func.__name__}")
        self.func()
        print(f"Exiting {self.func.__name__}")


entry_exit = EntryExit  # enforce PEP8 compliance. useful? debatable!


@entry_exit
def my_func():
    print("Inside my_func")


my_func()