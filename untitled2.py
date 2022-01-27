# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:51:27 2022

@author: fijik
"""

from tkinter import *
root=Tk()
root.title("encypted cool thing")

root.geometry("400x400")
root.configure(background = 'blue')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="green", fg="orange")
label = Label(root, text = "what was this supposed to be again? ", bg="green", fg="orange")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        
btn=Button(root,text="The funny name thing",command=asciiConverter, bg='red', fg = 'magenta')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
        
label.place(relx=0.5,rely=0.6,anchor=CENTER)
        
root.mainloop()