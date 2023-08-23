# ANAGRAM OR NOT

s1=input("ENTER STRING 1 : ")
s2=input("ENTER STRING 2 : ")

for i in s1.lower():
    if i in s2.lower():
        continue
    else:
        print("NOT AN ANAGRAM")
        break
print("ANAGRANM")    
