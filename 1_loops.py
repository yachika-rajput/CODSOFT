'''for i in range(1,100):
    
    
    print(i)

l = ["yachi",True,"hello",34]
i=0
while(i<len(l)):
    print(l[i])
    i += 1
    '''
# prime number
n = int(input("enter a number:"))
for i in range(2,n):
    if(n%i==0):
        print("no is not prime")
    break
else:
    print("no is prime")