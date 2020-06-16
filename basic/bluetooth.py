#-*- coding:utf-8 -*-
import bluetooth
import threading
server_socket=None
 
#连接套接字服务子线程
def serveSocket(sock,info):
    while True:
        receive=sock.recv(64).decode('utf-8');
        print('['+str(info)+']'+receive);
        receive=receive+"\n";
        sock.send(receive.encode('utf-8'));
 

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM);
#允许任何地址的主机连接,未知参数:1(端口号,通道号)
server_socket.bind(("",1))
#监听端口/通道
server_socket.listen(1);

while True:
    #等待有人来连接,如果没人来,就阻塞线程等待(这本来要搞个会话池,以方便给不同的设备发送数据)
    sock,info=server_socket.accept();
    print(str(info[0])+' Connected!');
    #创建一个线程专门服务新来的连接(这本来应该搞个线程池来管理线程的)
    t=threading.Thread(target=serveSocket,args=(sock,info[0]))
    #设置线程守护,防止程序在线程结束前结束
    t.setDaemon(True)
    #启动线程
    t.start();
