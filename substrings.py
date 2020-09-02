def checkPal(s):
    return s == s[::-1]

def substrings(s):
    count = 0
    for i in range(0, len(s)):
        for j in range(len(s), 0, -1):
            if s[i:j] and checkPal(s[i:j].strip()) and len(s[i:j]) > 1:
                count += 1

    return count

p = substrings("abaab")
