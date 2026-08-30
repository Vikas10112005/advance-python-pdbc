import pymysql

def testupdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update student set name='annu' where id = 2 "
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("done")
#testupdate1()

def testupdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s "
    data = ('pawan',4)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully update")
#testupdate2()

def testupdate3(name,id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = (name,id)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully")
#testupdate3('vikas','2')

def testupdate4(data):
    id = data['id']
    name = data['name']
    age = data['age']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "update student set name = %s , age = %s where id = %s"
    data = (name,age,id)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successed")
# params = {}
# params['id'] = 11
# params['name'] = 'manav'
# params['age'] = '27'
# testupdate4(params)
