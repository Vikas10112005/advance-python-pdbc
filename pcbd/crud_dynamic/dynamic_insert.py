import pymysql

def testinsert1():
     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
     cursor = connection.cursor()
     sql = "insert into student values (8,'monu',8,22)"
     cursor.execute(sql)
     connection.commit()
     connection.close()
     print("successed")
#testinsert1()

def testinsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "insert into student value(%s,%s,%s,%s)"
    data = (9,'punit',9,23)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully insert")
#testinsert2()

def testinsert3(id,name,rollno,age):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "insert into student value(%s,%s,%s,%s)"
    data = (id,name,rollno,age)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully insert")
#testinsert3(10,'pooja',10,23)

def testinsert4(data={}):
    id = data['id']
    name = data['name']
    rollno = data['rollno']
    age= data['age']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "insert into student value(%s,%s,%s,%s)"
    data = (id,name,rollno,age)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("successfully")

params = {}
params['id'] = 11
params['name'] ='pranav'
params['rollno'] = 11
params['age'] = 23
testinsert4(params)
