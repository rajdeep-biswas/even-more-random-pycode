s1 = 'garage'
s2 = 'bag'

mark1 = -1
mark2 = -1

if s2 in s1:
    mark1 = s1.index(s2)

elif s1 in s2:
    mark2 = s2.index(s1)

if mark2 != -1:
    for i in range(len(s2)):
        if i not in range(mark2, mark2 + len(s1)):
            print('inserted', s2[i])
    
elif mark1 != -1:
    for i in range(len(s1)):
        if i not in range(mark1, mark1 + len(s2)):
            print('deleted', s1[i])

else:
    i1 = 0
    i2 = 0
    
    while len(s1) != len(s2):
        if len(s1) > len(s2):
            print('deleted', s1[i1])
            s1 = s1[i1 + 1:]
        else:
            print('inserted', s2[i2])
            i2 += 1
            s1 = s2[:i2] + s1
        print(s1)

    i1 = 0

    while s1 != s2:
        if s1[i1] != s2[i1]:
            print('replaced', s1[i1], 'with', s2[i1])
            s1 = s1[:i1] + s2[i1] + s1[i1 + 1:]
        i1 += 1
