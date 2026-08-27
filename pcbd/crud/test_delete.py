import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='college')
cursor = connection.cursor()
sql = "delete from student where id = 5"
cursor.execute(sql)
connection.commit()
connection.close()
print("succesed")


