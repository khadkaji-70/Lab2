n=int(input("Enter the number of elements: "))
l1=[]
for i in range(n):
  num=int(input("Enter the value: "))
  l1.append(num)

t1=tuple(l1)
average=(sum(t1)/n)
print(f"the average is {average}")
t2=(sorted(t1))
if(n%2==0):
  median=(t2[(n-1)//2]+t2[((n-1)//2)+1])/2
else:
  median=t2[(n-1)//2]

print(f"Median is {median}")
#mode
max_count=0
mode=None
for num in t2:
  count=t2.count(num)
  if (count>max_count):
    max_count=count
    mode=num

print(f"The mode of the tuple is {mode} with frequency {max_count}")






