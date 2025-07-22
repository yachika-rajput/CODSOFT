'''name  = input("enter your name: ")
print(f"good afternoon {name}")'''

letter = ''' Dear "<|name|>,
you are selected! <|date|>...'''

print(letter.replace("<|name|>" , "yachi").replace("<|date|>" , "34 sept"))