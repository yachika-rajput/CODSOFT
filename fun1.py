def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
    
a= int(input("any number:"))
b= int(input("any number:"))
c= int(input("any number:"))
print(greatest(a,b,c))