'''N = int(input("enter number:"))
i = 1

sum = 0
while(i<=N):
    sum = sum+i
    i+=1
print(sum)

# factorial program

N = int(input("enter number:"))
i=1
fact = 1
while(i<=N):
    fact = fact*i
    i+=1


print(fact)
'''

n = int(input("enter number:"))
p = int(input("enter: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*(2*i-1),end="")
    print("\n")
for i in range(n+1):
    for j in range(p+1):
        print("  ",end="")
        print("*",end="")
    print("\n")