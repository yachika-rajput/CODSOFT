#n = int(input("enter number:"))
n=6
i = 0
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

print("\n")

n = 7
for i in range(1,n-2):
    for j in range(1,n):
        print("*"*2,end="")
    print("")

n = 7
for i in range(1,n-2):
    print("*"*(n-1)*2,end="")
    print("")