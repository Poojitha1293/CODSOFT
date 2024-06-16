import tkinter as tk
from tkinter import *
import random

player_score=0
computer_score=0
options=[('rock',0),('paper',1),('scissor',2)]

def player_choice(player_input):
    global player_score,computer_score
    computer_input=get_computer_choice()
    
    player_choice_label.config(text= "Your Selected : "+player_input[0])
    computer_choice_label.config(text= "Computer Selected : "+computer_input[0])

    if(player_input==computer_input):
        winner_label.config(text="Tie")
    elif((player_input[1]-computer_input[1])%3==1):
        player_score+=1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text="Your Score : "+str(player_score))
    else:
        computer_score+=1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text="Computer Score : "+str(computer_score))

def get_computer_choice():
    return random.choice(options)
    
system=tk.Tk()
system.title("ROCK PAPER SCISSORS GAME")
system.geometry('500x500')
system.configure(bg='pink')

game_title=tk.Label(system,text="ROCK PAPER SCISSORS",font=("Baskerville Old Face",30,"bold"),fg="blue",bg="yellow",width=60,height=2)
game_title.pack()

winner_label=tk.Label(system,text="Let's Start the Game....",font=("Times New Roman",30),fg='red',bg='pink')
winner_label.place(x=600,y=150)

player_options=tk.Label(system,text="Your Options : ",font=("Times New Roman",25),fg='grey4',bg='pink')
player_options.place(x=350,y=230)

rock_btn=tk.Button(system,text="ROCK",font=("Baskerville Old Face",15,"bold"),bg="lime green",fg="black",command=lambda : player_choice(options[0]))
rock_btn.place(x=550,y=320)

paper_btn=tk.Button(system,text="PAPER",font=("Baskerville Old Face",15,"bold"),bg="grey4",fg="white",command=lambda : player_choice(options[1]))
paper_btn.place(x=670,y=320)

scissor_btn=tk.Button(system,text="SCISSOR",font=("Baskerville Old Face",15,"bold"),bg="tomato",fg="black",command=lambda : player_choice(options[2]))
scissor_btn.place(x=800,y=320)

score_label=tk.Label(system,text="Score : ",font=("Times New Roman",25),fg="grey4",bg="pink")
score_label.place(x=380,y=400)

player_choice_label=tk.Label(system,text="Your Selected :  ---",font=("Goudy Old Style",20),fg="blue",bg="pink")
player_choice_label.place(x=500,y=460)

player_score_label=tk.Label(system,text="Your Score : -",font=("Goudy Old Style",20),fg="blue",bg="pink")
player_score_label.place(x=800,y=460)

computer_choice_label=tk.Label(system,text="Computer Selected : ---",font=("Goudy Old Style",20),fg="blue",bg="pink")
computer_choice_label.place(x=500,y=530)

computer_score_label=tk.Label(system,text="Computer Score : -",font=("Goudy Old Style",20),fg="blue",bg="pink")
computer_score_label.place(x=800,y=530)

system.mainloop()
