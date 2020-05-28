import random
i=0
f=open("input2.csv","w")
while i<1000:
    amt=0
    fraud=0
    notfraud=0
    txncount=0

    txncount=random.randint(0,10)
    #random amount between 1.00 to 499.99
    amt=random.randint(100,100000)
    #f.write(str(amt)+","+str(fraud)+"\n")
    #f.write(str(amt)+","+str(fraud)+","+ str(notfraud) +"\n")

    if txncount>=5:
        fraud=1
    elif amt>50000:
        fraud=1
    f.write(str(amt/100.00)+","+str(txncount)+","+ str(fraud) +"\n")
    i+=1
f.close()