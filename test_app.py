from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk,Image
 
main = Tk()

def leftKey(event):
    print ("Left key pressed")

def rightKey(event):
    print ("Right key pressed")

#frame = Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
#frame.pack()

main.title("Welcome to LikeGeeks app")
main.geometry('350x200')
 
lbl = Label(main, text="Hello")
lbl.grid(column=2, row=2)
 
bar = Progressbar(main, length=200)
bar.grid(column = 3, row = 3)
bar['value'] = 0

 
def clicked():
 
    lbl.configure(text="Button was clicked !!")
    bar['value']+=10
    if (bar['value']==100):
        lbl.configure(text = 'finished')
 
btn = Button(main, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

bar.grid(column = 3, row = 3)



img = ImageTk.PhotoImage(Image.open('suit1.jpg'))
panel = Label(main, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(column=5, row=0)
 
main.mainloop()