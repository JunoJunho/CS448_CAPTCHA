# -*- coding: utf-8 -*-
import re
import IEC
from time import sleep
import win32gui
import win32con
from Tkinter import *
sys.path.append('./CaptchaLibrary')
sys.path.append('./CaptchaLibrary/CHARACTERIZER')
from CAFESEARCHER import CAFESEARCHER
from CAFEJOINER import CAFEJOINER
from CHARACTERIZER.INITIALIZATION import INITIALIZATION



class App:
    def __init__(self, master):
        ################ FRAME 1 #################
        master.title("DAUM SIMULATOR")
        master.geometry("700x500")

        self.frame1=Frame(master)
        self.frame1.pack()

        self.label=Label(self.frame1, text="DAUM CAFE")
        self.label.pack(side=LEFT)

        self.searchEntry=Entry(self.frame1)
        self.searchEntry.pack(side=LEFT, padx=5)
        self.searchEntry.bind("<Return>", self.okEvent)

        self.searchBtn = Button(self.frame1, text="SEARCH", command=self.OK)
        self.searchBtn.pack(side=LEFT)

        ############### FRAME 2 #################
        self.frame2 = Frame(master)
        #self.frame2.pack(fill=BOTH)
        self.frame2.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.scrollbar = Scrollbar(self.frame2, orient=VERTICAL)
        self.scrollbar.config(command=self.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.cafeList = Listbox(self.frame2, yscrollcommand=self.scrollbar.set, selectmode=EXTENDED)
        self.cafeList.pack(side=LEFT, fill=BOTH, expand=1)
        ############### FRAME 3 ####################
        self.frame3 = Frame(master)
        self.frame3.pack(side=BOTTOM)
        
        self.regBtn = Button(self.frame3, text="Go Register", command=self.goRegister)
        self.regBtn.pack(side=LEFT)
        self.clearBtn = Button(self.frame3, text="Clear", command=self.CLEAR)
        self.clearBtn.pack(side=LEFT)
        #######################################
        self.login()
        self.Theta1, self.Theta2 = INITIALIZATION('D:\\003. Project\CS448\CAPTCHA\CaptchaLibrary\\nn_params.txt')
        print 'hello'
        
    def login(self):
        self.id = 'kimjunho5357'
        self.pw = 'dbxhvldk1'
        self.ie = IEC.IEController(minimized=True)
        self.hdlg = win32gui.FindWindow('IEFrame', None)
        win32gui.PostMessage(self.hdlg, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE)
        self.ie.Navigate('http://cafe.daum.net/')
#       비활성-로그인과정
        sleep(1)
        try:
            self.ie.SetInputValue('id', self.id)
        except:
            pass
        try:
            self.ie.SetInputValue('pw', self.pw)
        except:
            pass
        try:
            self.ie.ClickButton(id='loginSubmit')
        except:
            print 'You are already logged in.'
        else:
            print 'Now you are logged in.'

    def yview(self, *arg):
        self.cafeList.yview(*arg)
        
    def OK(self):
        #print("Clear First")
        self.cafeList.delete(0, END)
        
        print "Value is", self.searchEntry.get()

        # 카페 리스트 받아와서 show List에 저장됨.
        self.showList = CAFESEARCHER(self.searchEntry.get().encode('utf-8'))

        #fill the listboxes with showList
        for i, show in enumerate(self.showList):
            self.cafeList.insert(i, ' |%-3d | ' % (i+1) + show[0]+show[1]+show[2]+show[3]+show[4])

    def okEvent(self, event):
        self.OK()

    def CLEAR(self):
        self.cafeList.delete(0, END)
        self.showList = []

    def goRegister(self):
        self.selItems = self.cafeList.curselection()
        self.selItems = map(int, self.selItems)

        win32gui.PostMessage(self.hdlg, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE)
        
        sleep(1)
        for el in self.selItems:
            for line in self.showList[el]:
                print line.strip()
            # 카페 가입 시작.
            CAFEJOINER(self.ie, [self.showList[el][0]], self.Theta1, self.Theta2)
            print """================================  ================================"""
        win32gui.PostMessage(self.hdlg, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE)

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
