import tkinter
from tkinter import *
import random
from NewWindow import new_list
from defs import correct


list_of_words = {}

### Main window ###

window = Tk()
window.minsize(width=500, height=500)
window.title("Words Learning")

frame_twenty = tkinter.Frame(window, pady=20)
frame_twenty.pack()

frame_twentyone = tkinter.Frame(window, pady=20)
frame_twentyone.pack()

frame_twentytwo = tkinter.Frame(window)
frame_twentytwo.pack()

title = tkinter.Label(frame_twenty, text="Words learning", font=("Ink Free", 20, "bold"))
title.pack()

user_guess_input = tkinter.Entry(frame_twentyone, justify=CENTER)
user_guess_input.grid(row=2, column=0, padx=20)

random_word = tkinter.Label(frame_twentyone, font=("Ink Free", 20, "bold"))
random_word.grid(row=2, column=2)

correct_button = tkinter.Button(frame_twentyone, text="click", command=correct)
correct_button.grid(row=2, column=3)

right_answer = tkinter.Label(frame_twentyone, text="", font=("Ink Free", 20, "bold"))
right_answer.grid(row=3, column=0)

correct_wrong = tkinter.Label(frame_twentyone, text="", font=("Ink Free", 20, "bold"))
correct_wrong.grid(row=3, column=2)

tittle2 = tkinter.Label(frame_twentyone, text="", font=("Ink Free", 20, "bold"))
tittle2.grid(row=5, column=2)

create_new_list = tkinter.Button(frame_twentytwo, text="Load/Create list of words", command=new_list)
create_new_list.pack()


### proces ###



if len(list_of_words) == 0:
    random_word["text"] = ""
else:
    one_word = random.choice(list(list_of_words.keys()))
    random_word["text"] = one_word

window.bind('<Return>',lambda event:correct())




window.mainloop()