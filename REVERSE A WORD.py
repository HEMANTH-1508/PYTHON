# to arrange letters alphabatically in in reverse order

word = input("Enter a word: ")

sorted_word = ''.join(sorted(word))

reverse_sorted_word = ''.join(sorted(word, reverse=True))

print("Alphabetically in normal order:", sorted_word)
print("Alphabetically in reverse order:", reverse_sorted_word)

