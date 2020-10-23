import random
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="airplane")
mycursor=mycon.cursor()
themainone=["Chennai","Coimbatore","NewYorkCity","LA","NewDelhi"]
for i in themainone:
    for j in themainone:
        if i!=j:
            x="INSERT INTO one "
            g="VALUES("
            a=str(random.randint(5,35))
            g+=a
            x=x+g
            alpha=",'"+i+"','"+j+"',"+"11.50"+","+str(random.randint(3000,3400))+")"
            x+=alpha
            mycursor.execute(x)
            mycon.commit()
#INSERT INTO TABLE ONE VALUES(4,deaptture city, arrival city, dept time, price
