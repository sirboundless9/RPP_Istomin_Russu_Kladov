import sys
massiv = []
for arg in sys.argv[1:]:
    massiv.append(arg)
print(massiv)
id = list(map(lambda x: int(x), massiv))
print(id)
print(max(id))
id.reverse()
print(id)
avg = sum(id) / len(id)
print(avg)
print([avg if x == 0 else x for x in id])
