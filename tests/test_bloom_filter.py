from eth_bloom import BloomFilter

b = BloomFilter()
print(b'a value' in b)

print(type(b))
b.add(b'a value')
a = int(b)
print(bin(b))

print(b'a value' in b)
print(int(b))
print(len(bin(b)))

c = BloomFilter(bin(b))
print(b'a value'  in b)

url = 'http://163.com'
print(bytes(url.encode('utf-8')) in b )

b.add(bytes(url.encode('utf-8')))
print(bytes(url.encode('utf-8')) in b )
