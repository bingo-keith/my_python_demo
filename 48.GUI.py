#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.helloLabel = Label(self, text='Hello, world!')
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel.pack()
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Heelo, %s' % name)


app = Application()
# 设置窗口标题
app.master.title('Hello Test!')
app.mainloop()
