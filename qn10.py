#to find unique vowels in a sentence
vowel={'a','e','i','o','u'}
unique=set()
string=input("Enter a sentence: ")
for char in string.lower():
    if char in vowel:
        unique.add(char)

print("the unique vowels used are",unique)

