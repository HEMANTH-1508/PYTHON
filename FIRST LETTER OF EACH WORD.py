# PRINTING FIRST LETTER OF EACH WORD

s=input("ENTER THE STRING : ")

s1=s.split()

for i in range (len(s1)):
    print(s1[i][0].upper(),end=".")