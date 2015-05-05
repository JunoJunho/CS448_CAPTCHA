# -*- coding: cp949 -*-
import win32gui
import win32api
import win32con
import time


def WriteGuessString(guessString):
    VK_TAB = 0x09
    VK_MENU = 0x12  # ALT key

    hdlg = win32gui.FindWindow('IEFrame', None)
    rect = win32gui.GetWindowRect(hdlg)

    for guessChar in guessString:
        time.sleep(0.1)
        win32api.keybd_event(win32api.VkKeyScan(guessChar), 0x1e, 0, 0)
        win32api.keybd_event(win32api.VkKeyScan(guessChar), 0x9e, win32con.KEYEVENTF_KEYUP, 0)


def PressKey(key, count=1):
    hdlg = win32gui.FindWindow('IEFrame', None)
    rect = win32gui.GetWindowRect(hdlg)

    for i in range(count):
        win32api.keybd_event(key, 0x8f, 0, 0)
        win32api.keybd_event(key, 0x8f, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
