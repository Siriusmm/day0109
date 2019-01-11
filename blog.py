import tornado
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
        if name == 'abc' and password == '123':
            self.redirect('/blog')
        else:
            msg = '用户名或密码错误'
            self.render('login.html',result=msg)

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


app=Application([('/',IndexHandler),('/login',LoginHandler),('/blog',BlogHandler)],
                static_path='mystatics',template_path='mytemplates')
server=HTTPServer(app)
server.listen(8000)
IOLoop.current().start()