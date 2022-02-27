from tkinter import *
import tkinter as tk
import pymysql as ps
from PIL import Image, ImageTk
#creating the main window
window=Tk()
window.title("Auto Check-in")
canvas1 = tk.Canvas(window, width = 400, height = 400)
canvas1.pack()
#adding the main background
filename = PhotoImage(file = "//Users//cherish//Downloads//airplane2.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1.0, relheight=1.0)
#adding image of seat layout
image1 = Image.open("//Users//cherish//Downloads//seat.png")
test = ImageTk.PhotoImage(image1)

labe = tk.Label(image=test)
labe.image = test
labe.place(x=550, y=700)  
#creating the heading
label1 = tk.Label(window, text='Hello!You can check-in here')
label1.config(font=('helvetica', 14))
canvas1.create_window(200,25, window=label1)
#enter your name
label2 = tk.Label(window, text="Enter your name")
label2.config(font=('helvetica', 7))
canvas1.create_window(75,100, window=label2)
#enter you pnr
label3 = tk.Label(window, text="Enter your PNR")
label3.config(font=('helvetica', 7))
canvas1.create_window(75, 140, window=label3)
#enter airline
label4=tk.Label(window,text='Enter the name of the airline')
label4.config(font=('helvetica',7))
canvas1.create_window(75,180,window=label4)
#enter seat
label5=tk.Label(window,text='Enter your desired seat')
label5.config(font=('helvetica',7))
canvas1.create_window(75,220,window=label5)
#entry box for name
entry1 =tk.Entry (window) 
canvas1.create_window(200, 100, window=entry1)
#entry box for pnr
entry2 =tk.Entry (window) 
canvas1.create_window(200, 140, window=entry2)
#entry box for airlines
entry3 =tk.Entry (window) 
canvas1.create_window(200, 180, window=entry3)
#entry box for seat number
entry4=tk.Entry(window)
canvas1.create_window(200,220 ,window=entry4)
db=ps.connect(host="localhost",user="root",passwd="Cher!sh12",database="airport")
mc=db.cursor()
sql=" DELETE FROM customers WHERE name=%s"
sql2 = "INSERT INTO checked_in (name, PNR,airline,seat) VALUES (%s, %s, %s,%s);"
sql3="SELECT EXISTS(SELECT * FROM customers WHERE name= %s)"
sql4="SELECT EXISTS(SELECT * FROM customers WHERE PNR= %s)"
sql5="SELECT EXISTS(SELECT * FROM customers WHERE airline= %s)"
global labelx
labelx=tk.Label(window,text='')
labelx.config(font=('helvetica', 7))
canvas1.create_window(200,240 , window=labelx)
def check():
   
    number = entry2.get()
    name = entry1.get()
    airline=entry3.get()
    seat=entry4.get()
    mc.execute(sql3,(name))
    test=str(mc.fetchall())
    mc.execute(sql4,(number))
    test1=str(mc.fetchall())
    mc.execute(sql5,(airline))
    test2=str(mc.fetchall())
    ((0,))
    if name=="":
        labelx.config(text='please enter your name')
    elif number=="":
        labelx.config(text='please enter your PNR')
    elif airline=="":
        labelx.config(text='please enter your airline')
    elif seat=="":
        labelx.config(text='please choose a seat')
    elif(test[2]=="1") and (test1[2]=="1") and  (test2[2]=="1") :
        mc.execute(sql2,(name,number,airline,seat))
        db.commit()
        mc.execute(sql,(name))
        db.commit()
        labelx.config(text='Thank you for checking in! Your boarding pass is printing!')
        entry1.delete(0,'end')
        entry2.delete(0,'end')
        entry3.delete(0,'end')
        entry4.delete(0,'end')
    else:
        labelx.config(text='Sorry! You are not on the passengers list, contact administration')
        
    
   
    
button1 = tk.Button(text='Enter', command=check, bg='brown', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 260, window=button1)    

