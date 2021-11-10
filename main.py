import tkinter
from tkinter import filedialog
import subprocess
import socket
from pykeyboard import PyKeyboard
import psutil

list = psutil.pids()
NetEaseAlive = False
for i in list:
    p = psutil.Process(i)
    if p.name() == "CloudMusic.exe":
        NetEaseAlive = True
        break
list.clear()

k = PyKeyboard()
CODE = "UTF-8"


def PlayMusic():
    k.press_keys([k.control_key, k.alt_key, 'p'])


def NextSong():
    k.press_keys([k.control_key, k.alt_key, k.right_key])


def LastSong():
    k.press_keys([k.control_key, k.alt_key, k.left_key])


def IncreaseVolume():
    k.press_keys([k.control_key, k.alt_key, k.up_key])


def DecreaseVolume():
    k.press_keys([k.control_key, k.alt_key, k.down_key])


def main():
    main_host = socket.gethostbyname(socket.gethostname())
    print("本机ip:"+str(main_host))
    global NetEaseAlive
    while not NetEaseAlive:
        print("网易云未运行,请选择网易云路径")
        root = tkinter.Tk()
        root.withdraw()
        path = str(filedialog.askopenfilename())
        if "CloudMusic" in path:
            subprocess.Popen(path)
            print(path)
            print('开启成功')
            NetEaseAlive = True
        else:
            print("选择错误，请重新选择")
    MySocket = socket.socket()
    MySocket.bind(("192.168.123.11", 8888))
    MySocket.listen()
    while True:
        client_conn, address = MySocket.accept()
        command = client_conn.recv(50).decode(CODE)
        print("command:"+command)
        if command == "nextsong":
            NextSong()
        if command == "lastsong":
            LastSong()
        if command == "pause":
            PlayMusic()
        if command == "increasevolume":
            IncreaseVolume()
        if command == "decreasevolume":
            DecreaseVolume()
        client_conn.close()


main()
