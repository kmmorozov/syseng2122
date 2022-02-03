from tkinter import *
root = Tk()
def myfun(event):
    print(event)
    u=e1.get()
    p=e2.get()
    print(u)
    print(p)
    if u=='kirill' and p=='123qaz':
        l3["text"]="Вход успешен"
    else:
        l3["text"]="Пользователь или пароль не найден"
l1 = Label(root, text='Имя:')
l2 = Label(root, text='Пароль:')
l3 = Label(root)

e1 = Entry(root)
e2 = Entry(root)

cb = Checkbutton(root, text="чужой компьютер")
b1 = Button(text="Войти")

l1.grid(row=0,column=0,sticky=W)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
cb.grid(columnspan=2)
b1.grid(columnspan=2,sticky=E)
l3.grid(columnspan=2)
b1.bind("<Button-1>",myfun)



root.mainloop()