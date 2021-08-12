def orr():
    print("---------------------------------------------")



#null dict:
d = {}
print(d)

d = {'dict': 1, 'dictionary': 2}
print(d)


orr()


d = dict(short='dict', long='dictionary')
print(d)

d = dict([(1, 1), (2, 4)])
print(d)


orr()


d = dict.fromkeys(['a', 'b'])
print(d)

d = dict.fromkeys(['a', 'b'], 100)
print(d)


orr()

d = {a: a ** 2 for a in range(7)}
print(d)


