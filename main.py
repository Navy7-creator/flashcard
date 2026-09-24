from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
#--------------------------------------------------------------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/korean_words.csv")
    to_learn=og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




#------------------------------------------------------------------------------------------
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(title,text="Korean",fill="black")
    canvas.itemconfig(word,text=current_card["Korean"],fill="black")
    canvas.itemconfig(card_bg, image=card_fr_img)
    flip_timer=window.after(5000, flip_card)

    print(current_card["Korean"])
def flip_card():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=current_card["English"],fill="white")
    canvas.itemconfig(pronunciation,text=current_card["Pronunciation"],fill="white")
    canvas.itemconfig(card_bg,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame.from_dict(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()



#-----------------------------------UI---------------------------
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(5000,flip_card)

canvas=Canvas(width=800, height=526)
card_fr_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_bg =canvas.create_image(400, 263, image=card_fr_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title=canvas.create_text(400,130,text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="word",font=("Ariel",40,"bold"))
pronunciation = canvas.create_text(400,430,text="",font=("Ariel",15))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(row=1, column=0)


check_imag= PhotoImage(file="images/right.png")
known_button=Button(image=check_imag,highlightthickness=0,command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
