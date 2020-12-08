import tkinter as tk
def say_hi():
    print("Hi")

win = tk.Tk()
win.title("Test application")
win.geometry("800x800+900+300")
win.minsize(200,200)
win.maxsize(1000,1000)
win.resizable(True,True)

label_1 = tk.Label(win,text = "Hekko",
                   padx = 40,
                   pady = 100,
                   bg = 'green',
                   fg = 'yellow',
                   width = 250,
                   font =("arial" ,30,"bold"),
                   relief = tk.RAISED,
                   anchor = 'w',
                   )

label_1.pack()

btn1 = tk.Button(win,command = say_hi,
                 text = "button",
                 bg = 'black',
                 fg = 'red',
                 underline = True,
                 font =("arial" ,40,"bold"),
                borderwidth = 50,


                 )
btn1.pack()
win.mainloop()
