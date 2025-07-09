n= int(input("Enter the value of numbers you want to store: "))
l1=[]
for i in range(n):
  j=int(input("Enter the value: "))
  l1.append(j)

for i in range(n):
  for j in range(n-1):
    if(l1[i]>l1[j+1]):
      l1[j],l1[j+1]=l1[j+1],l1[j]

print(f"Maximum is {l1[-1]} and minimun is {l1[0]}")
print(f"Sorted list is {l1}")
l2=[]
for i in l1:
  if i not in l2:
    l2.append(i)
print(f"without duplicate{l2}")
