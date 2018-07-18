s = 0
t = 1

for i in list(range(1, 21)):
    t *= i
    s += t

print('1!+2!+....+20!=' + repr(s))
