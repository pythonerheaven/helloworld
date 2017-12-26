# Series 有索引， 可以用字典的方式， DataFrame: 每一列看作一个Series,培养按列构建数据的思维

import pandas as pd
pd.__version__

import numpy as np
from pandas import Series, DataFrame

a = np.random.randn(5)
print(a)

s = Series(a,index=['a','b','c','d','e'])
print(s)


d = {'a':1,'b':2}
s = Series(d)
print(s)


d = {'one':Series([1.0,2.0,3.0],index=['a','b','c']),'two':Series([1.0,2.0,3.0,4.0],index=['a','b','c','d'])}
df = DataFrame(d)
print(df)

# df.concat 合并

print(df['one'])

# df.drop_duplicate, sort_index,
df.plot()