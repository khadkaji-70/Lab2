
students={}
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter student name:")
    marks=[]
    for j in range(1,4):
        mark=int(input("Enter marks for student: "))
        marks.append(mark)
    students[name]=marks

def displayAverage(stds):
    for k,v in stds.items():
        average = sum(v) / len(v)
        print("The average is", average)


#to find topper
def displayTopper(stds):
    topper = ""
    highest = 0
    for k, v in stds.items():
        average = sum(v) / len(v)
        if average > highest:
            highest = average
            topper = k
    print(f"the topper is {topper} and highest average mark is {highest}")

def updateMarks(stds):
    name = input("Enter student name you want to update:")
    if name in stds:
        newMarks = []
        for i in range(1, 4):
            mark = int(input("Enter marks for student: "))
            newMarks.append(mark)
        stds[name] = newMarks
        print("Updated!!")
    else:
        print("Student not found")



while True:
    print("1. Display average marks")
    print("2. Display topper")
    print("3. Update marks")
    print("4. Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        displayAverage(students)
    elif choice==2:
        displayTopper(students)
    elif choice==3:
        updateMarks(students)
    elif choice==4:
        print("Exiting")
        break
    else:
        print("Invalid choice")
        continue


