l1=[1,2,4,3,2,4,24,5]
l2=[3,2,4,2,4,2,1,3,5]
mergedList=l1+l2
print(f"Merged list is {mergedList}")
l3=mergedList.copy()
for i in l3:
  if i in l1 and i in l2:
    l3.remove(i)

print(l3)
