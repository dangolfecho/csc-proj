import random
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="airplane")
mycursor=mycon.cursor()
themainone=["Chennai","Coimbatore","NewYorkCity","LA","NewDelhi"]
for i in themainone:
    for j in themainone:
        if i!=j:
            def timecreater():
                final=""
                a1=str(random.randint(0,23))
                if int(a1)<10:
                    a1="0"+a1
                a2=str(random.randint(0,59))
                if int(a2)<10:
                    a2="0"+a2
                final=a1+":"+a2
                return final
            def arrtimecreater(time):
                final=""
                pre=time[:2]
                t3=time[3:]
                t3=int(t3)+random.randint(1,59)
                if t3>60:
                    t4=str(int(t3-60))
                    check=1
                else:
                    check=0
                    t4=str(t3)
                if int(t4)<10:
                    t4="0"+t4
                if pre[0]=="0":
                    t1=int(pre[1])+random.randint(2,15)+check
                    if t1<10:
                        t2="0"+str(t1)
                    else:
                        t2=str(t1)
                else:
                    t1=int(pre)+random.randint(2,15)+check
                    if t1>=24:
                        t1=t1-24
                        if t1<10:
                            t1="0"+str(t1)
                    t2=str(t1)
                final=t2+":"+t4
                return final
            def durationcalc(t1,t2):
                c1=int(t1[3:])
                c2=int(t2[3:])
                if c1<c2:
                    temp=c2-c1
                elif c1>c2:
                    temp=c2-c1
                else:
                    temp=0
                if temp<0:
                    check=-1
                    temp+=60
                else:
                    check=0
                if temp<10:
                    d1="0"+str(temp)
                else:
                    d1=str(temp)
                a1=int(t1[:2])
                a2=int(t2[:2])
                if str(a1)[0]==0:
                    b1=int(a1[1])
                else:
                    b1=int(a1)
                if str(a2)[0]==0:
                    b2=int(a2[1])
                else:
                    b2=int(a2)
                if a1<a2:
                    req=str(int(a2-a1+check))
                if a2<a1:
                    req=str(int(a2-a1+24+check))
                if int(req)<10:
                    req="0"+req
                print(t1,t2)
                req=req+":"+d1
                return req

            x="INSERT INTO one "
            g="VALUES("
            a=str(random.randint(1000,7000))
            g+=a
            x=x+g
            time=timecreater()
            endtime=arrtimecreater(time)
            d=durationcalc(time,endtime)
            ticket=str(random.randint(80,160))
            price=str(random.randint(3000,3400))
            alpha=",'"+i+"','"+j+"','"+time+"','"+endtime+"','"+d+"',"+ticket+","+price+")"
            x+=alpha
            print(x)
            mycursor.execute(x)
mycon.commit()
#INSERT INTO TABLE ONE VALUES(4,deaptture city, arrival city, dept time, price
