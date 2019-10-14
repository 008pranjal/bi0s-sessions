with open('./Twin1', 'rb') as f:
    twin1 = f.read()
   
with open('./Twin2', 'rb') as f:
    twin2 = f.read()
   
f = ''
for i in range(min(len(twin1), len(twin2))):
    if twin1[i] != twin2[i]:
        f += str(twin2[i])
print(f)
