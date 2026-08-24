import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='college')
cursor = connection.cursor()
sql = "insert into student values (7,'amit',118,38)"
cursor.execute(sql)
connection.commit()
print("successfully insert")