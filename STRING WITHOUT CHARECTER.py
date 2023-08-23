# STRING WITHOUT THE GIVEN CHARECTER

s=input(" ENTER A STRING : ")
char=input("ENTER THE CHARECTER : ")

c=""

for i in s:
    if i not in char:
        c=c+i
print(c)
 