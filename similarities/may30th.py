a = "philadelphia"
b = "bucharest"

c = 0
while a != b:

    if c < len(a) and c < len(b):
        if a[c] == b[c]:
            print(a.upper())
            c += 1
            
        elif a[c] != b[c]:
            print(a, a[c].upper(), '/ substituted', a[c], 'with', b[c], c)
            a = a[:c] + b[c] + a[c + 1:]
            c += 1

    elif len(a) < len(b):
        a = a[:c] + b[c] + a[c:]
        print(a, a[c].upper(), '/ inserted', b[c], c)
        c += 1

    else:
        print(a, a[c].upper(), '/ deleted', a[c], c)
        a = a[:c] + a[c + 1:]
