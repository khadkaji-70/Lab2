num = input("Enter numbers separated by space: ").split() #split le space anusar list of string banauxa
l1 = [int(num) for num in num]
# using builtin function 
max_num=max(l1)
min_num=min(l1)
print(f"{max_num} is maximum and {min_num} is minimum")

print(sorted(l1))


print("List without duplication")
noduplicate=set(l1)
print(noduplicate)