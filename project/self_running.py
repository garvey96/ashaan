import shutil
import os
from tkinter import *
from tkinter import ttk

#startup_folder = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
#dst = os.path.join(startup_folder, "startup_program_python")
#os.mkdir(dst)

#shutil.copy(__file__, dst)
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x270")


def open_popup():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Child Window")
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)


print("running from", __file__)


condition = True
if(condition):
    Label(win, text=" Click the Below Button to Open the Popup Window", font=('Helvetica 14 bold')).pack(pady=20)
    #Create a button in the main Window to open the popup
    ttk.Button(win, text= "Open", command= open_popup).pack()
    win.mainloop()
