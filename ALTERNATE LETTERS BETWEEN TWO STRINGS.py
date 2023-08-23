# ALTERNATE THEE LETTERS BETWEEN TWO STRINGS
'''
a = input("ENTER STRING 1: ")
b = input("ENTER STRING 2: ")
for i in range(min(len(a), len(b))):
    s += a[i]
    s += b[i]
print(s)    
'''

a = "welcome"
b = "homely"
n = 1

s = ""
for i in range(max(len(a), len(b))):
    if i % (n + 1) == n:
        continue
    if i < len(a):
        s += a[i]
    if i < len(b):
        s += b[i]

print(s)
