"""
команды для функционала кнопок
"""

def test_button():
    print("Button work!")

def add_label():
    label = tk.Label(win,text="test label")
    label.pack()



"""
импорт библиотеки 
"""
import tkinter as tk
win = tk.Tk()
"""
модуль отвечающий за вид окна программы
"""

win.title("Keywords optimization")  # название окна
win.geometry("800x800+1600+300")  # размер окна
win.resizable(False, False)
# win.config(bg="#BABABA")
label = tk.Label(win, text="same text",
                 # bg="#BABABA",  # цвет фона под надписью в окне
                 # fg="#424242",  # цвет надписи в окне
                 font=("Arial", 20),
                 pady=20,  # отступ надписи сверху
                )

"""
создаю кнопки программы
"""

butt_1 = tk.Button(win, text="button",
                   # command = test_button, # действие при нажати на кнопку
                   command=add_label,
                   bg = '#BABABA',
                   borderwidth=(30),
                   # foreground="red",
                   activebackground="blue",
                   # fg="#424242",  # цвет надписи в окне
                   font=("Arial", 20),
                   padx=40,  # отступ надписи слева
                   pady=5,  # отступ надписи сверху

                 )
butt_1.pack()
label.pack()




win.mainloop()  # цикл отвечающий за открытие окна
