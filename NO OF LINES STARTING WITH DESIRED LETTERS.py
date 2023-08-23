# number of lines starting with desired letter

def start(text):
    a = text.split('. ')
    count = 0
    for sentence in a:
        if sentence.startswith(x):
            count += 1
    return count

x=input("ENTER THE ALPHABET : ")
text=input("ENTER THE TEXR : ")
count = start(text)
print(" sentences starting with the given alphabet are : ",count)
