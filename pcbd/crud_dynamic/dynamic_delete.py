import pymysql

def testdelete1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "delete from student where id = 11"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("delete")
#testdelete1()

def testdelete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "delete from student where id = %s"
    data = (10)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("delete successfully")
#testdelete2()

def testdelete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "delete from student where id = %s"
    data = [id]
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("done")
testdelete3(9)
