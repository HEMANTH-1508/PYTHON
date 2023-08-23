# SPACES, ALPHABETS, NUMBERS AND SPECIAL CHARECTERS IN A STRING

s=input("ENTER A STRING : ")

a,n,spl,sp=0,0,0,0

alp,num,spec,space=[],[],[],[]

for i in range(len(s)):
    if s[i].isalpha():
        a +=1
        alp.append(s[i])
    elif s[i].isdigit():
        n += 1
        num.append(s[i])
    elif s[i].isspace():
        sp += 1
        space.append(s[i])
    else:
        spl += 1
        spec.append(s[i])
        
print("SPECIAL CHARECTERS COUNT IS : ",spl)
print("THE SPECIAL CHARECTERS PRESENT ARE : ",spec)   

   
      