import mysql.connector


con=mysql.connector.connect(host="localhost",user="root",password="")

#CREATING DATABASE AND TABLE
cursor = con.cursor()
query1 = "create database if not exists store"
query2 = "use store"
query3 = "create table if not exists signup(username varchar(20),password varchar(20))"
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
while True:
    print("""1:Signup
2:Login""")

    ch=int(input("SIGNUP/LOGIN(1,2):"))

#SIGNUP
    if ch==1:

        username=input("USERNAME:")
        pw=input("PASSWORD:")

        query4 = "insert into signup values('"+username+"','"+pw+"')"
        cursor.execute(query4)
       
#LOGIN
    elif ch==2:

        username=input("USERNAME:")
        query5 = "select username from signup where username='"+username+"'"
        cursor.execute(query5)
        pot=cursor.fetchone()

        if pot is not None:
            print("VALID USERNAME!!!!!!")

            pw=input("PASSWORD:")

            cursor.execute("select password from signup where password='"+pw+"'")
            a=cursor.fetchone()

            if a is not None:
                print("""+++++++++++++++++++++++
+++LOGIN SUCCESSFULL+++
+++++++++++++++++++++++""")

                print("""======================================================================
++++++++++++++++++++++++++    X.Y.Z SHOP.     +++++++++++++++++++++++++
==========================================================================""")

                query6 = "create table if not exists Available_Products(ProductName varchar(30) primary key,type varchar(20),Quantity int(3),Company varchar(20),Specify varchar(30),Price int(4))"
                cursor.execute(query6)
                cursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, ProductName varchar(30),Quantity int(100),Price int(4),foreign key (ProductName) references Available_Products(ProductName))")
                cursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10) unique key , Address varchar(40))") 
                cursor.close()
                while(True):
                    print("""1:Add Stock
2:Delete Stock
3:Search Stock
4:Staff Details
5:Sell Record
6:Available Stock
7:Total Income after the Latest Reset 
8:Exit""")

                    a=int(input("Enter your choice:"))

    #ADD PRODUCTS
                    if a==1:

                        print("All information prompted are mandatory to be filled")
                    
                        Product=str(input("Enter Product Name:"))
                        type=str(input("type:"))
                        quantity=int(input("Enter quantity:"))        
                        Company=str(input("Enter company name:"))
                        Specify=str(input("Specify:"))
                        price=int(input("Enter the price:"))

                        cursor.execute("select * from Available_Product where Productname='"+Product+"'")
                        row=cursor.fetchone()

                        if row is not None:
                            cursor.execute("update Available_Product set quantity=quantity+'"+str(quantity)+"' where Productname='"+Product+"'")
                            cursor.close()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")
                        
                        
                        else:
                            cursor.execute("insert into Available_Products(Productname,type,quantity,Company,publication,price) values('"+Product+"','"+type+"','"+str(quantity)+"','"+Company+"','"+publication+"','"+str(price)+"')")
                            cursor.close()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""") 
                   

    #DELETE PRODUCTS
                    elif a==2:                

                        print("AVAILABLE PRODUCTS...")

                        cursor.execute("select * from Available_Product")
                        for x in cursor:
                            print(x)
                      
                        cusname=str(input("Enter customer name:"))
                        phno=int(input("Enter phone number:"))
                        Product=str(input("Enter Product Name:"))
                        price=int(input("Enter the price:"))
                        n=int(input("Enter quantity:"))

                        cursor.execute("select quantity from available_Product where Productname='"+Product+"'")
                        lk=cursor.fetchone()

                        if max(lk)<n:
                            print(n,"Product is not available!!!!")

                        else:
                            cursor.execute("select Productname from available_Product where Productname='"+Product+"'")
                            log=cursor.fetchone() 

                            if log is not None:
                                cursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+Product+"','"+str(n)+"','"+str(price)+"')")
                                cursor.execute("update Available_Product set quantity=quantity-'"+str(n)+"' where ProductName='"+Product+"'")
                                cursor.close()

                                print("""++++++++++++++++++++++
++PRODUCT HAS BEEN SOLD++
++++++++++++++++++++++""")

                            else:
                                print("PRODUCT IS NOT AVAILABLE!!!!!!!")

    #SEARCH PRODUCT ON THE BASIS OF GIVEN OPTIONS
                    elif a==3:

                        print("""1:Search by name
2:Search by type
3:Search by Company""")

                        l=int(input("Search by?:"))

        #BY PRODUCT NAME
                        if l==1:
                            o=input("Enter Product to search:")

                            cursor.execute("select Productname from available_Product where Productname='"+o+"'")
                            tree=cursor.fetchone()

                            if tree!=None:
                                print("""++++++++++++++++++++
++PRODUCT IS IN STOCK++
++++++++++++++++++++""")

                            else:
                                print("PRODUCT IS NOT IN STOCK!!!!!!!")

        #BY TYPE
                        elif l==2:
                            g=input("Enter type to search:")

                            cursor.execute("select type from available_Product where type='"+g+"'")
                            poll=cursor.fetchall()

                            if poll is not None:
                                print("""++++++++++++++++++++
++PRODUCT IS IN STOCK++
++++++++++++++++++++""")

                                cursor.execute("select * from available_Product where type='"+g+"'")

                                for y in cursor:
                                    print(y)

                            else:
                                print("PRODUCT OF SUCH type ARE NOT AVAILABLE!!!!!!!!!")


        #BY COMPANY NAME
                        elif l==3:
                            au=input("Enter Company to search:")

                            cursor.execute("select Company from available_Product where Company='"+au+"'")
                            home=cursor.fetchall()

                            if home is not None:
                                print("""++++++++++++++++++++
++PRODUCT IS IN STOCK++
++++++++++++++++++++""")

                                cursor.execute("select * from available_Product where Company='"+au+"'")

                                for z in cursor:
                                    print(z)

                            else:
                                print("PRODUCT OF THIS Company ARE NOT AVAILABLE!!!!!!!")
                        cursor.close()

    #STAFF DETAILS
                    elif a==4:
                        print("1:New staff entry")
                        print("2:Remove staff")
                        print("3:Existing staff details")

                        ch=int(input("Enter your choice:"))

        #NEW STAFF ENTRY
                        if ch==1:
                            fname=str(input("Enter Fullname:"))
                            gender=str(input("Gender(M/F/O):"))
                            age=int(input("Age:"))
                            phno=int(input("Staff phone no.:"))
                            add=str(input("Address:"))

                            cursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
                            print("""+++++++++++++++++++++++++++++
+STAFF IS SUCCESSFULLY ADDED+
+++++++++++++++++++++++++++++""")
                            cursor.close()

        #REMOVE STAFF
                        elif ch==2:
                            nm=str(input("Enter staff name to remove:"))
                            cursor.execute("select name from staff_details where name='"+nm+"'")
                            toy=cursor.fetchone()

                            if toy is not None:
                                cursor.execute("delete from staff_details where name='"+nm+"'")
                                print("""+++++++++++++++++++++++++++++++++
++STAFF IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
                                cursor.close()

                            else:
                                print("STAFF DOESNOT EXIST!!!!!!")

        #EXISTING STAFF DETAILS
                        elif ch==3:
                            cursor.execute("select * from Staff_details")
                            run=cursor.fetchone()
                            for t in cursor:
                                print(t)
                            if run is not None:
                                print("EXISTING STAFF DETAILS...")                        
                                for t in cursor:
                                    print(t)

                            else:
                                print("NO STAFF EXISTS!!!!!!!")
                            cursor.close()

    #SELL HISTORY                                
                    elif a==5:
                        print("1:Sell history details")
                        print("2:Reset Sell history")

                        ty=int(input("Enter your choice:"))

                        if ty==1:
                            cursor.execute("select * from sell_rec")
                            for u in cursor:
                                print(u)

                        if ty==2:
                            bb=input("Are you sure(Y/N):")

                            if bb=="Y":
                                cursor.execute("delete from sell_rec")
                                cursor.close()

                            elif bb=="N":
                                pass

    #AVAILABLE PRODUCTS
                    elif a==6:
                        cursor.execute("select * from available_Product order by productname")
                        for v in cursor:
                            print(v)

    #TOTAL INCOME AFTER LATEST UPDATE
                    elif a==7:
                        cursor.execute("select sum(price) from sell_rec")
                        for x in cursor:
                            print(x)
    #EXIT                    
                    elif a==8:
                        break

#LOGIN ELSE PART
            else:
                print("""++++++++++++++++++++++
++INCORRECT PASSWORD++
++++++++++++++++++++++""")


        else:
            print("""++++++++++++++++++++
++INVALID USERNAME++
++++++++++++++++++++""")

    else:
        break
