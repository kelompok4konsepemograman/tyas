buttons=StringVar()
button1 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button1))
button1.grid(row=1, column=0,sticky = S+N+E+W)
button2 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button2))
button2.grid(row=1, column=1,sticky = S+N+E+W)
button3 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button3))
button3.grid(row=1, column=2,sticky = S+N+E+W)