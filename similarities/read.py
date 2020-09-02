with open("lines1.txt", "r") as file:
    a = file.read()

with open("lines2.txt", "r") as file:
    b = file.read()

n = 2

substrA = []

for i in range(0, len(a)):
    if not len(a[slice(i, i + n)]) < n:        
        substrA.append(a[slice(i, i + n)])

print(substrA)
substrB = []

for i in range(0, len(b)):
    if not len(b[slice(i, i + n)]) < n:
        substrB.append(b[slice(i, i + n)])

print(substrB)
lines = []

for line in substrB:
    if line in substrA and line not in lines:
        lines.append(line)
