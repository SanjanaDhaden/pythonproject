from tkinter import *


import mysql.connector

from PIL import ImageTk
window = Tk()
frame = Frame(window)
frame.place(x=700,y=100)
usernameLabel = Label(frame,text="username")
usernameLabel.grid(row=0,column=0)
usernameEntry=Entry(frame,width=30)
usernameEntry.grid(row=0,column=1)
usernameLabel =Label(frame,text="password")
passwordLabel.grid(row=0,column=0)
usernameEntry=Entry(frame,width=30)
frame.pack()
window.mainloop()
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sanju#@1001"
)
mycur=conn.cursor()
if(mycur) :
    print("Success")
else :
    print("Problem in database")

q = "use customerdata"
mycur.execute(q)
#query = "create table studentdb(name varchar(100),rollno varchar(100))"
#mycur.execute(query)
#p = "drop table studentdb"
#mycur.execute(p)