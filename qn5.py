n= int(input("Enter the value of numbers you want to store: "))
l1=[]
for i in range(n):
  j=int(input("Enter the value: "))
  l1.append(j)
even_indices = range(0,len(l1),2)
print(even_indices)

for index in even_indices:
    count = 0
    for i in range(1,l1[index]+1):
        if (l1[index]%i==0):
            count +=1
    if count==2:
        print(l1[index])

