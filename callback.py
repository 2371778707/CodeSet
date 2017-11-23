#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

class Callback:
    def __init__(self, instance, function_name):
        self.instance = instance
        self.function_name = function_name

    def action(self, params):
        self.instance.__getattribute__(self.function_name)(params)
        print(getattr(self.instance,'self.function_name')(params))

class Test:
    def __init__(self):
        self.clb = None

    def register(self, clb):
        self.clb = clb

    def do_test(self):
        params = []
        self.clb.action(params)


class Api(object):
    def __init__(self, test_instance):
        test_instance.register(Callback(self, self.function.__name__))

    def function(self, params):
        print('function')


t = Test()
a = Api(t)
t.do_test()

# call.py
import called


def callback():
    print
    "in callback"


def main():
    # called.test()
    called.test_call(callback)
    print
    "in call.py"


main()

# called.py
''''' 
def test(): 
    print "in called.py test()" 
'''


def test_call(p_call):
    p_call()