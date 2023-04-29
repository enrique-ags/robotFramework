import pymssql  

conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
cursor = conn.cursor()  
cursor.execute('SELECT TOP (1000) * FROM [AdventureWorks2019].[HumanResources].[Employee];')  
row = cursor.fetchone()  
while row:  
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2])) 
    row = cursor.fetchone()