test = 'hello there'
dct = {key:test.count(key) for key in test}
print(dct)
res = min(dct, key=dct.get)
print(res)