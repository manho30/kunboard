#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : 初始化坤音键盘
@File        : utils.py
@IDE         : PyCharm
@Date        : 28/11/2022 11:29
"""

import os
import sys

import pynput.keyboard
import playsound
from threading import Thread
import tkinter
import tkinter.messagebox


root = tkinter.Tk()
root.title('坤音键盘')
root.geometry('300x200') # 置为工具窗口(没有最大最小按钮)
root.wm_attributes("-topmost", True)


#set up 2 button inside the window which can be clicked to start and stop the keyboard listener
def start():
    main('start')
    tkinter.messagebox.showinfo('提示', '坤音键盘已启动')

def stop():
    main('stop')
    tkinter.messagebox.showinfo('提示', '坤音键盘已停止')

def exit():
    root.destroy()

# show the info in top of the window aligned to center
label = tkinter.Label(root, text='坤音键盘', font=('楷体', 20), width=30, height=2)
label.pack()

label2 = tkinter.Label(root, text='作者：manho', font=('Comic sans', 10), width=30, height=2)
label2.pack()


#set up the button and the label with green color and red color
start_button = tkinter.Button(root, text='启动', command=start, bg='green', fg='white', font=('Arial', 12), width=10, height=1)
start_button.pack()

stop_button = tkinter.Button(root, text='停止', command=stop, bg='red', fg='white', font=('Arial', 12), width=10, height=1)
stop_button.pack()

exit_button = tkinter.Button(root, text='退出', command=exit, bg='red', fg='white', font=('Arial', 12), width=10, height=1)
exit_button.pack()



def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


# mutiple threads for playing audio, so that the audio can be played in parallel
def play_radio(path):
    t = Thread(target=playsound.playsound, args=(path,))
    t.start()

ch2audio = {
    'j': resource_path(os.path.join("audios", "j.mp3")),
    'n': resource_path(os.path.join("audios", "n.mp3")),
    't': resource_path(os.path.join("audios", "t.mp3")),
    'm': resource_path(os.path.join("audios", "m.mp3")),
    'J': resource_path(os.path.join("audios", "j.mp3")),
    'N': resource_path(os.path.join("audios", "n.mp3")),
    'T': resource_path(os.path.join("audios", "t.mp3")),
    'M': resource_path(os.path.join("audios", "m.mp3")),
    'jntm': resource_path(os.path.join("audios", "ngm.mp3"))
}

def on_press(key):
    try:
        ch = key.char
        if ch in ch2audio:
            play_radio(ch2audio[ch])
    except AttributeError:
        pass

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

def main(status):
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        if status == 'start':
            listener.join()

        else:
            listener.stop()

if __name__ == '__main__':
    root.mainloop()