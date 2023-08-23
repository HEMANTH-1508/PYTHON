# TO KNOW THE VOWELS AND CONSONENTS IN A STRING

s=input("ENTER A STRING : ")
vowels="AEIOUaeiou"
v=0
c=0
vo=[]
co=[]

for i in s:
    if i.isalpha():
        if i in vowels:
            v += 1
            vo.append(i)
        else:
            c += 1
            co.append(i)
          
print("VOWELS COUNT : ",v)
print("VOWELS ARE : ",vo)
print("CONSONENTS COUNT : ",c)
print("CONSONENT ARE : ",co) 
               
if c==v:
    print("VOWELS AND CONSONANTS ARE EQUAL IN NUMBER")
elif c>v:
    print("CONSONANTS ARE MORE THAN VOWELS")
else:
    print("VOWELS ARE MORE THAN CONSONANTS")     
    
              