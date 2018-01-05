
hk_trading = 1
is_hk_trade = 1
us_trading = 1
trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)

hk_trading = 1
is_hk_trade = 1
us_trading = 0

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)


hk_trading = 1
is_hk_trade = 0
us_trading = 0

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)

hk_trading = 0
is_hk_trade = 0
us_trading = 0

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)



hk_trading = 0
is_hk_trade = 1
us_trading = 1

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)


hk_trading = 0
is_hk_trade = 0
us_trading = 1

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)


hk_trading = 0
is_hk_trade = 1
us_trading = 0

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)


hk_trading = 1
is_hk_trade = 0
us_trading = 1

trading = hk_trading if is_hk_trade else us_trading
print(trading)
print(hk_trading)

def get_adder(summand1):
    """Returns a function that adds numbers to a given number."""
    def adder(summand2):
        return summand1 + summand2
    return adder

sum = get_adder(1)(2)
print(sum)

i = 4
def foo(x):
    def bar():
        print i
    # ...
    # A bunch of code here
    # ...
    for i in x: # Ah, i *is* local to Foo, so this is what Bar sees
        print i

    bar()
    return i

print( foo([1,2,3]) )