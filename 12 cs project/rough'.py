from datetime import date,datetime
import csv
dte= date.today()
d=input('date: ')
if d==str(dte):
        print("ok")
        f=open("customer.csv",'r')
        re=csv.reader(f)
        for i in re:
                print(i)
                if i[-3]==str(dte):
                        print('aaa')
