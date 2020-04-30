#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Pool
import os, time, random

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac
# pid = os.fork()
#
# if pid == 0:
#     print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))


# 创建子进程时，只需要传入一个执行函数和函数的参数，
# 创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start')
#     p.start()
#     p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#     print('Child process end.')

# # 用进程池的方式批量创建子进程
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep((random.random() * 3))
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# Pool
# # Pool的默认大小在我的电脑上是4，最多同时执行4个进程
# # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()  # 调用join()之前必须先调用close()
#     print('All subprocesses done.')

# 子进程
# import subprocess
#
# print('$ nslookup')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b' set q=mx\npython.org\nexit\n')
# print(output.decode('gb18030'))
# print('Exit code:', p.returncode)

# 进程间通信
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进行执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

# 在Unix/Linux下，可以使用fork()调用实现多进程。
#
# 要实现跨平台的多进程，可以使用multiprocessing模块。
#
# 进程间通信是通过Queue、Pipes等实现的。
