#import all the needed libraries
from tkinter import *
import tkinter as tk
import mysql.connector as ps 
from functools import partial
#creating the main window (canvas)
window=Tk()
window.title("Employee data entry")
canvas1 = tk.Canvas(window, width = 400, height = 300)
canvas1.pack()
#Adding the background
filename = PhotoImage(file = "cherish@Cherishs-MacBook-Air ~ % /Users/cherish/Downloads")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#adding the main heading
label1 = tk.Label(window, text='Customer data centre')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
#connecting sql and python
db=ps.connect(host="localhost",user="root",passwd="Cher!sh12",database="airport")
mc=db.cursor()
sql = "INSERT INTO `customers` (`name`, `PNR`,`airline` ) VALUES (%s, %s, %s)"
#creating the login system
usernameLabel = Label(window, text="User Name")
usernameLabel.config(font=('helvetica', 7))
canvas1.create_window(75, 100, window=usernameLabel)
username = StringVar()
usernameEntry = Entry(window, textvariable=username)
canvas1.create_window(200, 100, window=usernameEntry)
passwordLabel = Label(window,text="Password")
passwordLabel.config(font=('helvetica', 7))
canvas1.create_window(75, 140, window=passwordLabel)
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*')
canvas1.create_window(200, 140, window=passwordEntry)

def login():
    if(usernameEntry.get()=="airport" and passwordEntry.get()=="airport123"):
        label2 = tk.Label(window, text="Enter customer's name")
        label2.config(font=('helvetica', 7))
        canvas1.create_window(75, 100, window=label2)
        label3 = tk.Label(window, text="Enter customer's PNR")
        label3.config(font=('helvetica', 7))
        canvas1.create_window(75, 140, window=label3)
        label4=tk.Label(window,text='Enter the name of the airline')
        label4.config(font=('helvetica',7))
        canvas1.create_window(75,180,window=label4)
        
        entry1 =tk.Entry (window)
        canvas1.create_window(200, 100, window=entry1)
        entry2 =tk.Entry (window)
        canvas1.create_window(200, 140, window=entry2)
        entry3 =tk.Entry (window)
        canvas1.create_window(200, 180, window=entry3)
        usernameEntry.delete(0,'end')
        passwordEntry.delete(0,'end')
        usernameEntry.destroy()
        passwordEntry.destroy()
        usernameLabel.destroy()
        passwordLabel.destroy()
        loginButton.destroy()
        def data_entry():
            number = entry2.get()
            name = entry1.get()
            airline=entry3.get()
            mc.execute(sql, (name,number,airline))
            db.commit()
            labelx = tk.Label(window, text='Entry Successful!')
            labelx.config(font=('helvetica', 7))
            canvas1.create_window(330,260, window=labelx)
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            
        def show():
            sql2 = "SELECT * FROM `customers`"
            mc.execute(sql2)
            result = mc.fetchall()
            a=0
            for i in result:
                a+=1     
                

                labelx = tk.Label(window, text=i)
                labelx.config(font=('helvetica', 7))
                canvas1.create_window(320,100+(a*20), window=labelx)
            usernameLabel= Label(window, text="Customer's List")
            usernameLabel.config(font=('helvetica', 7))
            canvas1.create_window(320, 80, window=usernameLabel)    

               
        button1 = tk.Button(text='Enter', command=data_entry, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 280, window=button1)    
        button2 = tk.Button(text="Show customer's list", command=show, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(330, 290, window=button2)
        
        
    else:
        
        label = tk.Label(window, text="Incorrect login credentials")
        label.config(font=('helvetica', 7))
        canvas1.create_window(75, 180, window=label)
        passwordEntry.delete(0,'end')
        usernameEntry.delete(0,'end')
        
        
        
loginButton = Button(window, text="Login", command=login)
canvas1.create_window(300, 140, window=loginButton)
        
