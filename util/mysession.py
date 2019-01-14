from util.myutil import myuuid
#ＭｙＳｅｅｓｉｏｎ用来存储客户端信息
#存储格式：
# 键　id
# 值　{}

# 1345682423894:{'islogin':'True'}
# 192391280389e:{'aaa':'bbb','ccc':'ddd'}

session={}
class MySession:
    def __init__(self,handler):
        self.handler = handler

    def __getitem__(self, key):

        id = self.handler.get_cookie('sessionid')
        if id:
            #根据ｉｄ取出对应的存储在服务器上的信息
            info = session.get(id,None)
            if info:
                return info.get(key,None)
            else:
                return None

        else:
            return None

    def __setitem__(self, key, value):

        id = self.handler.get_cookie('cookieid')

        if id:
            info = session.get(id,None)
            if info:
                info[key] = value
            else:
                d = dict()
                d[key] = value
                session[id] = d
        else:
            d = dict()
            d[key] = value
            #为客户端指定一个uuid充当ｉｄ值
            id = myuuid()
            session[id] = d
            #并将ｉｄ以ｃｏｏｋｉｅ的形式写回给浏览器
            self.handler.set_cookie('cookieid',id,expires_days=10)