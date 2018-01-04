
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