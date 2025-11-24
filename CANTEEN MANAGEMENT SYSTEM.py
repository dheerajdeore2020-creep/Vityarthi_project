#CANTEEN MANAGEMENT SYSTEM----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost', user='root', password='tr!angulum3', database='canteen')
    mycursor=mydb.cursor()
except MySQLError:
    print("\nPlease check MYSQL connectivity !")
'''try:
    mycursor.execute("use PROJECT2025")
except:
    pass
'''

#INSTALLMENT------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tables():
    mycursor.execute('create table product(p_id int primary key, p_name varchar(45), p_company varchar(45), p_price float, p_qty int, p_discount float, p_rate float, p_purchasedate date')
    myscursor.execute('create table customer(cust_id int primary key, cust_name varchar(40), address varchar(50), phone char(10))')
    mycursor.execute('create table purchase(cust_id int, cust_name varchar(40), p_id int, p_name varchar(45), p_company varchar(30), rate float, quantity int, amount float, sale_date date)')

#PRODUCTS MENU STARTS---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_rec():
    while True:
        try:
            prod_id=int(input("PRODUCT ID: "))
            prod_name=input("NAME OF PRODUCT: ")
            prod_company=input("NAME OF PRODUCT COMPANY: ")
            prod_price=float(input("PER UNIT PRODUCT PRICE: "))
            prod_quan=int(input("PRODUCT QUANTITY: "))
            prod_discount=float(input("PRODUCT DISCOUNT: "))
            prod_rate=float(input("PRODUCT SELLING RATE: "))
            prod_date=input("PRODUCT PURCHASE DATE (yyyy-mm-dd): ")
            prod_payment=input("Is the outstanding payment made? (Yes/No): ")
            if prod_payment.upper()=="NO":
                amount_left=int(input("Enter the due amount for product purchase: "))
            else:
                amount_left=0
        except ValueError:
            print("Incorrect value entered!")
        else:
            data1=(prod_id, prod_date, prod_payment, amount_left)
            data=(prod_id, prod_name, prod_company, prod_price, prod_quan, prod_discount, prod_date)
            sql1='insert into product_report values(%s,%s,%s,%s)'
            sql='insert into product values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(sql,data)
            mycursor.execute(sql1,data1)
            mydb.commit()
            opt=input("Do you want to enter more data?(y/n): ")
            if opt=="n":
                exit
            print("\nRecord added !!")

def display_rec():
    d={}
    j=1
    try:
        mycursor.execute("select * from product")
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<15} {:<14} {:<14} {:<15}".format(a, b, c, h, e, f, str(g)))
    except:
        print("Error encountered in displaying record from table!")

def search_rec():
    d={}
    j=1
    try:
        id=int(input("Enter the product id:"))
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
    except:
        print("Error encountered in displaying record from table!")

def modify_rec():
    ch=0
    while ch!=7:
        print("="*30+"MODIFY PRODUCT-RECORD MENU"+"="*30)
        print("1. MODIFY PRODUCT NAME")
        print("2. MODIFY PRODUCT COMPANY")
        print("3. MODIFY PRODUCT PRICE")
        print("4. MODIFY PRODUCT QUANTITY")
        print("5. MODIFY PRODUCT DISCOUNT")
        print("6. MODIFY PRODUCT PURCHASE DATE")
        print("7. BACK TO PRODUCT MENU")
        print("="*86)
        ch=int(input("Enter your choice (1-7):"))
        if ch==1:
            prod_name()
        elif ch==2:
            prod_comp()
        elif ch==3:
            prod_price()
        elif ch==4:
            prod_quan()
        elif ch==5:
            prod_disc()
        elif ch==6:
            prod_purchase()
        elif ch==7:
            exit
        else:
            print("Incorrect choice! Please enter again!")

def prod_name():
    try:
        id=int(input("Enter the product id:"))
        pname=input("Enter the new product name:")
    except  ValueError:
        print("Incorrect value entered!")
    else:
        query="Update product set p_name=%s where p_id=%s"
        mycursor.execute(query,(pname, id))
        mydb.commit()
        print("\nThe modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        
        
def prod_comp():
    try:
        id=int(input("Enter the product id:"))
        pcomp=input("Enter the new product company:")
    except ValueError:
        print("Incorrect value entered!")
    else:
        query="Update product set p_company=%s where p_id=%s"
        mycursor.execute(query, (pcomp, id))
        mydb.commit()
        print("\nThe modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        

def prod_price():
    try:
        id=int(input("Enter the product id:"))
        pprice=input("Enter the new product quantity:")
    except ValueError:
        print("Incorrect value entered!")
    else:
        query="Update product set p_price=%s where p_id=%s"
        mycursor.execute(query, (pprice, id))
        mydb.commit()
        print("\nThe modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        

def prod_quan():
    try:
        id=int(input("Enter the product id:"))
        pquan=input("Enter the new product quantity:")
    except ValueError:
        print("Incorrect value entered!")
    else:
        query="Update product set p_qty=%s where p_id=%s"
        mycursor.execute(query, (pquan, id))
        mydb.commit()
        print("\nThe modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        

def prod_disc():
    try:
        id=int(input("Enter the product id:"))
        pdisc=input("Enter the new product discount:")
    except ValueError:
        print("Incorrect value entered!")
    else:
        query="Update product set p_discount=%s where p_id=%s"
        mycursor.execute(query, (pdisc, id))
        mydb.commit()
        print("\nThe modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        
        
def prod_purchase():
    try:
        id=int(input("Enter the product id:"))
        ppurchase=input("Enter the new product purchase date (yyyy-mm-dd):")
    except ValueError:
        print("\nIncorrect value entered!")
    else:
        query="Update product set p_purchasedate=%s where p_id=%s"
        mycursor.execute(query, (ppurchase, id))
        mydb.commit()
        print("The modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product where p_id="+str(id))
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        
        
def delete_rec():
    try:
        id=int(input("Enter the product id:"))
    except ValueError:
        print("Incorrect value entered!")
    else:
        mycursor.execute("DELETE from product where p_id="+str(id))
        print("\nThe modified data is:")
        d={}
        j=1
        mycursor.execute("select * from product")
        dt=["PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "PURCHASE DATE"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7]]
            d[j]=data
            j+=1
        print ("{:<15} {:<15} {:<18} {:<22} {:<15} {:<15} {:<15} {:<15}".format("PRODUCT ID", "PRODUCT NAME", "PRODUCT COMPANY", "PRODUCT PRICE(PER UNIT)", "QUANTITY", "DISCOUNT", "RATE", "PURCHASE DATE"))    
        for k, v in d.items():
            a, b, c, h, e, f, g=v
            print("{:<15} {:<15} {:<18} {:<24} {:<18} {:<15} {:<15} {:<15}".format(a, b, c, h, e, f, str(g)))
        


def prod_menu():
    ch=0
    while ch!=6:
        print("="*30+"PRODUCT MENU"+"="*30)
        print("1. CREATE PRODUCT")
        print("2. DISPLAY ALL PRODUCTS AVAILABLE")
        print("3. SEARCH DESIRED RECORD")
        print("4. MODIFY PRODUCT RECORD")
        print("5. DELETE PRODUCT RECORD")
        print("6. BACK TO ADMINISTRATOR MENU")
        print("="*73)
        ch=int(input("Enter your choice (1-7):"))
        if ch==1:
            create_rec()
        elif ch==2:
            display_rec()
        elif ch==3:
            search_rec()
        elif ch==4:
            modify_rec()
        elif ch==5:
            delete_rec()
        elif ch==6:
            exit
        else:
            print("Incorrect choice! Please enter again!")


#CUSTOMER MENU STARTS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_record():
    while True:
        try:
            custid=int(input("Enter CUSTOMER ID: "))
            custname=input("Enter CUSTOMER NAME: ")
            address=input("Enter CUSTOMER ADDRESS: ")
            phone=input("Enter CUSTOMER PHONE NO.: ")
        except ValueError:
            print("Incorrect value entered!")
        else:
            data=(custid, custname, address, phone)
            query='insert into customer values(%s,%s,%s,%s)'
            mycursor.execute(query, data)
            mydb.commit()
            more=input('Do you want to add more records? (y/n): ')
            if more in 'nN':
                break
            print('\nRecord added!')

def display_record():
    d={}
    j=1
    try:
        mycursor.execute('select * from customer')
        print()
        dt=['CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.']
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<44} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.'))
        for k, v in d.items():
            a, b, c, e=v
            print('{:<15} {:<22} {:<44} {:<15}'.format(a, b, c, e))
    except:
         print("Error encountered in displaying record from table!")

def search_record():
    d={}
    j=1
    try:
        key=input("Enter Customer ID to search for the record: ")
        query='select * from customer where cust_id=%s'
        mycursor.execute(query, (key,))
        print()
        dt=['CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.']
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<44} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.'))
        for k, v in d.items():
            a, b, c, e=v
            print('{:<15} {:<22} {:<44} {:<15}'.format(a, b, c, e))
    except:
         print("Error encountered in displaying record from table!")

def modify_record():
    while True:
        print('/N'+'='*30+'CUSTOMER RECORD MODIFICATION'+'='*30)
        print('1. MODIFY CUSTOMER NAME')
        print('2. MODIFY CUSTOMER ADDRESS')
        print('3. MODIFY CUSTOMER PHONE NO.')
        print('0. BACK TO CUSTOMER MENU')
        ch=input('\nEnter the choice to proceed (1/2/3/0): ')
        if ch=='1':
            cust_name()
        elif ch=='2':
            cust_address()
        elif ch=='3':
            cust_phone()
        elif ch=='0':
            break
        else:
            print('Invalid choice! Please enter again!')

def cust_name():
    try:
        cid=input('\nEnter Customer ID for the record to be modified: ')
        cname=input('Enter the New Customer name: ')
    except ValueError:
        print("Incorrect value entered!")
    else:
        query='update customer set cust_name=%s where cust_id=%s'
        data=(cname, cid)
        mycursor.execute(query, data)
        print('\nThe modified data is:')
        d={}
        j=1
        mycursor.execute('select * from customer where cust_id='+cid)
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<44} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.'))
        for k, v in d.items():
            a, b, c, e=v
            print('{:<15} {:<22} {:<44} {:<15}'.format(a, b, c, e))

def cust_address():
    try:
        cid=input('\nEnter Customer ID for the record to be modified: ')
        add=input('Enter the Updated Address: ')
    except ValueError:
        print("Incorrect value entered!")
    else:
        query='update customer set address=%s where cust_id=%s'
        data=(add, cid)
        mycursor.execute(query, data)
        print('\nThe modified data is:')
        d={}
        j=1
        mycursor.execute('select * from customer where cust_id='+cid)
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<44} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.'))
        for k, v in d.items():
            a, b, c, e=v
            print('{:<15} {:<22} {:<44} {:<15}'.format(a, b, c, e))

def cust_phone():
    try:
        cid=input('\nEnter Customer ID for the record to be modified: ')
        phn=input('Enter the Updated Phone no.: ')
    except ValueError:
        print("Incorrect value entered")
    else:
        query='update customer set phone=%s where cust_id=%s'
        data=(phn, cid)
        mycursor.execute(query, data)
        print('\nThe modified data is:')
        d={}
        j=1
        mycursor.execute('select * from customer where cust_id='+cid)
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<44} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.'))
        for k, v in d.items():
            a, b, c, e=v
            print('{:<15} {:<22} {:<44} {:<15}'.format(a, b, c, e))

def delete_record():
    try:
        cid=input('\nEnter Customer ID for the record to be deleted: ')
    except ValueError:
        print("Incorrect value entered!")
    else:
        query='delete from customer where cust_id=%s'
        mycursor.execute(query, (cid,))
        print('\nThe updated data is:')
        d={}
        j=1
        mycursor.execute('select * from customer')
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<44} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'CUSTOMER ADDRESS', 'PHONE NO.'))
        for k, v in d.items():
            a, b, c, e=v
            print('{:<15} {:<22} {:<44} {:<15}'.format(a, b, c, e))

def cust_menu():
    while True:
        print()
        print('='*30+'CUSTOMER MENU'+'='*30)
        print('\n1. Create record')
        print('2. Display record')
        print('3. Search record')
        print('4. Modify record')
        print('5. Delete record')
        print('0. Back to administrator menu')
        print(25*'*  ')
        ch=input('\nEnter your choice (1/2/3/4/5/0): ')
        if ch=='1':
            create_record()
        elif ch=='2':
            display_record()
        elif ch=='3':
            search_record()
        elif ch=='4':
            modify_record()
        elif ch=='5':
            delete_record()
        elif ch=='0':
            break
        else:
            print("Incorrect choice! Please enter again!")


#ADMIN MENU STARTS------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin():
    while True:
        print("="*30+"ADMINISTRATOR MENU"+"="*30)
        print("1. CUSTOMERS MENU")
        print("2. PRODUCTS MENU")
        print("3. CANTEEN SALE MENU")
        print("4. BACK TO MAIN MENU")
        print("="*73)
        ch=int(input("Enter your choice (1-7):"))
        if ch==1:
            cust_menu()
        elif ch==2:
            prod_menu()
        elif ch==3:
            cant_sales()
        elif ch==4:
            exit
        else:
            print("Incorrect choice! Please enter again!")


#PRODUCT REPORT GENERATOR STARTS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def prod_report():
    d={}
    j=1
    try:
        mycursor.execute("select * from product_report")
        dt=["PRODUCT ID", "PURCHASE DATE", "PRODUCT PAYMENT STATUS", "DUE AMOUNT"]
        for i in mycursor:
            data = [i[0], i[1], i[2], i[3]]
            d[j]=data
            j+=1
        print ("{:<15} {:<18} {:<18} {:<22}".format("PRODUCT ID", "PURCHASE DATE", "PAYMENT STATUS", "DUE AMOUNT"))    
        for k, v in d.items():
            a, b, c, h =v
            print("{:<15} {:<18} {:<18} {:<22}".format(a, str(b), c, h))
    except:
        print("Error encountered in displaying record from table!")



#MAIN MENU STARTS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():
    while True:
        print("="*30+"MAIN MENU"+"="*30)
        print("1. PRODUCTS REPORT GENERATOR")
        print("2. ADMINISTRATOR")
        print("3. EXIT")
        print("="*73)
        ch=int(input("Enter your choice (1-3):"))
        if ch==1:
            prod_report()
        elif ch==2:
            admin()
        elif ch==3:
            exit
        else:
            print("Incorrect choice! Please enter again!")
#main_menu()


#CANTEEN SALES MENU STARTS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_purchase():
    while True:
        try:
            c_id=int(input('Enter CUSTOMER ID: '))
            p_id=int(input('Enter PRODUCT ID: '))
            qty=int(input('Enter QUANTITY PURCHASED: '))
        except ValueError:
            print('Incorrect value entered!')
        else:
            query1='insert into purchase select cust_id, cust_name, p_id, p_name, p_company, rate, {0}, rate*{0} as amount, curdate() from customer natural join product where cust_id={1} and p_id={2}'.format(qty, c_id, p_id)
            mycursor.execute(query1)
            query2='update product set p_qty=p_qty-%s where p_id=%s' % (qty, p_id)
            mycursor.execute(query2)
            mydb.commit()
            ch=input('Do you want to add more records? (y/n): ')
            if ch in 'nN':
                break
            print('\nRecord added!')

def del_purchase():
    try:
        c_id=int(input('Enter CUSTOMER ID: '))
        p_id=int(input('Enter PRODUCT ID: '))
        date=input('Enter DATE OF PURCHASE (yyyy-mm-dd): ')
    except ValueError:
        print("Incorrect value entered!")
    else:
        query='delete from purchase where cust_id=%s and p_id=%s and sale_date=%s'
        mycursor.execute(query, (c_id, p_id, date))
        mydb.commit()
        print('\nThe updated data is:')
        d={}
        j=1
        mycursor.execute('select * from purchase')
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            d[j]=data
            j+=1
        print('{:<13} {:<20} {:<13} {:<20} {:<20} {:<10} {:<10} {:<10} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'PRODUCT ID', 'PRODUCT NAME', 'PRODUCT COMPANY', 'RATE', 'QUANTITY', 'AMOUNT', 'DATE'))
        for k, v in d.items():
            a, b, c, e, f, g, h, l, m=v
            print('{:<13} {:<20} {:<13} {:<20} {:<20} {:<10} {:<10} {:<10} {:<15}'.format(a, b, c, e, f, g, h, l, m))


def purch_qty():
    try:
        c_id=int(input('Enter CUSTOMER ID: '))
        p_id=int(input('Enter PRODUCT ID: '))
        qty=int(input('Enter UPDATED QUANTITY: '))
        date=input('Enter DATE OF PURCHASE (yyyy-mm-dd): ')
    except ValueError:
        print("Incorrect value entered!")
    else:
        #update qty in purchase table
        data=(qty, c_id, p_id, date)
        query='update purchase set quantity=%s where c_id=%s and p_id=%s and date=%s'
        mycursor.execute(query, data)
        mydb.commit()
        
        print('\nThe updated data is:')
        d={}
        j=1
        mycursor.execute('select * from purchase')
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            d[j]=data
            j+=1
        print('{:<15} {:<22} {:<15} {:<20} {:<20} {:<10} {:<10} {:<10} {:<15}'.format('CUSTOMER ID', 'CUSTOMER NAME', 'PRODUCT ID', 'PRODUCT NAME', 'PRODUCT COMPANY', 'RATE', 'QUANTITY', 'AMOUNT', 'DATE'))
        for k, v in d.items():
            a, b, c, e, f, g, h, l, m=v
            print('{:<15} {:<22} {:<15} {:<20} {:<20} {:<10} {:<10} {:<10} {:<15}'.format(a, b, c, e, f, g, h, l, m))
                
        #update qty in product table
        mycursor.execute('select quantity from purchase where p_id='+str(p_id)+' and cust_id='+str(c_id)+' and date='+str(date))
        quan=mycursor.fetchone()[0]
        data1=(quan-qty, c_id, p_id, date)
        query1='update product set p_qty=p_qty+%s where c_id=%s and p_id=%s and date=%s'
        mycursor.execute(query1, data1)
        mydb.commit()
        

def cant_sales():
    while True:
        print(25*'='+'CANTEEN SALES MENU'+25*'=')
        print('\n1. ADD CUSTOMER PURCHASE')
        print('2. MODIFY PURCHASE QUANTITY')
        print('3. DELETE CUSTOMER PURCHASE')
        print('0. BACK TO ADMIN MENU')
        print(73*'=')
        ch=input('Enter your choice (1/2/3/0): ')
        if ch=='1':
            add_purchase()
        elif ch=='2':
            purch_qty()
        elif ch=='3':
            del_purchase()
        elif ch=='0':
            break
        else:
            print("Incorrect choice! Please enter again!")


#CUSTOMER PRODUCT MENU STARTS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cust_prod():
    while True:
        print(25*'='+'CUSTOMER PRODUCT MENU'+25*'=')
        print('\n1. CUSTOMER MENU')
        print('2. PRODUCT MENU')
        print('3. CANTEEN SALES MENU')
        print('0. BACK TO ADMIN MENU')
        print(73*'=')
        ch=input('Enter your choice (1/2/3/0): ')
        if ch=='1':
            cust_menu()
        elif ch=='2':
            prod_menu()
        elif ch=='3':
            cant_sales()
        elif ch=='0':
            break
        else:
            print("Incorrect choice! Please enter again!")


#INVOICE GENERATOR------------------------------------------------------------------------------------------------------------------------------------------------------------
def invoice():
    while True:
        cust_id=int(input('\nEnter CUSTOMER ID: '))
        date=input('Enter DATE OF PURCHASE (yyyy-mm-dd): ')
        print()
        print('INVOICE'.center(100))
        #print(f"{'INVOICE':^100}")
        cust='select cust_name, phone from customer where cust_id=%s' % (cust_id,)
        mycursor.execute(cust)
        l=[]
        for i in mycursor:
            for j in i:
                l.append(j)
        print('Customer ID :', cust_id, f"{'Date : '+date :^100}")
        print('Customer Name :', l[0])
        print('Customer Phone No. :', l[1])
        print()
        d={}
        j=1
        query='select p_id, p_name, p_company, rate, quantity, amount from purchase where cust_id=%s and sale_date=%s'
        data=(cust_id, date)
        mycursor.execute(query, data)
        for i in mycursor:
            data=[i[0], i[1], i[2], i[3], i[4], i[5]]
            d[j]=data
            j+=1
        print('{:<13} {:<20} {:<20} {:<10} {:<10} {:<10}'.format('PRODUCT ID', 'PRODUCT NAME', 'PRODUCT COMPANY', 'RATE', 'QUANTITY', 'AMOUNT'))
        for k, v in d.items():
            a, b, c, e, f, g=v
            print('{:<13} {:<20} {:<20} {:<10} {:<10} {:<10} '.format(a, b, c, e, f, g))
            
        q='select sum(amount) from purchase where cust_id=%s and sale_date=%s'
        mycursor.execute(q, (cust_id, date))
        total=mycursor.fetchone()[0]
        
        print('{:<13} {:<20} {:<20} {:<10} {:<10} {:<10}'.format('','','','','TOTAL',total))
        
        ch=input('\nWant to generate another invoice? (y/n): ')
        if ch in 'nN':
            break

invoice()
