import time,random
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="mysql12345",database="railway")
mycursor=mydb.cursor()
y="y"
l=[]
z=[]
while y=="y":
    print("\n\n\t\t\t\t\t\t\t1.BOOK YOUR TICKET(S)")
    print("\t\t\t\t\t\t\tWELCOME TO INDIAN RAILWAYS")
    print("\t\t\t\t\t\t\t2.CANCEL YOUR TICKET")
    print("\t\t\t\t\t\t\t3.BOOKED TICKETS") 
    print("\t\t\t\t\t\t\t4.CANCELLED TICKETS")
    n=int(input("Enter your choice:"))
    if n==1:
        a=int(input("Enter 5 digit Train number:"))
        print("\t\t1.Sleeper")
        print("\t\t2.3rd A.C")
        print("\t\t3.2nd A.C")
        print("\t\t4.1st A.C")
    b=int(input("Select coach:"))
    if b==1:
        berth=["lower","middle","upper","side lower","side upper"]
        rate=0
    elif b==2:
        berth=["lower","middle","upper","side lower","side upper"]
        rate=400
    elif b==3:
        berth=["lower","upper","side lower","side upper"]
        rate=1000
    elif b==4:
        berth=["lower","upper"]
        cabin=["A","B","C","D","E"]
        rate=2000
    c=int(input("Enter number of passengers:"))
    for i in range(c):
        if b==4:
            d=input("Enter name:")
            e=int(input("Enter age:"))
            f=int(input("Enter phone number:"))
            data=[d,e,f,random.choice(berth),random.randint(1,30),"Cabin:",random.choice(cabin)]
            l.append(data)
            mycursor.execute("insert into booked_tickets values('{}',{},{},'{}',{},'{}')"\
            .format(d,e,f,random.choice(berth),random.randint(1,30),random.choice(cabin)))
            mydb.commit()
        else:
            d=input("Enter name:")
            e=int(input("Enter age:"))  
            f=int(input("Enter phone number:"))
            data=[d,e,f,random.choice(berth),random.randint(1,30)]
            l.append(data)
            mycursor.execute("insert into booked_tickets values('{}',{},{},'{}',{},'{}')"\
            .format(d,e,f,random.choice(berth),random.randint(1,30),'NULL'))
            mydb.commit()
    print("\t\t 1.VEGETARIAN")
    print("\t\t 2.NON-VEGETARIAN")
    print("\t\t 3.NO FOOD")
    print("NOTE- Ticket fare is inclusive of food cost")
    j=int(input("Select food type-"))
    o=(input("Do you want a blanket set?[Rs 70 only](y/n)-"))
    if o==y:
        br=70
    else:
         br=0
    print("\t\t\t\t\t\t\t\tLOADING....")
    time.sleep(1.5)
    print("\n\nYour total fare is:",c*(1023+rate+br),"Rs only.")
    print("\n\n\n\t\t\t\t\t\t\tTICKET CREDENTIALS:",l)
    print("\t\t\t\t\t\t\tTrain number:",a)
    print("IMPORTANT NOTE-CARRY ANY GOVERNMENT ISSUED IDENTITY PROOF.")
    print("\n\t\t\t\t\t\t\tCONGRATULATIONS!!!")
    print("\n\t\t\t\t\t\t\tYOUR TICKET HAS BEEN BOOKED.")
    y=input("\n\n\nDo you want to run the program again?(y/n):")
    if y=="n":
        break
    if n==2:
        print("ENTER TICKET CREDENTIALS AS FOLLOWS:")
        time.sleep(0.8) 
        q=input("Enter name:")
        p=int(input("Enter age:"))
        m=int(input("Enter phone number:"))
        data=[q,p,m]
        z.append(data)
        print("\t\t\t\t\t\t\t\tLOADING....")
        time.sleep(1.5)
        print("\t\t\t\t\t\t\tYOUR TICKET",z, "HAS BEEN SUCCESSFULLY CANCELLED.")
        mycursor.execute("insert into cancelled_tickets values('{}',{},{})".format(q,p,m))
        mycursor.execute("delete from booked_tickets where Name='{}'".format(q))
        mydb.commit()
    y=input("Do you want to use any other service?(y/n):")
    if y=="n":
            break
    if n==3:
        if l==[]:
            print("Sorry!!! No ticket is booked.")
    else:
        print("You have booked:",l)
        y=input("Do you want to use any other service?(y/n):")
    if y=="n":
        break
    if n==4:
        if z==[]:
            print("Sorry!!! No ticket is cancelled.")
    else:
        print("You have cancelled:",z)
        y=input("Do you want to use any other service?(y/n):")
        if y=="n":
            break
            print("\n\n\n\n\n\n\n\nHAVE A SAFE AND JOYFUL JOURNEY.")
            print("\nThank you for choosing us, see you later!!!!!")