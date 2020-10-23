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
    g="(Flight integer(7) PRIMARY KEY,Departure_city varchar(30),Arrival_City varchar(30), Departure_Time varchar(10), Arrival_Time varchar(10), Duration varchar(10), Tickets integer(4), Price Integer(10))"
    x=x+g
    mycursor.execute(x)
