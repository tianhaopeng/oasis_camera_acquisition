#
# python_grabber
#

from tkinter import *


class SelectDevice:
    def __init__(self, parent, devices):
        self.device_id = None

        top = self.top = Toplevel(parent)
        top.attributes("-toolwindow", 1)
        top.geometry("250x200")
        top.resizable(False, False)
        top.columnconfigure(0, weight=1)
        top.rowconfigure(1, weight=1)

        self.myLabel = Label(top, text='Select a video device:')
        self.myLabel.grid(padx=5, pady=5)

        self.listbox = Listbox(top, selectmode=SINGLE)
        self.listbox.grid(sticky=W+E+N+S, padx=5, pady=5)
        for item in devices:
            self.listbox.insert(END, item)

        self.mySubmitButton = Button(top, text='Ok', command=self.send)
        self.mySubmitButton.grid(padx=5, pady=5)

    def send(self):
        self.device_id = self.listbox.curselection()[0]
        self.top.destroy()
