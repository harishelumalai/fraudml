import random
i=0
f=open("input.csv","w")
while i<500:
    amt=0
    fraud=0
    notfraud=0
    #random amount between 1.00 to 499.99

    amt=random.randint(100,49999)
    f.write(str(amt)+","+str(fraud)+"\n")
    #f.write(str(amt)+","+str(fraud)+","+ str(notfraud) +"\n")

    amt=random.randint(50000,100000)
    fraud=1
    f.write(str(amt)+","+str(fraud)+"\n")
    #f.write(str(amt)+","+str(fraud)+","+ str(notfraud) +"\n")
    i+=1
f.close()