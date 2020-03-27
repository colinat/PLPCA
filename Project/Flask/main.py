#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:11:26 2020

@author: mj
"""

# import the Flask class from the flask module
from flask import Flask, render_template, request
import ployTest as poly
#import Transcript_py3 as py3
import os

# create the application object
app = Flask(__name__)
flag = False

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

@app.route('/Upload', methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def Upload():
    print("inside home...")
    cwd = os.getcwd()
    print("cwd - ", cwd)
    print("ROOT_PATH - ", ROOT_PATH)
    print("request.method - ", request.method)
    if request.method == 'POST':
        return render_template("error.html")
    return render_template("home.html")

@app.route("/upload", methods=['POST'])
def upload():
    print("inside upload")
    file = request.files['file']
    name = request.values['name']
    folderLocation = ROOT_PATH.replace('Flask', 'data')
    file.save(os.path.join(folderLocation,name))
    fileLocation = "".join((folderLocation, "\\", name))
    print("folderLocation - ", fileLocation)
    if os.path.isfile(fileLocation):
        print("File exist...")
        global flag
        flag = False
        if flag == False :
            """
            py3.getcsv(folderLocation+"/input.txt")
            """
            flag = poly.plotAllAspects(folderLocation) 
            print(flag)
            return render_template("Sales.html")
    else:
        render_template("error.html")

@app.route('/OpCost')
def OpCost():
    return render_template('opCost.html') 

@app.route('/Sales')
def Sales():
    return render_template('Sales.html') 

@app.route('/ProductServices')
def ProductServices():
    return render_template('ProductServices.html') 

@app.route('/Debt')
def Debt():
    return render_template('debt.html') 

@app.route('/Earnings')
def Earnings():
    return render_template('earnings.html') 

@app.route('/Acquisitions')
def Acquisitions():
    return render_template('acquisitions.html') 

@app.route('/Competition')
def Competition():
    return render_template('competition.html') 

@app.route('/OpRisks')
def OpRisks():
    return render_template('opRisks.html')  

@app.route("/About")
def About():
    return render_template("about.html")

def chatbot_response(text):
    print("chatbot_response text : ", text)
    #ints = predict_class(text, model)
    #print("chatbot_response ints : ", ints)
    #res = getResponse(ints, intents)
    return "response is on the way!!!"

# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 7777)
    #TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'