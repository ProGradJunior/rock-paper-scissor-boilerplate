from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="aqua")

# picture
rock_img = ImageTk.PhotoImage(Image.open("./assets/rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("./assets/paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("./assets/scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("./assets/rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("./assets/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("./assets/scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="aqua")
comp_label = Label(root, image=scissor_img_comp, bg="aqua")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerScore = Label(root, text=0, font=("Arial", 15), bg="aqua", fg="green")
computerScore = Label(root, text=0, font=("Arial", 15), bg="aqua", fg="green")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=("Arial", 15), text="USER", bg="aqua", fg="brown")
comp_indicator = Label(root, font=("Arial", 15), text="COMPUTER",
                       bg="aqua", fg="brown")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=("Arial", 15), bg="aqua", fg="green")
msg.grid(row=3, column=2)

# update message


# update user score


# update computer score


# check winner    


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="black", font=("Arial", 15), command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="black", font=("Arial", 15), command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="black", font=("Arial", 15), command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
