#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author    : HeliantHuS
# Time      : 2018/10/30
import socket
import sys
import requests

class SoCket():
    def __init__(self, address):
        ip,port = address.split(":")[0],address.split(":")[1]
        self.main(ip, port)

    def auto_replay(self, msg):
        print('对方:%s' % msg)
        reply = self.get_response(msg)
        return reply


    def get_response(self, message):
        data = {
            'key': 'ed2fd8a780f546c0897accb4bb3a0846',
            'info': message,
            'userid': 'robot'
        }
        try:
            apiUrl = 'http://www.tuling123.com/openapi/api'
            r = requests.post(apiUrl, data).json()
            replays = r['text']
            print('回复:%s' % replays)
            return replays
        except:
            return
    def main(self, ip, port):
        ip_port = (ip, int(port))
        sk = socket.socket()
        sk.bind(ip_port)
        sk.listen(500)
        print('服务器成功开启，服务器ip:{}, 端口号:{}等待连接...'.format(ip_port[0], ip_port[1]))
        while True:
            try:
                conn, address = sk.accept()
                client_data = conn.recv(1024)
                if client_data.decode() == "help":
                    conn.sendall(
                        bytes('请输入数字用来查询:\n1.查看官网！\n2.查看我是你的谁\n你还可以输入中文对我聊天哦！', encoding="utf-8"))
                elif client_data.decode() == '1':
                    conn.sendall(
                        bytes("官网是！！！！http://172.168.70.172", encoding="utf-8"))
                elif client_data.decode() == '2':
                    conn.sendall(bytes("我是机器人啊！！zz", encoding="utf-8"))
                elif client_data.decode() == "":
                    conn.sendall(bytes('并不理解你的意思！', encoding="utf-8"))
                elif client_data.decode() != [1 - 9]:
                    msg = self.auto_replay(client_data.decode())
                    conn.sendall(bytes(msg, encoding="utf-8"))

                try:
                    with open('message.log', 'a+') as fp:
                        fp.write(str(address[0]) + '---->R:' +
                                 client_data.decode() + "Q:" + msg + '\n')
                except NameError:
                    with open('message.log', 'a+') as fp:
                        fp.write(str(address[0]) + '---->R:' +
                                 client_data.decode() + "Q:" + "固定回复！" + '\n')
                conn.close()
            except ConnectionResetError:
                pass

if __name__ == '__main__':
    try:
        address = sys.argv[1]
        sock = SoCket(address)
    except IndexError:
        print("请在后面加本机的IP和端口号(不要使用127.0.0.1) 格式为：./socket_server.exe (xxx.xxx.xxx.xxx:port)")
        input("----轻按回车以退出----")
        sys.exit()
