#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:11:26 2020

@author: mj
"""

# import the Flask class from the flask module
from flask import Flask, render_template
import ployTest as poly
#import ChotBotGUI as chaty
import os
#Creating GUI with tkinter
import tkinter
from tkinter import *

# create the application object
app = Flask(__name__)
flag = False

"""
@app.context_processor
def context_processor():
    return dict(flag=False)
""" 

@app.route('/welcome')
@app.route('/home')
@app.route('/OpCost')
@app.route("/")
def home():
    cwd = os.getcwd()
    print(cwd)
    global flag
    if flag == False :
        flag = poly.plotAllAspects(cwd) 
    print(flag)
    return render_template("home.html")

@app.route('/Sales')
def Sales():
    return render_template('Sales.html') 

@app.route('/ProductServices')
def ProductServices():
    return render_template('ProductServices.html') 

@app.route("/about")
def about():
    return render_template("about.html")

def chatbot_response(text):
    print("chatbot_response text : ", text)
    #ints = predict_class(text, model)
    #print("chatbot_response ints : ", ints)
    #res = getResponse(ints, intents)
    return "response is on the way!!!"

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


"""
@app.route("/chatbot")
def chatbot():
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
"""


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 7777)
    #TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'