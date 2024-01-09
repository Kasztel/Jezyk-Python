from tkinter import *
import random

window = Tk()

window.configure(bg="white")

window.geometry("400x400")

window.title("Rzut kością")

def dice_roll():
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice_dots)}')
    label.pack()


roll_button = Button(window, text="Rzuć", width=10, height=2, font=15, bg="yellow", bd=2, command=dice_roll)

roll_button.pack(padx=10, pady=15)

label = Label(window, font=("times", 250), bg="white", fg="red")

window.mainloop()
