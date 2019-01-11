import tornado
import pymysql
from tornado import options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file
from tornado.web import Application, RequestHandler

define('port',default=8000,type=int,multiple=False)
parse_config_file('config')

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',result='')
    def post(self, *args, **kwargs):
        pass


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',result='')
    def post(self, *args, **kwargs):
        name = self.get_argument('name', '')
        password = self.get_argument('password', '')
        result=''
        connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='blogdb')
        cursor = connect.cursor()
        sql='select count(*) from tb_user where user_name=%s and user_password=%s'
        t=(name,password)
        print(t)
        try:
            cursor.execute(sql,t)
            data = cursor.fetchone()[0]
        except Exception as err:
            print(err)
        cursor.close()
        print(data)
        if data:
            self.redirect('/blog')
        else:
            msg = '用户名或密码错误'
            self.render('login.html',result=msg)

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html',result='')

    def post(self, *args, **kwargs):
        name=self.get_body_argument('name',None)
        password=self.get_body_argument('password',None)
        rpassword=self.get_body_argument('rpassword',None)
        city=self.get_body_argument('city',None)
        files=self.request.files
        avatar=files.get("avatar")
        if avatar:
            data=avatar[0].get('body')
            avatar_path='upload/avatar/'+name+'.jpg'
            with open(avatar_path,'wb') as f:
                f.write(data)
        else:
            avatar_path=None
        if name and password:
            connect=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='blogdb')
            cursor=connect.cursor()
            sql="select count(*) from tb_user where user_name=%s"
            t=(name,)
            try:
                cursor.execute(sql,t)
                db=cursor.fetchone()[0]
            except Exception as err:
                print(err)
            if db:
                msg='用户名已被占用'
                self.render('register.html',result=msg)
            else:
                sql="insert into tb_user(user_name,user_password,user_avatar,user_city) VALUES (%s,%s,%s,%s)"
                t=(name,password,avatar_path,city)
                try:
                    cursor.execute(sql,t)
                    connect.commit()
                    self.write('注册成功')
                except Exception as err:
                    print(err)
            cursor.close()

        else:
            msg='用户名或密码不能为空'
            self.render('register.html',result=msg)

class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('blog.html',blogs=[{'title':'第一篇博客',
                            'tag':['情感','男女','星座'],
                            'content':'好长好长好长的正文',
                            'author':'某某人',
                            'avatar':'a.jpg',
                            'comment':45},

                           {'title':'第二篇博客',
                            'tag':['技术','达内'],
                            'content':'学好python找我就对了',
                            'author':'大旭旭',
                            'avatar':None,
                            'comment':0}])
    def post(self, *args, **kwargs):
        pass


app=Application([('/',IndexHandler),
                 ('/login/',LoginHandler),
                 ('/register/',RegisterHandler),
                 ('/blog',BlogHandler)],
                static_path='mystatics',template_path='mytemplates')
server=HTTPServer(app)
server.listen(8000)
IOLoop.current().start()