# PRINTING UNCOMMON WORDS IN BOTH THE STRINGS


string1 =input("ENTER STRING 1 : ")
string2 =input("ENTER STRING 2 : ") 
words1 = string1.split()
words2 = string2.split()

a=[]
b = []
for word in words1:    
    if word not in words2:        
        a.append(word)

for word in words2:    
    if word not in words1:
        b.append(word)      
 
print(a,b)

