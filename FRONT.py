from tkinter import *
from tkinter import ttk, messagebox, Menu
import tkinter
import speech_recognition as sr
import sys
import os
import sqlite3
import string
import re
#import final_front_iti 
#import backend
#from backend import *

global st
rw = Tk()
rw.title(" TRAIN ENQUIRY SYSTEM")
rw.geometry("500x300")
rw.configure(background="powder blue")
list1 = ['Humsafar','Duranto','Rajdhani','GorakhpurExpress','HyderabadExpress','GuwahatiSpecial','PatliputraExpress','KalkaMail','ShatabdiExpress','JhelumExpress']
list2 = ['Pune','Delhi','Kolkata','Lucknow','Chennai','Guwahati','Patna','Chandigarh','Secunderabad','Pune']
list3 = ['Nagpur','Pune','Mumbai','Bengaluru','Hyderabad','Hyderabad','Ranchi','Kolkata','Indore','Delhi']

def data_m(text2):
    conn=sqlite3.connect("train.db")
    cur=conn.cursor()
    #text.upper()
    repr(text2)
    list4 = text2.split()
    if("from" in text2 and "to" in text2):
           next_word = list4[list4.index("from") + 1]
           next_word1 = list4[list4.index("to") + 1]
           print(next_word+next_word1)
           if(next_word in list2 and next_word1 in list3):
                  print(next_word+next_word1)
                  #conn1=sqlite3.connect("train.db")
                  #cur1=conn1.cursor()
                  print(next_word+next_word1)
                  cur.execute("SELECT * FROM train WHERE Destination=? and source=?",(next_word1,next_word))
                  row=cur.fetchall()
                  print(next_word+next_word1)
                  conn.close()
                  print(next_word+next_word1)
                  window4 = tkinter.Toplevel(rw)
                  window4.geometry("600x70")
                  window4.configure(background="powder blue")
                  label=tkinter.Label(window4,text=row, font = ("Arial Bold", 15))
                  label.pack()
                  print(row)
                  flag=1     

                  
                                           #text2.replace(' ','')
    else:
           text2 = re.sub(r"\s+", "", text2, flags=re.UNICODE)
           print(text2)
           for i in list1:
               if(i in text2):
                   print(i)
                   cur.execute("SELECT * FROM train WHERE name=?",(i,))
                   row=cur.fetchall()
                   conn.close()
                   window3 = tkinter.Toplevel(rw)
                   window3.geometry("600x70")
                   window3.configure(background="powder blue")
                   label=tkinter.Label(window3,text=row, font = ("Arial Bold", 15))
                   label.pack()
                   print(row)
                   flag=1
                                     
           
    if(flag!=1):
           print("Sorry no such record exists!")
           label=tkinter.Label(window3,text="Sorry no such record exists!",font = ("Arial Bold", 15))
           label.pack()

       

def help1() :
       window2 = tkinter.Toplevel(rw)
       window2.geometry("400x5")
       window2.configure(background="powder blue")
       Label(window2, text="Select the commands as per your scope of use").pack()

def speech():
        r = sr.Recognizer()
        window1 = tkinter.Toplevel(rw)
        window1.geometry("500x200")
        window1.configure(background="powder blue")
        with sr.Microphone() as source:
                
                print("Kindly speak something...")
                audio = r.listen(source)
                label = tkinter.Label(window1,text = "<<Your speech must include words like\n Currentstatus, Source, destination, estimated time>>", font =("Arial Bold", 8))
                label.pack()

                print("Recognising your speech")
                try:
                        text1 = r.recognize_google(audio)
                        print("You said : {}".format(text1))
                        label = tkinter.Label(window1,text = "You said: "+text1, font =("Arial Bold", 10),fg="red")
                        label.pack()
                        #btn3 = tkinter.Button(window1, text = "SUBMIT MY SPEECH", font=("Arial Bold",12),fg = "violet",bg="black", width=25, height=2, bd=2)    
                        #btn3.pack(side=LEFT, padx=20, pady=35)
                        data_m(text1)
                except:
                        label = tkinter.Label(window1,text = " Sorry, Could not recognise your voice ", font =("Arial Bold", 10))
                        label.pack()
                        print("Sorry, could not recognise your voice")

def run():
       os.system('final_front_iti.py')




     
menu = Menu(rw)
 
new_item = Menu(menu)

menu.add_cascade(label='HELP', command=help1)

rw.config(menu=menu)

label = ttk.Label(rw, text = "WELCOME TO THE TRAIN ENQUIRY SYSTEM", font = ("Arial Bold", 15))
#label.grid(column=10, row=5)
label.pack()


btn1 = tkinter.Button(rw, text = "GIVE COMMAND IN SPEECH", font=("Arial Bold",12),fg = "violet",bg="black", width=25, height=2, bd=2)

btn1.pack(side=LEFT, padx=20, pady=35)
btn1.config(command = speech)

btn2 = tkinter.Button(rw, text = "ADMINISTRATION", font=("Arial Bold",12),fg = "violet",bg="black", width=25, height=2,bd=2)
btn2.pack(side = LEFT, padx=20, pady=35)
btn2.config(command = run)
rw.mainloop()
