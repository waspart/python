import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
f.close()
