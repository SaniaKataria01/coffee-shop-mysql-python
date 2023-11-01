import mysql.connector
import datetime
import json

mycon=mysql.connector.connect(host='localhost',password='1234',user='root',database='csproject')
if mycon.is_connected():
    print("SUCCESSFULLY CONNECTED\n")
cursor=mycon.cursor()

s="create table IF NOT EXISTS MENU (ITEM_CODE VARCHAR(3),CATEGORY VARCHAR(15),ITEM VARCHAR(30),PRICE INT(6))"
cursor.execute(s)

st="create table IF NOT EXISTS CUSTOMER (ORDER_NO INT(5),NAME VARCHAR(30),PHNO INT(12) UNIQUE ,EMAIL VARCHAR(30),ORDER_DATE DATE,TIME VARCHAR(10),CUST_ORDER VARCHAR(200))"
cursor.execute(st)

st="create table IF NOT EXISTS EMPLOYEE (EMP_ID VARCHAR(5), EMPLOYEE_NAME VARCHAR(30),POST VARCHAR(20),DATE_OF_JOIN DATE,SALARY INT(10),ADDRESS VARCHAR(100))"
cursor.execute(st)

cursor.execute("select * from menu ORDER BY CATEGORY ")
data=cursor.fetchall()

cursor.execute("select * from customer")
cust=cursor.fetchall()

def menu_add():
        
        srno=input("ITEM CODE: ")
        category=input("CATEGORY: ")
        item=input("ITEM NAME: ")
        cost=int(input("COST: "))
        
        ord=(srno,category,item,cost)
        st="insert into menu values(%s,%s,%s,%s)"
        cursor.execute(st,ord)
        print("\nITEM ADDED SUCCESSFULLY")
                

def del_menu():
    srno=input("ITEM CODE TO BE DELETED: ")
    
    f=0
    for i in data:
        if i[0]==srno:
            st="delete from menu where item_code=%s"
            tu=(srno,)
            cursor.execute(st,tu)
            f=1
    if f==1:
        print("ITEM DELETED SUCCESSFULLY")
    else:
        print("RECORD NOT FOUND TRY AGAIN")


def update_menu():
    srno=input("ITEM CODE: ")
    pr=int(input("CHANGED PRICE: "))
    f=0
    for i in data:
        if i[0]==srno:
            st="UPDATE MENU SET PRICE=%s where item_code=%s"
            tu=(pr,srno)
            cursor.execute(st,tu)
            f=1
    if f==1:
        print("ITEM UPDATED SUCCESSFULLY")
    else:
        print("RECORD NOT FOUND TRY AGAIN")

def display_menu():
        print("                                                  MENU\n")
        print("+--------------------------------------------------------------------------------------------------------------------+")
        print("|ITEM CODE                   |CATEGORY                    |ITEM                        |COST                         |")
        print("+--------------------------------------------------------------------------------------------------------------------+")

        for s in data:
            print("|",s[0]," "*(25-len(s[0])),
                  "|",s[1]," "*(25-len(s[1])),
                  "|",s[2]," "*(25-len(s[2])),
                  "|",s[3]," "*(26-len(str(s[3]))),"|")
            print("+--------------------------------------------------------------------------------------------------------------------+")


def record():
            global x
            display_menu()
            
            name=input("NAME ")
            ph_no=int(input("PHONE NUMBER: "))
            email_id=input("EMAIL ID: ")
            ord_no=x+1
            z=order()
            y = json.dumps(z)
            today = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            tu=(ord_no,name,ph_no,email_id,today,current_time,y)
            st="insert into customer values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(st,tu)
            
            return tu




def order():
    
    w='Y'
    ordr=()
    while w=='Y':
        print()
        icode=input("ITEM CODE: ")
        qty=int(input("QUANTITY: "))
        li=[]
        for s in data:
                if s[0]==icode:
                    cost=s[3]*qty
                    
                    li=[icode,s[2],qty,cost]
                    break
        ordr+=(li,)
            

        w=input("CONTINUE ORDERING Y for yes /N for no : ")    
    
    return ordr


def invoice():
    tot=0
    print('\n\n')
    o=record()
    a=o[-1]
    ad=json.loads(a)
    pri_inv=input("\nPRINT INVOICE Y/N: \n")
    if pri_inv=='Y':
        print("                                        FRESH BREW  ")
        print("                       421,SECTOR-6,GANPATI CHOWK,DWARKA,NEW DELHI\n")
        print("                                         INVOICE\n")
        print("ORDER NO:",o[0],"\tNAME:",o[1],'\tDATE:',o[-3],'\tTIME:',o[-2])    
        print("\n+--------------------------------------------------------------------------------------------------------------------+")
        print("|ITEM CODE                   |CATEGORY                    |ITEM                        |COST                         |")
        print("+--------------------------------------------------------------------------------------------------------------------+")
        for i in range (len(ad)):
                tot=tot+int(ad[i][-1])
                print(  "|",ad[i][0]," "*(25-len(ad[i][0])),
                        "|",ad[i][1]," "*(25-len(ad[i][1])),
                        "|",ad[i][2]," "*(25-len(str(ad[i][2]))),
                        "|",ad[i][3]," "*(26-len(str(ad[i][3]))),"|")
        print("+--------------------------------------------------------------------------------------------------------------------+")

        print("\n                                                                                    TOTAL :Rs.",tot)
        print("\n-------------------------THANK YOU FOR VISITING FRESH BREW ---------------------------")
        print("********************VISIT US ON OUR OFFICIAL WEBSITE www.freshbrew.com********************\n\n")
    else:
          print("\n-------------------------THANK YOU FOR VISITING FRESH BREW ---------------------------")
          print("********************VISIT US ON OUR OFFICIAL WEBSITE www.freshbrew.com********************\n\n")  




'''x=1
print("IS IT THE FIRST RECORD OF THE DAY: ")
an=input("Y/N ")
if an=='Y':
        x=0
elif an=='N':
        dte=input("DATE: ")
        l=[]
        for l in cust:           
                if str(l[-3])==str(dte):
                        
                        if x<int(l[0]):
                             x=int(l[0])  '''        

def disp_customer_record():
    print("                                                                      CUSTOMER RECORDS\n")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|ORDERNO |      NAME       |    PHNO    |       EMAIL         |    DATE     |   TIME    |                                ORDER                                                   |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    for s in cust:
                print(  "|",s[0]," "*(5-len(str(s[0]))),
                        "|",s[1]," "*(14-len(s[1])),
                        "|",s[2]," "*(9-len(str(s[2]))),
                        "|",s[3]," "*(18-len(s[3])),
                        "|",s[4]," "*(0-len(str(s[4]))),
                        "|",s[5]," "*(3-len(str(s[5]))),
                        "|",s[6]," "*(85-len(str(s[6]))),"|")
                print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print()

def search_customer():
        na=input('NAME: ')
        date=input('DATE : ')
        a=0
        for i in cust:
                if i[0]==str(ord_no) and i[-3]==date and i[1]==na.upper():
                        print("\nRECORD FOUND")
                        print(i)
                        a=1
        if a==0:
                print("\nRECORD NOT FOUND")
                
def customer_delete():
        f=0
        ordno=int(input("ORDER NO TO BE DELETED: "))
        name=input("CUSTOMER NAME: ")
        dte=input("DATE OF ORDER WITH 00:00:00.0000: ")
        date_time_obj = datetime.datetime.strptime(dte, '%Y-%m-%d %H:%M:%S.%f')
        date=date_time_obj.date()
        for reco in cust:
                if(reco[0]==ordno and reco[1]==name and reco[-3]==date ):
                        f=1
                        st="delete from CUSTOMER where ORDER_NO=%s and NAME=%s and ORDER_DATE=%s"
                        tu=(ordno,name,date)
                        cursor.execute(st,tu)
            

        if(f==1):
                print("\nRECORD FOUND AND DELETED")
        else:
                print("\nNO SUCH RECORD FOUND !")
                       
def staff_add():
        name=input("EMPLOYEE NAME: ")
        emp_id=input("EMPLOYEE ID: ")
        post=input("EMPLOYEE POST: ")
        date_of_join=input("DATE OF JOIN: ")
        salary=input("EMPLOYEE SALARY")
        phno=input("EMPLOYEE PHONE NO: ")
        address=input("ADDRESS: ")
        rec=(emp_id,name,post,date_of_join,salary,phno,address)
        s="insert into "
        print("\nRECORD ADDED SUCCESSFULLY!")



mycon.commit()






























