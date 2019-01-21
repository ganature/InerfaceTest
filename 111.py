# coding=utf-8
import socket
import time
import threading
import os
#
#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',10021))
#
# s.listen(1)
#
# print('Server is running...')
#
# def TCP(sock,addr):
#     print('Accept new connection from %s:%s.' % addr)
#     while True:
#         data=sock.recv (1024)  # 接受其数据
#         time.sleep (1)  # 延迟
#         if not data or data.decode () == 'quit':  # 如果数据为空或者'quit'，则退出
#             break
#         print data
#         print dir(data)
#         sock.send (data.decode ('utf-8').upper ().encode ())  # 发送变成大写后的数据,需先解码,再按utf-8编码,  encode()其实就是encode('utf-8')
#
#     sock.close ()  # 关闭连接
#     print('Connection from %s:%s closed.' % addr)
#
#
# while True:
#     sock, addr=s.accept ()  # 接收一个新连接
#     TCP (sock, addr)


def get_files(filepath):
    if os.path.exists(filepath):
        dir=os.listdir(filepath)
        for d in dir:
            if os.path.isfile(os.path.join(filepath,d)):
                print (d)
            else:
                get_files(os.path.join(filepath,d))




if __name__=="__main__":
    filepath='D:\\Software'
    # print(os.listdir(filepath))
    get_files(filepath)
    # a='aodbsld'
    # for dirpath, dirnames, filenames in os.walk (filepath):
    #     for filename in filenames:
    #         print(os.path.join (dirpath, filename))
    #         if 1==1 and 2==2 or 3==3:
    #             print("OK")
    # b=['a','c','b']
    # b.sort()
    # c=list(a)
    # c.sort(reverse=True)
    # print c
    # print b
    # A0={'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
    # for i in A0:
    #     print i

