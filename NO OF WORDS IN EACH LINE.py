#  TO FIND THE NUMBER OF WORDS IN EACH LINE 

s=input("ENTER THE STRING : ")

s1=s.split(".")
s1.pop()

print("NUMBER OF LINES IS/ARE : ",len(s1))

a=1
for i in s1:
    word=i.split()
    a+=1
    print("NO OF WORDS IN LINE ",":",len(word))
    
    
    