# to find the index of the given charecter

def find_char(s, c):
    for i in range(len(s)):
        if s[i] == c:
            print(f"The character '{c}' is present at index {i}.")
            return
    print(f"The character '{c}' is not present in the string.")

s=input("ENTER THE TEXT : ")
c=input("ENTER THE CHARECTER NEED TO BE SEARCHED : ")
find_char(s,c)

