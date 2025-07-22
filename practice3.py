'''username = input("enter any name : ")

if (len(username)<= 10):
    print("username contain less ch than 10")
else:
    print("username not contain less ch than 10")


l = ["yachika":"riya":"paril":"darshil"]
name = input("enter any name: ")

if(name in l):
    print("name is in list")
else:
    print("go to hell")
'''

d =  {}
  
name = input("enter name: ")
lang = input("enter language:")
 
d.update({name:lang})
name = input("enter name: ")
lang = input("enter language:")
 
d.update({name:lang})

name = input("enter name: ")
lang = input("enter language:")
d.update({name:lang})
name = input("enter name: ")
lang = input("enter language:")
 
d.update({name:lang})

print(d)
