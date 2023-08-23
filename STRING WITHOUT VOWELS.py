# STRING WITHOUT VOWELS

s=input(" ENTER A STRING : ")
c=""
vowels="AEIOUaeiou"

for i in s:
    if i not in vowels:
        c=c+i
print(c)    
        