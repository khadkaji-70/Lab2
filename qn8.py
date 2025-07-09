n=int(input("Enter a total number of student: "))
universal=set()
for i in range(n):
  roll=int(input("Enter the roll number of student: "))
  universal.add(roll)

c=int(input("Enter number of student who play cricket:"))
cricket=set()
for i in range(c):
  roll=int(input("Enter cricket player's roll no: "))
  cricket.add(roll)

f=int(input("Enter the number of football players: "))
football=set()
for i in range(f):
  roll=int(input("Enter the roll no of football players: "))
  football.add(roll)

print(f"The roll number of students who play both sports are {cricket & football}")
print(f"The roll number of students who play neither sports are {cricket | football}")
print(f"The roll number of students who play only one sports are {cricket ^ football}")



