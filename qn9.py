import random

num=set()
while len(num)<10:
  num.add(random.randint(1,100))

print(f"Set with 10 unique numbers: {num}")

smallest=min(num)
largest=max(num)
num.remove(smallest)
num.remove(largest)

print(f"Set after removing smallest and largest numbers:{num} ")
