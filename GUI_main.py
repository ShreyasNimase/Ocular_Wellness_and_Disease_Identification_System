# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Pathological Myopia Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('2.jpg')
image2 = image2.resize((1800, 850))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Pathological  Myopia  Detection",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=70, height=1)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
   
    
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=100, y=240)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="brown", fg="white")
button3.place(x=100, y=330)

root.mainloop()