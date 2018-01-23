# #library.py
# import builtins
#
# class Base(object):
#     def __init__(self):
#         pass
#
#     def foo(self):
#         return 'foo'
#
#     def __add__(self, other):
#         __build_cl
#
# old_bc = __build_class__
# def my_bc(fun,name, base):
#     if base is Base:
#         print('check if bar method defined')
#     return old_bc(fun,name,base)
#
#
#
# builtins.__build_class__ = my_obc

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        return super().__new__(cls,name,bases,body)

class Base(object):
    def foo(self):
        return self.bar()
