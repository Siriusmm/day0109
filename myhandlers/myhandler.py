from tornado.web import RequestHandler

from util.DButil import DButil


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
        if name and password:
            login_info=dict(username=name,password=password)
            dbutil=self.application.dbutil
            data=dbutil.is_login(**login_info)
            if data:
                self.redirect('/blog')
            else:
                msg = '用户名或密码错误'
                self.render('login.html',result=msg)
        else:
            msg = '用户名或密码不能为空'
            self.render('login.html', result=msg)

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html',result='')

    def post(self, *args, **kwargs):
        username=self.get_body_argument('name',None)
        password=self.get_body_argument('password',None)
        rpassword=self.get_body_argument('rpassword',None)
        city=self.get_body_argument('city',None)
        files=self.request.files
        avatar=files.get("avatar")
        if avatar:
            data=avatar[0].get('body')
            avatar_path='mystatics/images/avatar/'+username+'.jpg'
            with open(avatar_path,'wb') as f:
                f.write(data)
        else:
            avatar_path=None
        if username and password and city:
            dbutil=self.application.dbutil
            db=dbutil.user_exist(username)
            if db:
                msg='用户名已被占用'
                self.render('register.html',result=msg)
            else:
                register_info=dict(username=username,password=password,city=city,avatar_path=avatar_path)
                info=dbutil.register(**register_info)
                if info:
                    self.redirect('/login')
                else:
                    msg='未知错误'
                    self.render('register.html',result=msg)

        else:
            msg='用户名或密码不能为空'
            self.render('register.html',result=msg)

class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        username=self.get_body_argument('username',None)
        print(username)
        result=self.application.dbutil.user_exist(username)
        if result:
            d=dict(msg='not_ok')
        else:
            d=dict(msg='ok')
        self.write(d)

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