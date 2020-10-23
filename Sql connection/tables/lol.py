import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="airplane")
mycursor=mycon.cursor()
themainone=["Chennai","Coimbatore","NewYorkCity","LA","NewDelhi"]
j=["one","two","three","four","five"]
for i in j:
    x="CREATE TABLE "
    y=str(i)
    x=x+y
    x=x+" "
    g="(Flight integer(4) PRIMARY KEY,Departure_city varchar(5),Arrival_City varchar(5), Departure_Time varchar(5), Price Integer(6))"
    x=x+g
    print(x)
    mycursor.execute(x)
