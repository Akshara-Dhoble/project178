# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:46:57 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import*
import random
root = Tk()
root.configure(bg = "red")
root.geometry("500x500")
root.title("COLOR RANDOMIZER GAME")

label_random = Label(root)
label_random.place(relx = 0.5 , rely = 0.4 , anchor=CENTER)

class game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["Black ,Grey, Red, Blue, Orange, White ,Brown, Pink, Yellow ,Green, Purple, Maroon, Turquoise, Cyan ,Navy blue, Gold"]
        self.random_number_for_color = random.randint(0,16)
       
        self.color = ["Black ,Grey, Red, Blue, Orange, White ,Brown, Pink, Yellow ,Green, Purple, Maroon, Turquoise, Cyan ,Navy blue, Gold"]
        self.random_number_for_color.random.randint(0,16)
        
        label_random["text"] = self.text[self.random_number_for_text]
        label_random["fg"] = self.color[self.random_number_for_color]
     
obj = game()        
     
btn = Button(root , text="Start" , command=obj.updateGame , bg = "white" , fg = "Brown" ,  relief = FLAT , padx=10 , pady=1)
btn.place(relx=0.5 , rely=0.7 , anchor = CENTER)        
        
root.mainloop()