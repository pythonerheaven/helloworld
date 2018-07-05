#
# def simple_coroutine():
#     print('-> coroutine started')
#     x = yield
#     print('-> coroutine received:',x)
#
# my_coro = simple_coroutine()
# print(my_coro)
# next(my_coro)
# my_coro.send(10)

from functools import wraps

def coroutine(func):
    '''
    装饰器：向前执行到第一个`yield` 表达式，预激`func`
    :param func:
    :return:
    '''
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total/count


coro_avg = average()
#print( next(coro_avg) )
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))
try:
    print(coro_avg.send(None))
except StopIteration as exc:
    result = exc.value

