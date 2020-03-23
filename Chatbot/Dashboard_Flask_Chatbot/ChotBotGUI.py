#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:20:42 2020

@author: mj
"""

def chatbot_response(text):
    print("chatbot_response text : ", text)
    #ints = predict_class(text, model)
    #print("chatbot_response ints : ", ints)
    #res = getResponse(ints, intents)
    return "response is on the way!!!"

#Creating GUI with tkinter
import tkinter
from tkinter import *

def chatMsg(msg1, msg2):
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "You: " + msg1 + '\n\n')
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    ChatLog.insert(END, "Bot: " + msg2 + '\n\n')
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
    
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    print(msg)
    EntryBox.delete("0.0",END)
    
    if msg != '':
        print("inside if" , msg)
        msg1 = msg
        msg2 = chatbot_response(msg)
        chatMsg(msg1, msg2)
    else:
        msg1 = msg
        msg2 = "Msg is blank!!!"
        chatMsg(msg1, msg2)    
        
        
base = Tk()
base.title("ChatBot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)
#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
EntryBox.config(foreground="#442265", font=("Verdana", 14 ))

SendButton.place(x=6, y=401, height=90)

ChatLog.config(state=NORMAL)
ChatLog.insert(END, "Bot: " + "Hello there!!!" + '\n\n')
ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
ChatLog.config(state=DISABLED)
base.mainloop()
