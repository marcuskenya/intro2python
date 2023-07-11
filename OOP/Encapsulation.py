class Base:
    def __init__(self, a, b,c,d):
        self.a = "I have rights"
        self.__b = "and priviledges"
        self.c= "more rights"
        self.d="and power"


class Derived(Base):
    def __init__(self):
        print(self.a)
        print(self.__b)
        print(self.c)
        print(self.d)


# create an instance of the parent class.
obj1 = Base('a','b','c','d')
print(obj1.a)
# print(obj1.b) unaccesible
print(obj1.c)
print(obj1.d)

