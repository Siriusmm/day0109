import tornado
import pymysql
from tornado import options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file
from tornado.web import Application, RequestHandler

from myapp.myapplication import MyApplication
from myconfig.config import configs
from myhandlers.myhandler import *
from mymoduls.mymoduler import *

app=MyApplication([('/',IndexHandler),
                 ('/login',LoginHandler),
                 ('/register',RegisterHandler),
                 ('/blog',BlogHandler),
                ('/check',CheckHandler)],
                 sp='mystatics',
                 tp='mytemplates',
                  um={'login_module':LoginModule,'register_module':RegisterModule,'blog_module':BlogModule})
server=HTTPServer(app)
server.listen(configs['port'])
IOLoop.current().start()