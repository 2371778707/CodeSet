#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="异步上传重试方案"

# 导入所需包
import asyncio
import aiohttp
import aiomysql
import time
import json
from functools import wraps
import sys

sys.path.append("/home/spider/lin/utils/")
from logconfig import load_my_logging_cfg

# 获取日志logger
logger = load_my_logging_cfg("upload_status")


# 时间运行装饰器


def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        r = await func(*args, **kwargs)
        end = time.time()
        logger.info("\n国外国家首都客厅数据上传总共耗时：{}\n".format(end - start))
        return r

    return wrapper


class Get_data:
    mysql = {
        "host": "192.168.1.98",
        "port": 3306,
        "database": "spider",
        "user": "bigdata",
        "password": "zhongguangzhangshi",
        "charset": "utf8",

    }
    now_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @classmethod
    async def getdata(cls, loop):
        async with aiomysql.create_pool(host=cls.mysql["host"],
                                        port=cls.mysql["port"],
                                        user=cls.mysql["user"],
                                        password=cls.mysql["password"],
                                        db=cls.mysql["database"],
                                        charset="utf8",
                                        loop=loop
                                        ) as pool:
            async with pool.get() as conn:
                async with conn.cursor() as cur:
                    # sql = '''select * from t_channel_news where create_date="%s" ''' % date_n
                    #     sql = '''select * from sd_new where create_date="%s"''' % date_n
                    sql = "select * from _news_foreign_cap_data where create_date = '{}' order by newsid desc;".format(
                        cls.now_date)
                    await cur.execute(sql)
                    res = await cur.fetchall()
                    r = [i for i in res]
                    import random
                    random.shuffle(r)
                    return r


class UploadStatus:
    """
    队列queue-》发送-》循环查看重试队列requeue是否为空-》接着发送
    """

    def __init__(self):
        try:
            # 导入loop循环
            import uvloop
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
            loop = asyncio.get_event_loop()
        except ImportError as e:
            loop = asyncio.get_event_loop()
        else:
            self.loop = loop
            # 指定默认队列
            self.queue = []
            # 推荐队列
            self.cqueue = []
            # 请求重试队列
            self.requeue = []
            # 推荐重试队列
            self.recqueue = []
            # 保存原始数据
            self.data = []
            # 增加头部
            self.headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.8',
                'cookie': '_user_id=1702270120456800000; _user_account=admin;',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

    # 封装数据

    def req_covert(self, r):
        info_d = dict()
        info_d["title"] = r[4]
        info_d["newsDesc"] = r[4]
        info_d["source"] = r[6]
        info_d["content"] = r[8]
        info_d["newsType"] = '1'
        info_d["typeId"] = '1708161038001960000'
        info_d["classify"] = r[9]
        if r[7]:
            info_d["pics"] = r[7]
        info_d["area"] = r[10]
        info_d["areaTitle"] = r[1]
        info_d["isTop"] = 0
        info_d["inEssential"] = 0
        info_d["isRecommend"] = 0
        info_d["counts"] = 0
        info_d["languageVersion"] = r[12]
        info_d["link"] = r[14]
        return info_d

    # 封装数据

    def rec_covert(self, r, id):
        rec_data = dict()
        rec_data['area'] = r[10]
        rec_data['title'] = r[4]
        rec_data['source'] = r[6]
        rec_data['isTop'] = 0
        rec_data['isEssential'] = 0
        rec_data['classify'] = r[9]
        rec_data['objId'] = id
        rec_data['objType'] = 'news'
        rec_data['languageVersion'] = r[12]
        rec_data['imageUrl'] = r[7]
        return rec_data

    # 转化数据
    def torec(self, r, id):
        if "pics" in r.keys():
            r['imageUrl'] = r["pics"]
        else:
            r['imageUrl']=None
        r['objId'] = id
        r['objType'] = 'news'
        del r["newsDesc"]
        del r["newsType"]
        del r["content"]
        del r["typeId"]
        del r["areaTitle"]
        del r["isRecommend"]
        del r["counts"]
        del r["link"]
        return r

    # 打包数据

    async def pack(self):
        await self.getdata()
        self.queue = [
            asyncio.ensure_future(
                self.req(
                    self.req_covert(data))) for data in self.queue]
        # 数据上传数量
        ul = len(self.queue)
        res = await asyncio.gather(*self.queue)
        # 查看返回数据是否是可以推荐的数据
        isrec = [(i, v) for i, v in enumerate(res) if v]
        lrec = len(isrec)
        self.cqueue = [asyncio.ensure_future(self.rec(self.rec_covert(self.data[index], id))) for index, id in isrec]
        # 数据推荐数量
        cul = len(self.cqueue)
        resc = await asyncio.gather(*self.cqueue)
        # 进行推荐

        logger.info(
            "\n#############\n国外国家首都客厅数据上传情况\n###############\n上传数量--{}\n{}\n"
            "\n#############\n国外国家首都客厅数据可推荐情况\n###############\n可推荐数量--{}\n已推荐数量--{}\n"
            "\n#############\n国外国家首都客厅数据推荐具体情况\n###############\n{}\n".format(ul, res, lrec, cul, resc))


        # 重传数据数据

    async def repack(self):
        # 重装data数据
        self.data = [i for i in self.requeue]
        # 封装请求方法
        self.queue = [
            asyncio.ensure_future(
                self.req(
                    data)) for data in self.requeue]
        self.requeue = []
        # 数据上传数量
        ul = len(self.queue)
        res = await asyncio.gather(*self.queue)
        isrec = [(i, v) for i, v in enumerate(res) if v]
        lrec = len(isrec)
        self.cqueue = [asyncio.ensure_future(self.rec(self.torec(self.data[index], id))) for index, id in isrec]
        # 数据推荐数量
        cul = len(self.cqueue)
        resc = await asyncio.gather(*self.cqueue)
        logger.info(
            "\n#############\n国外国家首都客厅数据重传情况\n###############\n上传数量--{}\n{}\n"
            "\n#############\n国外国家首都客厅数据可推荐情况\n###############\n可推荐数量--{}\n已推荐数量--{}\n"
            "\n#############\n国外国家首都客厅数据推荐具体情况\n###############\n{}\n".format(ul, res, lrec, cul, resc))

    # 获取任务
    async def getdata(self):
        data = await Get_data.getdata(self.loop)
        self.queue = data
        self.data = data

    # 请求方法

    async def req(self, data):
        """
        请求上传方法
        :param data:
        :return: 成功响应200，返回对应信息，返回对应存储对象id?id,""

                不成功响应404，放入重试队伍，进行重传
        """
        async with aiohttp.ClientSession() as client:
            try:
                async with client.post("http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/top/news/save",
                                       headers=self.headers, data=data) as resp:
                    assert resp.status == 200
                    i = await  resp.content.read(100)
                    a = i.decode("utf-8")
                    try:
                        # 正确解码
                        info = json.loads(a)['retObj']
                    except json.JSONDecodeError as e:
                        # 非正确解码
                        info = json.loads(a + '""}')['retObj']
                    except Exception as e:
                        info = json.loads(a + '""}')["retObj"]
                    return info
            except BaseException:
                self.requeue.append(data)

    # 推荐首页方法
    async def rec(self, data):
        """
        推荐首页方法
        :param data:封装好的dict包括id
        :return: 成功响应200，返回对应信息
                不成功响应404，放入推荐重试队伍，进行重传
        """
        async with aiohttp.ClientSession() as client:
            try:
                async with client.post(
                        "http://192.168.1.13:8080/cityparlor-web/cityparlor/cityparlor/index/add",
                        headers=self.headers, data=data) as resp:
                    assert resp.status == 200
                    i = await  resp.content.read(100)
                    a = i.decode("utf-8")
                    try:
                        # 正确解码
                        info = json.loads(a)['msg']
                    except json.JSONDecodeError as e:
                        # 非正确解码
                        info = json.loads(a + '""}')['msg']
                    except Exception as e:
                        info = json.loads(a + '""}')["msg"]
                    return info
            except BaseException:
                self.recqueue.append(data)

    # 任务运行

    async def tasking(self):
        await self.pack()
        while self.requeue:
            await self.repack()

    def __call__(self, *args, **kwargs):
        self.loop.run_until_complete(self.tasking())
        self.loop.close()


# 开始记录
logger.info("\n###############\n国外国家首都客厅数据开始上传\n#################")
# 实例化
us = UploadStatus()
us()
logger.info("\n###############\n国外国家首都客厅数据上传结束\n##################\n")
# 记录结束
