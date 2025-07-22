mark1 = a = int(input("first marks:"))
mark2 = a = int(input("second marks:"))
mark3 = a = int(input("third marks:"))
total_percentage = 100*(mark1 + mark2+ mark3)/300
print(total_percentage)
if (total_percentage >= 40 and mark1>=33 and mark2 >= 33 and mark3>=33):
    print("passed")
else:
    print("failed")




