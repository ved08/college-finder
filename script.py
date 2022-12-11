import mysql.connector as sql
mycon=sql.connect(host='localhost',user='ved08',passwd='ved08',database='colleges')           #connectivity established
cur=mycon.cursor()                                                                            #cursor instance created

print('\nWELCOME TO THE COLLEGE FINDER PROGRAM! \n----------------------------------------\n')
print('Select the course you are looking for from the index below\nand type the associated number.\n\n----------------------------------------\n')
print('''Enter 1 \nfor Bachelor of Science (B.Sc)

Enter 2 \nfor Bachelor of Technology (B.Tech)

Enter 3 \nfor Bachelor of Arts (B.A)

Enter 4 \nfor Bachelor of Medicine & Bachelor of Surgery (MBBS)

Enter 5 \nfor Bachelor of Commerce (B.Com)

Enter 6 \nfor Bachelor of Design (B.Des)

Enter 7 \nfor Bachelor of Fine Arts (B.F.A)

Enter 8 \nfor Bachelor of Business Administration (B.B.A)

Enter 9 \nfor Bachelor of Architecture (B.Arch)

Enter 10 \nfor Chartered Accountancy (CA)  ''')
    
course=int(input('\nEnter course number:'))
