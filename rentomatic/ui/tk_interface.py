import os

from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import filedialog

from rentomatic.interface.interface import Interface


class TkWindow():
    def __init__(self, window):
        super().__init__()
        self._window = window
        self._window.title('约瑟夫环')
        self._window.geometry('1080x481+10+10')
        self._name = ''
        self._start = 1
        self._step = 1
        self._reader = None
        self._interface = None
        self.create_page()

    def create_page(self):
        Button(self._window,text='打开文件', command= self.open_text).grid(row=0, columnspan=2)
        self._intext = Text(self._window,height=15)
        self._intext.grid(row=1,columnspan=2,padx=10,pady=10)
        Label(self._window,text='请输入开始的序号：',font=('Arial',12)).grid(row=2,column=0,sticky="w")
        self._start = Entry(self._window,font=('Arial',12))
        self._start.grid(row=2,column=1,sticky="w")
        Label(self._window, text='约瑟夫的相应规则：', font=('Arial', 12)).grid(row=3, column=0,sticky="w")
        self._step = Entry(self._window, font=('Arial', 12))
        self._step.grid(row=3, column=1,sticky="w")
        Button(self._window,text='开始约瑟夫', command= self.start_josephus).grid(row=4, columnspan=2)
        Label(self._window, text='淘汰次序：', font=('Arial', 12)).grid(row=0,column=2, columnspan=2,sticky="w")
        self._outext = Text(self._window, height=15)
        self._outext.grid(row=1,column=2,  columnspan=2,padx=10,pady=10)
        Label(self._window, text='具体信息如下：', font=('Arial', 12)).grid(row=3, column=2,columnspan=2,sticky="w")
        self._success = Text(self._window, height=1)
        self._success.grid(row=4, column=2,columnspan=2,padx=10,pady=10,sticky="w")

    def open_text(self):
        self._interface = Interface()
        file_path = filedialog.askopenfilename()
        file_path = file_path.replace('/','\\\\')
        target_file = ''
        file_names = self._interface.read_name_list(file_path)
        if file_names:
            content = ''
            for each in file_names:
                content = content + each + '\n'
            target_file = tkinter.simpledialog.askstring('请输入要解压的文件名', content)
            if not target_file:
                return self.open_text()
        try:
            self._interface.create_reader(file_path,target_file)
            self._interface.get_josephus()
            people_info = self._interface.get_people_str()
            self._intext.insert(INSERT, people_info)
        except FileNotFoundError:
            tkinter.messagebox.showwarning(title='Warning', message='请输入.txt、。csv、。zip文件')

    def start_josephus(self):
        start = self._start.get()
        step = self._step.get()
        try:
            start = int(start)
            step = int(step)
            self._interface.check_start(start)
            self._interface.set_start(start)
            self._interface.set_step(step)
            people_info = self._interface.get_out_str()
            self._outext.insert(INSERT, people_info)
            success_person = self._interface.get_people()
            self._success.insert(INSERT, success_person)
        except ValueError:
            tkinter.messagebox.showwarning(title='Warning', message='请输入正确的数字下标')

def gui_start():
    init_window = Tk()
    test_gui = TkWindow(init_window)
    init_window.mainloop()


if __name__ =='__main__':
    gui_start()