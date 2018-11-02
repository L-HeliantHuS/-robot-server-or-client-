#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author    : HeliantHuS
# Time      : 2018/10/31
import time
import sys
import socket

print("输入help获得帮助")
address = input("请输入服务端的IP：")
port = input("请输入端口号：")
ip_list = address.split(".")
init = 0
try:
    if (ip_list[0].isdigit() == True and int(ip_list[0]) < 255) and (ip_list[1].isdigit() == True and int(ip_list[1]) < 255) and (ip_list[2].isdigit() == True and int(ip_list[2]) < 255) and (ip_list[3].isdigit() == True and int(ip_list[3]) < 255):
        print("正在连接服务器…………")
        while True:
            try:
                ip_port = (address, int(port))
                sk = socket.socket()
                sk.connect(ip_port)
                if init == 0:
                    print("服务器连接成功！\n"
                          "**********************************************************\n"
                          "|    W     WW     W         A       W     WW     W       |\n"
                          "|     W   W  W   W         A A       W   W  W   W        |\n"
                          "|      W W    W W         A A A       W W    W W         |\n"
                          "|       W      W         A     A       W      W          |\n"
                          "**********************************************************")
                    init += 1
                inputs = input("请输入你要说的内容：")
                if inputs == "":
                    print("不可以输入空白的哦！")
                    continue
                elif inputs == "exit":
                    exit()
                sk.sendall(bytes(inputs, encoding="utf-8"))
                server_reply = sk.recv(1024)
                print(server_reply.decode())
                sk.close()
            except (ConnectionRefusedError,TimeoutError):
                print("服务器连接失败，请检查您的网络环境，或服务器是否开启！")
                input("----轻击回车以退出----")
                sys.exit()

    else:
        print("ip不规范！")
        time.sleep(1)
        sys.exit()
except IndexError:
    print("ip不规范！")
    time.sleep(1)
    sys.exit()
