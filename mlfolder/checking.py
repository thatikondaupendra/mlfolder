lys=1
nlys=1
c=0
for i in range(1991,2020):
    print(i)
    c += 1
    if (i%4==0 and i%100!=0):
        print(i)
        lys+=1
    elif(i%400==0):
        print(i)
        lys+=1
    else:
        nlys+=1
print(lys,nlys,c)