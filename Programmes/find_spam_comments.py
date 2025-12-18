# set spam comment for detect
s1 = "earn money"
s2 = "join now"
s3 = "comment for link"
s4 = "online pyment"
# make a variable for comment
comment = input("enter your comment here: ")
# give conditions for find soam in commments
if ((s1 in comment) or (s2 in comment) or (s3 in comment) or (s4 in comment)):
    print("this is spam. be aware of this.")

else:
    print("the comment is safe, don't worry.")