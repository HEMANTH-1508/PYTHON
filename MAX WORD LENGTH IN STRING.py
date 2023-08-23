# WHICH  MAX  WORD LENGTH IN THE STRING 

s=input("ENTER A STRING : ")

s1=s.split()
l=[]

for i in s1:
    
    l.append(len(i))
    
print(max(l))  