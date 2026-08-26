import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='college')
cursor = connection.cursor()
sql = "select * from student"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],)

