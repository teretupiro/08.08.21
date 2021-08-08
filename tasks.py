from tkinter import*

root=Tk()

def about():
    a=Toplevel()
    a.geometry('150x250')
    a.overrideredirect(True)
    Label(a,text='aboba').pack(expand=1)
    a.after(5000,lambda :a.destroy())


Button(text='button',width=20,).pack()
Label(text='label',width=20,height=3).pack()
Button(text='aboba',width=20,command=about).pack()



root.resizable(False,False)
root.update_idletasks()
s=root.geometry()
s=s.split('+')
s=s[0].split('x')
width_root=int(s[0])
height_root=int(s[1])


w=root.winfo_screenwidth()
h=root.winfo_screenheight()

w=w//2
h=h//2

w=w-width_root//2
h=h-height_root//2

root.geometry('+{}+{}'.format(w,h))

root.mainloop()