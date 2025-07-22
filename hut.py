import pyttsx3
engine = pyttsx3.init()
engine.say("hlooooooooo,here presented a house.")
engine.runAndWait()
n = 10
i = 0
for i in range(1,n):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),"@"*n*2,end="")
    print("")

for i in range(1,n-2):
    for j in range(1,n*2):
        #print("",end="")
        print("*.",end="")
    print("")
for i in range(1,n-2):

 #   print(""*2,end="")
    print("*."*2," "*4,end=" ")
    print("*."*(2*n-6),end="")
    print("")