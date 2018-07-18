def normalize(name):
    new_name = []
    new_name.append(name[0].upper())
    for n in name[1:]:
        new_name.append(n.lower())
    return ''.join(new_name)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)