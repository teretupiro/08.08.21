from tkinter import*

def differentwin():

    a=Toplevel()
    a.geometry('200x200')
    a['bg']='grey'
    lx1=Label(a,text='x1').place(x=10,y=10)
    ly1=Label(a, text='y1').place(x=10, y=50)
    ex1=Entry(a,width=10)
    ex1.place(x=30,y=50)
    ey1=Entry(a,width=10)
    ey1.place(x=30, y=10)
    lx2 = Label(a, text='x2').place(x=110, y=10)
    ly2 = Label(a, text='y2').place(x=110, y=50)
    ex2 = Entry(a, width=10)
    ex2.place(x=130, y=50)
    ey2 = Entry(a, width=10)
    ey2.place(x=130, y=10)

    var=StringVar()
    var.set('oval')

    rb_rect=Radiobutton(a,text='[]',variable=var,value='rect').place(x=10,y=130)
    rb_oval=Radiobutton(a,text='O',variable=var,value='oval').place(x=10,y=160)
    entry_list = (ex1, ey1, ex2, ey2)
    Button(a,text='Draw',command=lambda:draw(a,entry_list,var)).place(x=150,y=150)




def draw(win,entry_list,var):
    if var.get()=='oval':
        canvas.create_oval(int(entry_list[0].get()),
                       int(entry_list[1].get()),
                       int(entry_list[2].get()),
                       int(entry_list[3].get()),fill='black')
    elif var.get()=='rect':
     canvas.create_rectangle(int(entry_list[0].get()),
                     int(entry_list[1].get()),
                     int(entry_list[2].get()),
                    int(entry_list[3].get()),fill='black')

    win.destroy()


root=Tk()
canvas=Canvas()
canvas.pack()








Button(text='Open',command=differentwin).pack()


root.mainloop()