# make a empty list for input data
marks = []

# add data by append means add in last in the  list
m1 = int(input("Enter your marks here: "))
marks.append(m1)
m2 = int(input("Enter your marks here: "))
marks.append(m2)
m3 = int(input("Enter your marks here: "))
marks.append(m3)
m4 = int(input("Enter your marks here: "))
marks.append(m4)
m5 = int(input("Enter your marks here: "))
marks.append(m5)
m6 = int(input("Enter your marks here: "))
marks.append(m6)

# sort the list by using sort functions 
marks.sort()

print(marks)
print(type(marks))