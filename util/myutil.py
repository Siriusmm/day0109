import hashlib
from uuid import uuid4


def mymd5(pwd):
    md=hashlib.md5()
    md.update(pwd.encode("utf8"))
    pwd_md5=md.hexdigest()
    return pwd_md5

def myuuid():
    u=uuid4()
    return(str(u))