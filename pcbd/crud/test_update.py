import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='college')
cursor = connection.cursor()
sql = "update student set name = 'pooja' where id = 7"
cursor.execute(sql)
connection.commit()
print("successfully")