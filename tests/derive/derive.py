#user.py

from base import Base


base = Base()
assert hasattr(base,'foo')

class Derived(Base):
    def bar(self):
        return self.foo()

squares = []
for x in range(5):
    squares.append(lambda: x ** 2)

print(squares[2]())
print(squares[4]())


squares = []
for x in range(5):
    squares.append(lambda n=x: n ** 2)

print(squares[2]())
print(squares[4]())


def func2(a, b):
    a = 'new-value'        # a and b are local names
    b = b + 1              # assigned to new objects
    return b            # return new values

x, y = 'old-value', 99
x, y = func2(x, y)
print(x, y)                # output: new-value 100

