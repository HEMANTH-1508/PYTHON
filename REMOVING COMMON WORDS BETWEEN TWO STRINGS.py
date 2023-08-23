# REMOVING COMMON WORDS BETWEEN TWO STRINGS

s1=input("ENTER STRING 1 : ")
s2=input("ENTER STRING 2 : ")

sent1=s1.split()
sent2=s2.split()


for i in range(min(len(sent1),len(sent2))):
    if sent1[i] in sent2:
        sent1.remove(sent1[i])
        sent2.remove(sent1[i])
        
print(sent1)
print(sent2)
        