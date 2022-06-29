from tkinter import *
from PIL import Image, ImageTk

a=1
b=0
player1_score=0
player2_score=0

def new_game():
    win = Toplevel(root)
    win.title("The game")
    win.iconbitmap("C:\python\Tic Tac Toe\icon.ico")

    canvas = Canvas(win, width=500, height=500, bg="grey25")
    canvas.grid(columnspan=5, rowspan=5)

    score_text = StringVar()
    score_label = Label(win, textvariable=score_text, font=("impact", 20), bg="grey25", fg="white")
    score_text.set("Player1 (X) score:  " + str(player1_score) + "        Player2 (O) score: "+ str(player2_score))
    score_label.grid(row=0, columnspan=5)

    button1=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(1), font=("impact", 30), fg="grey25")
    button1.grid(row=1,column=1)

    button2=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(2), font=("impact", 30), fg="grey25")
    button2.grid(row=1,column=2)

    button3=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(3), font=("impact", 30), fg="grey25")
    button3.grid(row=1,column=3)

    button4=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(4), font=("impact", 30), fg="grey25")
    button4.grid(row=2,column=1)

    button5=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(5), font=("impact", 30), fg="grey25")
    button5.grid(row=2,column=2)

    button6=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(6), font=("impact", 30), fg="grey25")
    button6.grid(row=2,column=3)

    button7=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(7), font=("impact", 30), fg="grey25")
    button7.grid(row=3,column=1)

    button8=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(8), font=("impact", 30), fg="grey25")
    button8.grid(row=3,column=2)

    button9=Button(win,text="",bg='white', width=7, height=2,command=lambda : buttonclick(9), font=("impact", 30), fg="grey25")
    button9.grid(row=3,column=3)

    turn_text = StringVar()
    turn_label = Label(win, textvariable=turn_text, font=("impact", 20), bg="grey25", fg="white")
    turn_text.set("It's Player1's turn.")
    turn_label.grid(row=4, columnspan=5)


    def play_again(winner_text):
        def reset_game():
            n.destroy()
            n.update()
            button1["text"]=button2["text"]=button3["text"]=button4["text"]=button5["text"]=button6["text"]=button7["text"]=button8["text"]=button9["text"]=""
            a=1
            b=0

        def close_game():
            n.destroy()
            n.update()
            win.destroy()
            win.update()

        n = Toplevel(win)
        n.title("Play again?")
        n.iconbitmap("C:\python\Tic Tac Toe\icon.ico")
        n.geometry("235x125")
        n.configure(bg="white")


        winner_label = Label(n, text=winner_text, bg="white", fg="grey25", font=("impact", 16))
        winner_label.grid(row=0, columnspan=2)

        play_label = Label(n, text="Do you want to play again?", bg="white", fg="grey25", font=("impact", 16))
        play_label.grid(row=1, columnspan=2)

        yes_btn = Button(n, text="Yes!", bg="grey25", fg="white", font=("impact", 16),command=reset_game)
        yes_btn.grid(row=2, column=0)

        no_btn = Button(n, text="No!", bg="grey25", fg="white", font=("impact", 16),command=close_game)
        no_btn.grid(row=2, column=1)

    def check_winner():
        global player1_score, player2_score
        #Player1 is the winner
        if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        elif button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X":
            player1_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player1 is the winner!")

        #Player2 is the winner
        elif button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O":
            player2_score+=1
            score_text.set("Player1 score:  " + str(player1_score) + "                    Player2 score: "+ str(player2_score))
            play_again("Player2 is the winner!")

        elif button1["text"]!="" and button2["text"]!="" and button3["text"]!="" and button4["text"]!="" and button5["text"]!="" and button6["text"]!="" and button7["text"]!="" and button8["text"]!="" and button9["text"]!="" :
            play_again("Game over! No one won.")


    def buttonclick(x):
        global a, b
        #player1=a
        #player2=b
        if x==1 and a==1 and button1["text"]=="":
            button1["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==1 and b==1 and button1["text"]=="":
            button1["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==2 and a==1 and button2["text"]=="":
            button2["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==2 and b==1 and button2["text"]=="":
            button2["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==3 and a==1 and button3["text"]=="":
            button3["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==3 and b==1 and button3["text"]=="":
            button3["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==4 and a==1 and button4["text"]=="":
            button4["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==4 and b==1 and button4["text"]=="":
            button4["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==5 and a==1 and button5["text"]=="":
            button5["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==5 and b==1 and button5["text"]=="":
            button5["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==6 and a==1 and button6["text"]=="":
            button6["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==6 and b==1 and button6["text"]=="":
            button6["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==7 and a==1 and button7["text"]=="":
            button7["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==7 and b==1 and button7["text"]=="":
            button7["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==8 and a==1 and button8["text"]=="":
            button8["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==8 and b==1 and button8["text"]=="":
            button8["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0

        if x==9 and a==1 and button9["text"]=="":
            button9["text"]="X"
            check_winner()
            turn_text.set("It's Player2's turn.")
            a=0
            b=1

        if x==9 and b==1 and button9["text"]=="":
            button9["text"]="O"
            check_winner()
            turn_text.set("It's Player1's turn.")
            a=1
            b=0


def instructions():
    p = Toplevel(root)
    p.title("Instructions")
    p.iconbitmap("C:\python\Tic Tac Toe\icon.ico")

    instructions_label = Label(p, bg="white", text="1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. Player1 is X, Player2 is O. Players take turns putting their marks in empty squares.\n\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.", font=("shanti", 10))
    instructions_label.grid(row=1, column=1)


def exit_game():
    root.quit()


root = Tk()
root.title("Tic Tac Toe game")
root.iconbitmap("C:\python\Tic Tac Toe\icon.ico")
root.configure(bg="white")


canvas = Canvas(root, width=500, height=500, bg="white")
canvas.grid(columnspan=3, rowspan=5)

#logo
logo = Image.open('game.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

play_btn = Button(root, text="New game", font=("impact", 16), command=new_game, bg="grey25", fg="white")
play_btn.grid(row=2, column=1)

instructions_btn = Button(root, text="Instructions", font=("impact", 16), command=instructions, bg="grey25", fg="white")
instructions_btn.grid(row=3, column=1)

exit_btn = Button(root, text="Exit", font=("impact", 16), command=exit_game, bg="grey25", fg="white")
exit_btn.grid(row=4, column=1)


root.mainloop()
