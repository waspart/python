import random

ln = 3
dn = 6

#print('字母数量：' + repr(ln) +'，数字数量：' + repr(dn))

print(ln + dn)
print(ln & dn)

nolst = list(range(0, 100, 100))
nolst.append(473)
print(nolst)

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(random.random() + 1)