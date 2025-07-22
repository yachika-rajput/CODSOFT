n=6
i = 0
for i in range(1,n):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
for i in range(1,n-2):
    for j in range(1,n*2):
        print("*",end="")
    print("")

