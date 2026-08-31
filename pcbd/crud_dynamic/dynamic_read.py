import pymysql



def testread1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0] ,'\t',data[1], '\t',data[2],'\t',data[3])
    connection.commit()
    connection.close()
    print("read done")
# testread1()

def testread2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    result = cursor.fetchall()
    coloumnname = ('id','name','rollno','age')
    for x in result:
        print({(coloumnname)[i]:x[i]for i ,_ in enumerate(x)})
    connection.commit()
    connection.close()
# testread2()

def testread3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from student where id = 4"
    print('sql=>',sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2],'\t',data[3])
    connection.commit()
    connection.close()
#testread3()

def testread4(id,name,rollno,age):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from student"
    print('sql=>', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
    connection.commit()
    connection.close()
#testread4(1,'vikas',3,23)



def read6(param={}):
    id = param.get('id',0)
    name = param.get('name','')
    rollno = param.get('rollno',0)
    age = param.get('age',0)
    pageNo = param.get('pageNo',0)
    pagesize = param.get('pagesize',0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='school')
    cursor = connection.cursor()
    sql = "select * from student where 1 = 1"
    if id != 0 :
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" + name + "%'"
    if rollno != 0 :
        sql += " and rollno = " + str(rollno)
    if age != 0 :
        sql += " and age = " + str(age)

    if pagesize > 0:
        pageNo = (pageNo - 1) * pagesize
        sql += " limit " + str(pageNo) + ", " + str(pagesize)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
    connection.commit()
    connection.close()

param = {}
param['name'] = 'k'
param['age'] = 0
param['pageNo'] = 0
param['pageSize'] = 2

read6(param)

    
