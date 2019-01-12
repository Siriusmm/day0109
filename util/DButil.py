import pymysql

from util.myutil import mymd5


class DButil:
    def __init__(self,**kwargs):
        host=kwargs.get('host','127.0.0.1')
        port = kwargs.get('port', 3306)
        user=kwargs.get('user','root')
        password=kwargs.get('password','123456')
        database=kwargs.get('database','blogdb')
        charset=kwargs.get('charset','utf8')
        db_info=dict(host=host,port=port,user=user,password=password,database=database,charset=charset)
        conn=pymysql.connect(**db_info)
        if conn:
            self.cursor=conn.cursor()
        else:
            raise Exception("数据库链接参数错误")

    def user_exist(self,username):
        sql='select count(*) from tb_user where user_name=%s'
        t=(username,)
        try:
            self.cursor.execute(sql,t)
            dbuser=self.cursor.fetchone()[0]
        except Exception as err:
            raise err
        if dbuser:
            return True
        else:
            return False

    def register(self,**kwargs):
        username=kwargs.get('username')
        password=kwargs.get('password')
        pwd=mymd5(password)
        avatar_path=kwargs.get('avatar_path')
        city=kwargs.get('city')
        sql = "insert into tb_user(user_name,user_password,user_avatar,user_city) VALUES (%s,%s,%s,%s)"
        t = (username, pwd, avatar_path, city)
        try:
            self.cursor.execute(sql, t)
            self.cursor.connection.commit()
            self.cursor.close()
            return True
        except Exception as err:
            self.cursor.close()
            print(err)
            return False



    def is_login(self,**kwargs):
        username=kwargs.get('username')
        password=kwargs.get('password')
        pwd=mymd5(password)
        user_info=(username,pwd)
        print(user_info)
        sql='select count(*) from tb_user where user_name=%s and user_password=%s'
        self.cursor.execute(sql,user_info)
        count=self.cursor.fetchone()[0]
        if count:
            return True
        else:
            return False




