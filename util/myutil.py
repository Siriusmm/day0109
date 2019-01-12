import hashlib
def mymd5(pwd):
    md=hashlib.md5()
    md.update(pwd.encode("utf8"))
    pwd_md5=md.hexdigest()
    return pwd_md5

