import csv
def search_customer():
        f=open("customer.csv",'r')
        re=csv.reader(f)
        date=input('DATE : ')
        ord_no=int(input('ORDER NO: '))
        na=input('NAME: ')
        for i in re:
                if i[0]==str(ord_no) and i[-3]==date and i[1]==na.upper():
                        print(i)
                        
search_customer()
