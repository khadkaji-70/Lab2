string=input("enter a string: ")
freq={}
for char in string.lower():
    if char.isalpha():
        freq[char]=freq.get(char,0)+1

print(freq)

