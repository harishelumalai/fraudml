import random
i=0
f=open("input.csv","w")
while i<1000:
    amt=0
    fraud=0
    #random amount between 1.00 to 499.99
    if i<500:
        amt=random.randint(100,49999)
    else:
        amt=random.randint(50000,100000)
        fraud=1
    f.write(str(amt)+","+str(fraud)+"\n")
    i+=1
f.close()