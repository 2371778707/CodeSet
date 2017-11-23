# !/usr/bin/env python
#-*-coding:utf-8-*-

#我想困扰最多的就是执行两条命令，一条一直在执行，卡住第二条怎么办,按照下面的情况
#child先执行，child3后执行，并且child1先调用wait(),因此，无论如何child1先执行，
#怎么让child3先执行呢，child3放在1前面，还是不行，child3.wait()也药放在前面。
# import subprocess
# child = subprocess.Popen(["ping", "www.baidu.com"])
# child2 = subprocess.Popen("ls -l",shell=True)
# child.wait()
# child3 = subprocess.Popen("python python.py",shell=True)
# child.wait()
# child3.wait()
# child2.wait()
# print("parent process")
#其实两个命令并不会阻塞，写两个ping脚本，发现同时都有出现，说明都在执行，看到堵塞只是因为命令慢而已
#当执行一条循环的命令时，发现无法输出，是主程序先执行完，没有等待子进程，因为这个就是一个子进程的问题
# ，因此，需要wait()方法来等待子进程。