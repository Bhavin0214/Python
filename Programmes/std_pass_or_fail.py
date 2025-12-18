# take marks of students
a = int(input("enter your maths marks: "))
b = int(input("enter your secince marks: "))
c = int(input("enter your SST marks: "))

# for a get percentage
pr = ((a+b+c)/300)*100

# condition for pass or fail
if pr>=40 and a>=33 and b>=33 and c>=33:
    print(" congras! you are pass! ")
else:
    print("try again next time sorry you are fail.")

print("your percentage is :", pr)