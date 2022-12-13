import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='ved08',database='colleges')           #connectivity established
cur=mycon.cursor()                                                                            #cursor instance created
           
print('''
WELCOME TO THE COLLEGE FINDER PROGRAM!
----------------------------------------
Search for the course you want to study from the index below
and type the associated number.
\n--------------------------------------------------------------------------------\n''')


#COURSES


print('''Enter 1 \n  for Bachelor of Science (B.Sc)\n
Enter 2 \n  for Bachelor of Technology (B.Tech)\n
Enter 3 \n  for Bachelor of Arts (B.A)\n
Enter 4 \n  for Bachelor of Medicine & Bachelor of Surgery (MBBS)\n
Enter 5 \n  for Bachelor of Commerce (B.Com)\n
Enter 6 \n  for Bachelor of Design (B.Des)\n
Enter 7 \n  for Bachelor of Fine Arts (B.F.A)\n
Enter 8 \n  for Bachelor of Business Administration (B.B.A)\n
Enter 9 \n  for Bachelor of Architecture (B.Arch)\n
Enter 10 \n  for Chartered Accountancy (C.A)  ''')   
course=int(input('\nEnter course number:'))

coursedict={1:'B.Sc',
            2:'B.Tech',
            3:'B.A',
            4:'MBBS',
            5:'B.Com',
            6:'B.Des',
            7:'B.F.A',
            8:'B.B.A',
            9:'B.Arch',
            0:'C.A'}


#CITIES


print('''\n--------------------------------------------------------------------------------\n
Search for your preferred city from the index below
and type the associated number.
\n--------------------------------------------------------------------------------\n''')
print('''Enter 1 \n  for Bangalore\n
Enter 2 \n  for Chennai\n
Enter 3 \n  for Delhi\n
Enter 4 \n  for Hyderabad\n
Enter 5 \n  for Indore\n
Enter 6 \n  for Jaipur\n
Enter 7 \n  for Kharagpur\n
Enter 8 \n  for Kolkata\n
Enter 9 \n  for Manipal\n
Enter 10 \n  for Mumbai\n
Enter 11 \n  for Pune\n
Enter 12 \n  for Varanasi\n
Enter 13 \n  for Vellore\n
Enter 0 \n  TO SKIP QUESTION\n''')

city=int(input('\nEnter city number:'))

citydict={
    1:'Bangalore',
    2:'Chennai',
    3:'Delhi',
    4:'Hyderabad',
    5:'Indore',
    6:'Jaipur',
    7:'Kharagpur',
    8:'Kolkata',
    9:'Manipal',
    10:'Mumbai',
    11:'Pune',
    12:'Varanasi',
    13:'Vellore',
    0:'%'
}


#FEE RANGE


print('''\n--------------------------------------------------------------------------------\n
What is your ideal fee range? Browse in the index below
and type the associated number.
*Don't worry, there will be scholarship websites provided for each result later!*
\n--------------------------------------------------------------------------------\n''')
print('''Enter 1 \n   for <1 Lakhs P.A.\n
Enter 2 \n  for <5 Lakhs P.A.\n
Enter 3 \n  for <10 Lakhs P.A.\n
Enter 4 \n  for <20 Lakhs P.A.\n
Enter 5 \n  for >20 Lakhs P.A.\n
Enter 0 \n  TO SKIP QUESTION\n''')

fee=int(input('\nEnter fee range number:'))
if fee == 0:
    fee = 5

#PERCENTAGE IN CLASS 12


print('''\n--------------------------------------------------------------------------------\n
What was your percentage scored in Class 12 Final Exams (or equivalent)?
Type the numeric value ONLY.
Example:
Enter Class 12 percentage: 80
\n--------------------------------------------------------------------------------\n''')

percentage=int(input('\nEnter Class 12 percentage:'))


#CREATING THE QUERY WITH PARAMETERISED VALUES AND EXTRACTING DATA


values=(coursedict.get(course),citydict.get(city),fee,percentage)
print(values)

query='select * from colleges where Course like "%{}%" and City like "%{}%" and fee_type<={} and Percentage_Required<{};'.format(coursedict.get(course),citydict.get(city),fee,percentage)
cur.execute(query)
data=cur.fetchall()
for row in data:
    print(row)
mycon.close()