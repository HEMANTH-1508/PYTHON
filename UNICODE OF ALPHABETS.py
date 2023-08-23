# UNICODE OF THE ALPHABETS 


import  string

alphabets=list(string.ascii_uppercase)

for i in range(len(alphabets)):
    print(alphabets[i],"=",ord(alphabets[i]))
    
    
alphabets=list(string.ascii_lowercase)

for i in range(len(alphabets)):
    print(alphabets[i],"=",ord(alphabets[i]))    
