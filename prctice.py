p1 = "make a lot of money"
p2 = "subscribe"
p3 = "buy now"


m = input("any message:")

if(p1 in m or (p2 in m) or ( p3 in m)):
    print("message is spam ")
else:
    print("not spam")
 
