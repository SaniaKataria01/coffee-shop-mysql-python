#modules imported
import pickle
from datetime import date,datetime
import os
import csv
#-----------------------------------------------------------------------------------------------------------------------------------------
print("_______________________________________________________________________________________________________________________________________________________________________________________")

print("*************************************************************************************WELCOME TO FRESH BREW***************************************************************************** ")
print("________________________________________________________________________________________________________________________________________________________________________________________\n")

#function definition
                
def createmenu():
        file=open("Menu.dat","ab")
        c="Y"
        while(c=="Y"):
            
            srno=input("ITEM CODE: ")
            category=input("CATEGORY: ")
            item=input("ITEM: ")
            cost=int(input("COST: "))
            order=[srno,category,item,cost]
            pickle.dump(order,file)
            
            c=input("enter Y/N: ")
        file.close()    


def display_menu():
        file=open("Menu.dat",'rb')
        print("                                                  MENU\n")
        print("+--------------------------------------------------------------------------------------------------------------------+")
        print("|ITEM CODE                   |CATEGORY                    |ITEM                        |COST                         |")
        print("+--------------------------------------------------------------------------------------------------------------------+")
        try:
                while True:
                        s=pickle.load(file)
                        print("|",s[0]," "*(25-len(s[0])),
                              "|",s[1]," "*(25-len(s[1])),
                              "|",s[2]," "*(25-len(s[2])),
                              "|",s[3]," "*(26-len(str(s[3]))),"|")
                        print("+--------------------------------------------------------------------------------------------------------------------+")
        except EOFError:
                file.close()


def record():
            global x
            display_menu()
            
            fi=open("customer.csv",'a',newline='')
            name=input("NAME ")
            ph_no=int(input("PHONE NUMBER: "))
            email_id=input("EMAIL ID: ")
            ord_no=x+1
            z=order()
            
            today = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            tu=[ord_no,name,ph_no,email_id,today,current_time,z]
            wr=csv.writer(fi)
            wr.writerow(tu)

            return tu




def order():
    f=open("Menu.dat",'rb')
    w='Y'
    ordr=[]
    while w=='Y':
        print()
        icode=input("ITEM CODE: ")
        qty=int(input("QUANTITY: "))
        li=[]
        try:
            while True:
                s=pickle.load(f)
                
                if s[0]==icode:
                    cost=s[3]*qty
                    
                    li=[icode,s[2],qty,cost]
                    break
            ordr.append(li)
            
        except EOFError:
            pass

        w=input("CONTINUE ORDERING Y for yes /N for no : ")    
    
    return ordr


def invoice():
    tot=0
    print('\n\n')
    o=record()
    ad=o[-1]
    pri_inv=input("PRINT INVOICE Y/N: ")
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


def menu_add():
    
        file=open("Menu.dat","ab")

        srno=input("ITEM CODE: ")
        category=input("CATEGORY: ")
        item=input("ITEM NAME: ")
        cost=int(input("COST: "))
        ord=[srno,category,item,cost]
        pickle.dump(ord,file)
        print("\nITEM ADDED SUCCESSFULLY")
        file.close()        
                
       
                
def del_menu():
    found=False
    file=open("Menu.dat","rb")
    file_1=open("new_rec.dat","wb")
    sno=input("ITEM CODE TO BE DELETED: ")
    try:
        while True:
            s=pickle.load(file)
            if (s[0]==sno):
                  found=True
            else:
                 pickle.dump(s,file_1)                     
                
    except EOFError:
            file.close()


    if (found==False):
          print("\nNO RECORD FOUND")
    else:
         print("\nRECORD FOUND AND DELETED")    
    file_1.close()
    os.remove("Menu.dat")
    os.rename("new_rec.dat","Menu.dat")
    
    
def update_menu():
    f=open("Menu.dat",'r+b')
    srno=input("ITEM CODE: ")
    pr=int(input("CHANGED PRICE: "))
    found=False
    try:
        while True:
            rpos=f.tell()
            
            s=pickle.load(f)
            if s[0]==srno:
                s[-1]=pr
                f.seek(rpos)
                pickle.dump(s,f)
                found= True
    except EOFError:
            f.close()
    if found==True:
            print("RECORD FOUND AND UPDATED")
    else:
            print("RECORD NOT FOUND")
        
def disp_customer_record():
    f=open("customer.csv",'r')
    re=csv.reader(f)
    print("                                                                      CUSTOMER RECORDS\n")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|ORDERNO |      NAME       |    PHNO    |       EMAIL         |    DATE     |   TIME    |                                ORDER                                                   |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    for s in re:
                if s[0]=='ORDER NO':
                        continue
                print(  "|",s[0]," "*(5-len(s[0])),
                        "|",s[1]," "*(14-len(s[1])),
                        "|",s[2]," "*(9-len(s[2])),
                        "|",s[3]," "*(18-len(s[3])),
                        "|",s[4]," "*(0-len(s[4])),
                        "|",s[5]," "*(3-len(s[5])),
                        "|",s[6]," "*(85-len(str(s[6]))),"|")
                print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")


    
    f.close()
    print()



def search_customer():
        f=open("customer.csv",'r')
        re=csv.reader(f)
        date=input('DATE : ')
        ord_no=int(input('ORDER NO: '))
        na=input('NAME: ')
        a=0
        for i in re:
                if i[0]==str(ord_no) and i[-3]==date and i[1]==na.upper():
                        print("\nRECORD FOUND")
                        print(i)
                        a=1
        if a==0:
                print("\nRECORD NOT FOUND")
                
def customer_delete():
        f=0
        list=[]
        ordno=input("ORDER NO TO BE DELETED: ")
        name=input("CUSTOMER NAME: ")
        date=input("DATE OF ORDER: ")

        file=open("customer.csv","r",newline="")
        file2=open("newcustomer.csv","a",newline="")

        re=csv.reader(file)
        wr=csv.writer(file2)
        for i in re:
                list.append(i)

        for reco in list:
                if(reco[0]==ordno and reco[1]==name and reco[-3]==date):
                        flag=1
                        
                else:
                       wr.writerow(reco)  

        if(flag==1):
                print("\nRECORD FOUND AND DELETED")
        else:
                print("\nNO SUCH RECORD FOUND !")
                       
        file.close()
        file2.close()
        os.remove("customer.csv")
        os.rename("newcustomer.csv","customer.csv")        

def staff_add():
        file=open("Staff_records.csv","a",newline="")
        staff_w=csv.writer(file)
        #staff_w.writerow(['EMP-ID','NAME','POST','DATE OF JOIN','SALARY','PHNO','ADDRESS'])
        name=input("EMPLOYEE NAME: ")
        emp_id=input("EMPLOYEE ID: ")
        post=input("EMPLOYEE POST: ")
        date_of_join=input("DATE OF JOIN: ")
        salary=input("EMPLOYEE SALARY")
        phno=input("EMPLOYEE PHONE NO: ")
        address=input("ADDRESS: ")
        rec=[emp_id,name,post,date_of_join,salary,phno,address]
        staff_w.writerow(rec)
        print("\nRECORD ADDED SUCCESSFULLY!")


def staff_modify_emp_id():
        flag=0
        staff_list=[]
        emp_id=input("EMPLOYEE ID TO BE UPDATED: ")

        file=open("Staff_records.csv","r",newline="")
        file2=open("new_Staff_records.csv","a",newline="")

        staff_r=csv.reader(file)
        staff_w=csv.writer(file2)
        for i in staff_r:
                staff_list.append(i)

        for reco in staff_list:
                if reco[0]==emp_id:
                        print("EMP-ID FOUND")
                        name=input("EMPLOYEE NAME: ")
                        post=input("EMPLOYEE POST: ")
                        date_of_join=input("DATE OF JOIN: ")
                        salary=input("EMPLOYEE SALARY")
                        phno=input("EMPLOYEE PHONE NO: ")
                        address=input("ADDRESS: ")
                        new=[emp_id, name,post,date_of_join,salary,phno,address]

                        staff_w.writerow(new)
                        flag=1
                else:
                        staff_w.writerow(reco)
        if (flag==1):
                print("\nRECORD FOUND AND UPDATED!")
        else:
                print("\nNO SUCH RECORD FOUND !")
                       
        file.close()
        file2.close()
        os.remove("Staff_records.csv")
        os.rename("new_Staff_records.csv","Staff_records.csv")


def staff_disp():
        file=open("Staff_records.csv","r")
        staff_r=csv.reader(file)
        print("+--------------------------------------------------------------------------------------------------------------------------------------------+")
        print("|EMP-ID |     EMP NAME    |     POST      |  DATE OF JOIN |  SALARY   |    PHNO     |        ADDRESS                                         |")
        print("+--------------------------------------------------------------------------------------------------------------------------------------------+")
        for s in staff_r:
                if s[0]=='EMP-ID':
                        continue
                print(  "|",s[0]," "*(3-len(s[0])),
                        "|",s[1]," "*(14-len(s[1])),
                        "|",s[2]," "*(12-len(s[2])),
                        "|",s[3]," "*(12-len(s[3])),
                        "|",s[4]," "*(8-len(s[4])),
                        "|",s[5]," "*(10-len(s[5])),
                        "|",s[6]," "*(53-len(str(s[6]))),"|")
                print("+--------------------------------------------------------------------------------------------------------------------------------------------+")

        file.close()

def staff_search():
        file=open("Staff_records.csv","r")
        emp_id=input("ENTER EMP-ID TO BE SEARCHED: ")
        staff_r=csv.reader(file)
        flag=0
        for rec in staff_r:
                if rec[0]==emp_id:
                        print("\nRECORD FOUND !")
                        print(rec)
                        flag=1
        if (flag==0):
                print("\nSORRY, RECORD NOT FOUND")

def staff_delete():
        flag=0
        staff_list=[]
        emp_id=input("EMPLOYEE ID TO BE DELETED: ")
        name=input("EMPLOYEE NAME: ")

        file=open("Staff_records.csv","r",newline="")
        file2=open("new_Staff_records.csv","a",newline="")

        staff_r=csv.reader(file)
        staff_w=csv.writer(file2)
        for i in staff_r:
                staff_list.append(i)

        for reco in staff_list:
                if(reco[0]!=emp_id and reco[1]!=name ):
                        flag=1
                        staff_w.writerow(reco)

        if(flag==1):
                print("RECORD FOUND AND DELETED")
        else:
                print("NO SUCH RECORD FOUND !")
                       
        file.close()
        file2.close()
        os.remove("Staff_records.csv")
        os.rename("new_Staff_records.csv","Staff_records.csv")

def refresh_order():
        flag=0
        order_list=[]
        print("TO REFRESH ORDER ENTER THE FOLLOWING DETAILS")
        ord_no=input("ORDER NO: ")
        name=input("CUSTOMER NAME: ")
        date=input("DATE OF ORDER: ")

        f1=open("customer.csv","r")
        f2=open("customer main.csv","w",newline='')

        order_r=csv.reader(f1)
        order_w=csv.writer(f2)

        for i in order_r:
                order_list.append(i)
        
        for j in order_list:
                if(j[0]==ord_no and j[1]==name and j[4]==date ):
                        print("RECORD FOUND\n",j)
                        z=order()
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        new=[j[0],j[1],j[2],j[3],j[4],current_time,z]
                        order_w.writerow(new)
                        flag=1
                else:
                        order_w.writerow(j)

        if (flag==1):
                print("YOUR ORDER HAS BEEN SUCCESSFULLY REFRESHED!")
        else:
                print("SORRY YOUR ORDER COULD NOT BE REFRSHED!")

        f1.close()
        f2.close()
        os.remove("customer.csv")
        os.rename("customer main.csv","customer.csv")
        os.remove("customer main.csv")
        
        



     
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#main
 
print("1.ORDER\n   ->PLACE ORDER\n   ->REFRESH ORDER\n   ->CANCEL ORDER\n")
print("2.MENU\n   ->ADD ITEM\n   ->DELETE ITEM\n   ->UPDATE MENU\n   ->DISPLAY MENU\n")
print("3.CUSTOMER\n   ->DISPLAY CUSTOMER RECORD\n   ->SEARCH CUSTOMER\n   ->DELETE CUSTOMER RECORD\n")
print("4.STAFF\n   ->DISPLAY STAFF RECORD\n   ->ADD STAFF RECORD\n   ->DELETE STAFF RECORD\n   ->UPDATE STAFF RECORD\n")
print("5.EXIT\n")

while True:
        
    ch=int(input("\nENTER CHOICE:"))

    if ch==1:
            x=1
            print("IS IT THE FIRST RECORD OF THE DAY: ")
            an=input("Y/N ")
            if an=='Y':
                 x=0
            elif an=='N':
                 dte=input("DATE: ")
                 f=open("customer.csv",'r')
                 re=csv.reader(f)
                 l=[]
                 for l in re:
                         if l[0]=='ORDER NO':
                                 continue
                         else:
                                 
                           if str(l[-3])==str(dte):
                        
                                   if x<int(l[0]):
                                        x=int(l[0])                            
                 f.close()
            print(x)
  
            while True:
                    
                print('\n1.PLACE ORDER\n2.REFRESH ORDER\n3.CANCEL ORDER\n4.EXIT ')
                cho=int(input("\nENTER SUB CHOICE:"))
                if cho==1:
                        invoice()
                elif cho==2:
                        refresh_order()
                elif cho==3:
                        customer_delete()
                elif cho==4:
                        break
                else:
                            print("INVALID ENTRY")
      

    elif ch==2:
            print("\n")
            password=input("\nENTER PASSWORD: ")
            if password=='dynamite7':
                while True:
                    print('\n1.ADD ITEM\n2.DELETE ITEM\n3.UPDATE MENU\n4.DISPLAY MENU\n5.EXIT')
                    cho=int(input("\nENTER SUB CHOICE:")) 
                    if cho==1:
                            menu_add()
                    elif cho==2:
                            del_menu()
                    elif cho==3:
                            update_menu()
                    elif cho==4:
                            display_menu()
                    elif cho==5:
                            break
                    else:
                            print("INVALID ENTRY") 
        
    elif ch==3:
            pas=input("\nENTER PASSWORD: ")
            if pas=='dynamite7':
                    while True:
                            
                        print('\n1.DISPLAY CUSTOMER RECORD\n2.SEARCH CUSTOMER\n3.DELETE CUSTOMER RECORD\n4.EXIT')
                        cho=int(input("ENTER SUB CHOICE:"))
                        if cho==1:
                                disp_customer_record()
                        elif cho==2:
                                search_customer()
                        elif cho==3:
                                customer_delete() 
                        elif cho==4:
                                break
                        else:
                                print("INVALID ENTRY")
                            
            else:
                    print("AUTHORISED PERSONNEL ONLY!!")
            


    elif ch==4:
            pas=input("\nENTER PASSWORD: ")
            if pas=='dynamite7':
                while True:
                        print("\n1.DISPLAY STAFF RECORD\n2.ADD STAFF RECORD\n3.DELETE STAFF RECORD\n4.UPDATE STAFF RECORD\n5.EXIT")
                        cho=int(input("\nENTER SUB CHOICE:"))
                        if cho==1:
                                staff_disp()
                        elif cho==2:
                                staff_add()
                        elif cho==3:
                                staff_delete()
                        elif cho==4:
                                staff_modify_emp_id()
                        elif cho==5:
                                break
                        else:
                                print("INVALID ENTRY")
            
    elif ch==5:
            break
    else:
            print("INVALID CHOICE")
