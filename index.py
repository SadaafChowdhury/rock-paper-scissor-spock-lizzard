# Import the required libraries :
from tkinter import *
import random
import simpleaudio as sa

root = Tk()
root.configure(bg="#000000")
root.geometry('+0+0')
root.iconbitmap("Game.ico")
root.title("Rock-Paper-Scissor-Lizard-Spock")
root.resizable(width=False, height=False)

# To play sound files :
start = sa.WaveObject.from_wave_file("Start.wav")
Win = sa.WaveObject.from_wave_file("Win.wav")
Lose = sa.WaveObject.from_wave_file("Lose.wav")
Draw = sa.WaveObject.from_wave_file("Draw.wav")

start.play()

# Hand images :
rockHandPhoto = PhotoImage(file="Rock.jpg")
paperHandPhoto = PhotoImage(file="Paper.jpg")
scissorHandPhoto = PhotoImage(file="Scissor.jpg")
lizardHandPhoto = PhotoImage(file="Lizard.jpg")
spockHandPhoto = PhotoImage(file="Spock.jpg")

# Graphical images :
rockPhoto = PhotoImage(file="Rock.jpg")
paperPhoto = PhotoImage(file="Paper.jpg")
scissorPhoto = PhotoImage(file="Scissor.jpg")
lizardPhoto = PhotoImage(file="Lizard.jpg")
spockPhoto = PhotoImage(file="Spock.jpg")

# Decision image :
decisionPhoto = PhotoImage(file="Decision.jpg")

# Result images :
winPhoto = PhotoImage(file="Win.jpg")
losePhoto = PhotoImage(file="Lost.jpg")
tiePhoto = PhotoImage(file="Draw.jpg")

# Initialize the button variables :
rockHandButton = " "
paperHandButton = " "
scissorHandButton = " "
lizardHandButton = " "
spockHandButton = " "

# Create the result button :
resultButton = Button(root, image=decisionPhoto)

# Set the variable to True
click = True


def play():
    global rockHandButton, paperHandButton, scissorHandButton, lizardHandButton, spockHandButton

    # Set images and commands for buttons :
    rockHandButton = Button(root, image=rockHandPhoto, command=lambda: youPick("Rock"))
    paperHandButton = Button(root, image=paperHandPhoto, command=lambda: youPick("Paper"))
    scissorHandButton = Button(root, image=scissorHandPhoto, command=lambda: youPick("Scissor"))
    lizardHandButton = Button(root, image=lizardHandPhoto, command=lambda: youPick("Lizard"))
    spockHandButton = Button(root, image=spockHandPhoto, command=lambda: youPick("Spock"))

    # Place the buttons on window :
    rockHandButton.grid(row=0, column=0)
    paperHandButton.grid(row=0, column=1)
    scissorHandButton.grid(row=0, column=2)
    lizardHandButton.grid(row=0, column=3)
    spockHandButton.grid(row=0, column=4)

    # Add space :
    root.grid_rowconfigure(1, minsize=50)

    # Place result button on window :
    resultButton.grid(row=2, column=0, columnspan=5)


def computerPick():
    choice = random.choice(["Rock", "Paper", "Scissor", "Lizard", "Spock"])
    return choice


def youPick(yourChoice):
    global click

    compPick = computerPick()

    if click == True:

        if yourChoice == "Rock":

            rockHandButton.configure(image=rockPhoto)

            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False

            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=losePhoto)
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()

                click = False

            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=winPhoto)
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Lizard":
                paperHandButton.configure(image=lizardPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=winPhoto)
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            else:
                paperHandButton.configure(image=spockPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=losePhoto)
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False


        elif yourChoice == "Paper":
            rockHandButton.configure(image=paperPhoto)

            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False

            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Lizard":
                paperHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            else:
                paperHandButton.configure(image=spockPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False



        elif yourChoice == "Scissor":
            rockHandButton.configure(image=scissorPhoto)
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False

            elif compPick == "Lizard":
                paperHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            else:
                paperHandButton.configure(image=spockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

        elif yourChoice == "Lizard":
            rockHandButton.configure(image=lizardPhoto)
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Lizard":
                paperHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False

            else:
                paperHandButton.configure(image=spockPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

        elif yourChoice == "Spock":
            rockHandButton.configure(image=spockPhoto)
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

            elif compPick == "Lizard":

                paperHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False

            else:
                paperHandButton.configure(image=spockPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False


    else:
        # To reset the game :
        if yourChoice == "Rock" or yourChoice == "Paper" or yourChoice == "Scissor" or yourChoice == "Lizard" or yourChoice == "Spock":
            rockHandButton.configure(image=rockHandPhoto)
            paperHandButton.configure(image=paperHandPhoto)
            scissorHandButton.configure(image=scissorHandPhoto)
            lizardHandButton.configure(image=lizardHandPhoto)
            spockHandButton.configure(image=spockHandPhoto)
            resultButton.configure(image=decisionPhoto)

            # Get back the deleted buttons :
            scissorHandButton.grid(row=0, column=2)
            lizardHandButton.grid(row=0, column=3)
            spockHandButton.grid(row=0, column=4)

            # Set click = True :
            click = True

            # Play the sound file :
            start.play()


# Calling the play function :
play()

# Enter the main loop :
root.mainloop()