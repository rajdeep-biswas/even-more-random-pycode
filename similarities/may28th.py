a = "kitten"
b = "sitting"

if len(a) < len(b):
    c = 0
    while len(a) != len(b):
        a = a[:c] + b[c] + a[c:]
        print('inserted', b[c])
        c += 1
        print(a)
        
else:
    c = 0
    while len(a) != len(b):
        print('deleted', a[0])
        a = a[1:]

while a != b:
    if a[c] != b[c]:
        print('substituted', a[c], 'with', b[c])
        a = a[:c] + b[c] + a[c + 1:]
        c += 1
        print(a)
    else:
        c += 1
