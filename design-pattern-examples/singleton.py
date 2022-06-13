class Singleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call getInstance() instead")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


o1 = Singleton.get_instance()
print(o1)

o2 = Singleton.get_instance()
print(o2)