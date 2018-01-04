import numpy
import talib

close = numpy.random.random(100)

output = talib.MACD(close,2,3,4)
print(output)