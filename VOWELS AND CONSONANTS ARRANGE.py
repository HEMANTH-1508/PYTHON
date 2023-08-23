# to arrange vowels and consonants alphabatically in in reverse order

word = input("Enter a word: ")
vowels = []
consonants = []
for i in word:
    if i.lower() in "aeiou":
        vowels.append(i.lower())
    elif i.isalpha():
        consonants.append(i.lower())
print("Vowels:", ", ".join(sorted(vowels)))
print("Consonants:", ", ".join(sorted(consonants)))
if len(vowels) > len(consonants):
    print("There are more vowels than consonants.")
elif len(consonants) > len(vowels):
    print("There are more consonants than vowels.")
else:
    print("There are an equal number of vowels and consonants.")
    