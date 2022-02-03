from tkinter import *

root = Tk()

top_frame = Frame(root)
bot_frame = Frame(root)

top_frame.pack()
bot_frame.pack(side=BOTTOM)


button1 = Button(top_frame,text="Кнопка в верхней части",fg='green')
button1.pack(side=LEFT)
button2 = Button(bot_frame,text="Кнопка в ниженей части",fg='yellow')
button2.pack()



root.mainloop()