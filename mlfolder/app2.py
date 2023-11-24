print('//if  statement')
temperature=25
if temperature >30:
    print('It is a hot day')
    print ('drink plenty of water')
elif temperature>20:#(20,30)
    print("It's a nice day")
elif temperature>10:#(10,20)
    print("It's a bit cold")
else:
    print("unknown")
print('exercise')
weight=int(input("weight:"))
unit=input("(k)g or (L)bs:")
if unit.upper()=="K":
    converted=weight/0.45
    print("weight in Lbs:"+str(converted))
else:
    converted=weight*0.45
    print("weight in kgs:" +(converted))

