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
from ctypes import windll

import pynput.keyboard
import playsound
from threading import Thread
import tkinter
import tkinter.messagebox

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


root = tkinter.Tk()
windll.shcore.SetProcessDpiAwareness(1)
root.title('坤音键盘v2.0.0')
root.geometry('500x400')
root.wm_attributes("-topmost", True)
#icon
root.iconphoto(False, tkinter.PhotoImage(file=resource_path(os.path.join('public', 'img.png'))))



def start():
    Thread(target=main_program, args=('start',)).start()
    tkinter.messagebox.showinfo('提示', '坤音键盘已启动\n版本：2.0.0\n作者：manho')

def _exit():
    root.destroy()
    os._exit(1)

def _log():
    log = tkinter.Toplevel()
    log.title('日志')
    log.geometry('600x400')
    log.wm_attributes("-topmost", True)
    log.grid_rowconfigure(0, weight=1)
    log.grid_columnconfigure(0, weight=1)
    txt = tkinter.Text(log, font=('楷体', 20), undo=True)
    scrollb = tkinter.Scrollbar(log, command=txt.yview)
    txt.configure(yscrollcommand=scrollb.set)
    txt.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
    scrollb.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    txt.insert(tkinter.END, '2021-11-28 19:24\n')
    txt.insert(tkinter.END, '新增3个音效\n')
    txt.insert(tkinter.END, '版本：2.0.0\n')
    txt.insert(tkinter.END, '作者：manho\n')
    txt.insert(tkinter.END, '--------------------------\n')
    txt.insert(tkinter.END, '2021-11-28 16:09\n')
    txt.insert(tkinter.END, '修复了窗口无反应问题\n')
    txt.insert(tkinter.END, '版本：1.1.0\n')
    txt.insert(tkinter.END, '作者：manho\n')
    txt.insert(tkinter.END, '--------------------------\n')
    txt.insert(tkinter.END, '2021-11-28 11:29\n')
    txt.insert(tkinter.END, '坤音键盘已启动\n')
    txt.insert(tkinter.END, '版本：1.0.0\n')
    txt.insert(tkinter.END, '作者：manho\n')

    txt.pack()




label = tkinter.Label(root, text='坤音键盘', font=('楷体', 30), width=30, height=2)
label.pack()

label2 = tkinter.Label(root, text='作者：manho', font=('Comic sans', 20), width=30, height=2)
label2.pack()


start_button = tkinter.Button(root, text='启动', command=start, bg='green', fg='white', font=('Arial', 12), width=13, height=2)
start_button.pack()

exit_button = tkinter.Button(root, text='退出', command=_exit, bg='red', fg='white', font=('Arial', 12), width=13, height=2)
exit_button.pack()

src_button = tkinter.Button(root, text='源码', command=lambda: os.startfile('https://github.com/manho30/kunboard'), bg='blue', fg='white', font=('Arial', 12), width=13, height=2)
src_button.pack()

log_button = tkinter.Button(root, text='日志', command=_log, bg='blue', fg='white', font=('Arial', 12), width=13, height=2)
log_button.pack()


# mutiple threads for playing audio, so that the audio can be played in parallel
def play_radio(path):
    t = Thread(target=playsound.playsound, args=(path,))
    t.start()

ch2audio = {
    'j': resource_path(os.path.join("audios", "j.mp3")),
    'n': resource_path(os.path.join("audios", "n.mp3")),
    't': resource_path(os.path.join("audios", "t.mp3")),
    'm': resource_path(os.path.join("audios", "m.mp3")),
    'g': resource_path(os.path.join("audios", "g.mp3")),
    'a': resource_path(os.path.join("audios", "a.mp3")),
    'J': resource_path(os.path.join("audios", "j.mp3")),
    'N': resource_path(os.path.join("audios", "n.mp3")),
    'T': resource_path(os.path.join("audios", "t.mp3")),
    'M': resource_path(os.path.join("audios", "m.mp3")),
    'G': resource_path(os.path.join("audios", "g.mp3")),
    'A': resource_path(os.path.join("audios", "a.mp3")),
    'ngm': resource_path(os.path.join("audios", "ngm.mp3")),
}
def on_press(key):
    try:
        ch = key.char
        if ch in ch2audio:
            play_radio(ch2audio[ch])

    except AttributeError:
        if key == key.space or key == key.enter:
            play_radio(ch2audio['ngm'])

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

def main_program (status):
    if status == 'start':
        with pynput.keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    else:
        with pynput.keyboard.Listener(on_press=on_press) as listener:
            listener.stop()

if __name__ == '__main__':
    root.mainloop()