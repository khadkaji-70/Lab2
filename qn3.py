string = input("Enter string separated by space: ")#split le space anusar list of string banauxa
l1 = string.split()
unique=[]
print(l1)
for word in l1:
  if word  not in unique:
    unique.append(word)

for word in unique:
  print(word,l1.count(word))