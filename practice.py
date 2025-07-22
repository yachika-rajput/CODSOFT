a = int(input("first number:"))
b = int(input("second number:"))
c = int(input("third number:"))
d = int(input("fourth number:"))
if (a>b and a>c and a>d):
    print("a is greatest",a)
elif(b>a and b>c and b>d):
    print("b ia greatest",b)
elif(c>a and c>b and c>d):
    print("c is greatest",c)
else:
    print("d is greatest",d)