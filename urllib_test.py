#urllib python3
from urllib import request

def ub_test(url):
    request.urlretrieve(url,filename="21.html")
    request.urlcleanup()
    file = request.urlopen(url).read()
    # while True:
    fileline = request.urlopen(url).readline()
        # print(fileline,"\n")
    return file,fileline
def crawl_csdn():
    headers = ()
    opener = request.build_opener()
    opener.addheaders = [headers]
    url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
    # con = request.urlopen(url).read()
    con = opener.open(url,timeout=1).read()
    return con
if __name__ =="__main__":
    key = "林".encode("utf-8")
    url = 'http://www.baidu.com/s?wd={}'.format(key)
    a,b = ub_test(url)
    print(type(a),"\n",type(b.decode("utf-8")))
    # a = crawl_csdn()
    print(a)