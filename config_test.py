#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

from configparser import ConfigParser


class cConfParser:
    def __init__(self, conf_path):
        self.fpath = conf_path  # 配置文件路径,要求是绝对路径
        self.cf = ConfigParser.ConfigParser()  # ConfigParser对象实例
        self.cf.read(self.fpath)  # 一启动就读取配置文件

    def __del__(self):
        # 一关闭就将ConfigParser对象的内容序列化到本地配置文件中
        with open(self.fpath, 'w') as fh:
            self.cf.write(fh)
        fh.close()

        # 添加指定的节

    def add_section(self, s):
        sections = self.cf.sections()
        if s in sections:
            return
        else:
            self.cf.add_section(s)

            # 移除指定的节

    def remove_section(self, s):
        return self.cf.remove_section(s)

    def get(self, s, o):
        return self.cf.get(s, o)

    def set(self, s, o, v):
        if self.cf.has_section(s):
            self.cf.set(s, o, v)

            # 移除指定节内的指定选项

    def remove_option(self, s, o):
        if self.cf.has_section(s):
            return self.cf.remove_option(s, o)
        return False

        # 返回节内的(key, val)列表

    def items(self, s):
        return self.cf.items(s)

        # 返回所有节的列表

    def sections(self):
        return self.cf.sections()

        # 返回节内的key列表

    def options(self, s):
        return self.cf.options(s)


if __name__ == '__main__':
    config_file = './config_demo2.conf'
    cp = cConfParser(config_file)
