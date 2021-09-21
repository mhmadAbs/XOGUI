# Registerd Players

import random
from tkinter import *

root = Tk()
root.title("TicTacToe")
root.configure(bg="grey")
root.wm_minsize(420, 500)


class RegisteredPlayer:

    def __init__(self, window):
        # Content of Squares
        s11 = StringVar()
        s12 = StringVar()
        s13 = StringVar()
        s21 = StringVar()
        s22 = StringVar()
        s23 = StringVar()
        s31 = StringVar()
        s32 = StringVar()
        s33 = StringVar()
        squares_strings = [s11, s12, s13, s21, s22, s23, s31, s32, s33]

        player_wins = 0
        ai_wins = 0

        def getPlayerScore():
            with open("../Backup/Results.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith(id_entry.get()):
                        fst, snd = line.split(",")
                        _, p_score = fst.split("-")
                        _, a_score = snd.split("-")
                        return int(p_score), int(a_score)
                    return 0

        def getAiSign():
            if player_sign.get() == "X":
                return "O"
            return "X"

        def highlight(fst, snd, thd):
            fst.config(bg="orange")
            snd.config(bg="orange")
            thd.config(bg="orange")

        def checkResult():
            if s11.get() == s12.get() and s12.get() == s13.get() and s11.get() != "":
                stopGame()
                highlight(r1c1, r1c2, r1c3)
                return True
            elif s21.get() == s22.get() and s22.get() == s23.get() and s21.get() != "":
                stopGame()
                highlight(r2c1, r2c2, r2c3)
                return True
            elif s31.get() == s32.get() and s32.get() == s33.get() and s31.get() != "":
                stopGame()
                highlight(r3c1, r3c2, r3c3)
                return True

            elif s11.get() == s21.get() and s21.get() == s31.get() and s11.get() != "":
                stopGame()
                highlight(r1c1, r2c1, r3c1)
                return True
            elif s12.get() == s22.get() and s22.get() == s32.get() and s12.get() != "":
                stopGame()
                highlight(r1c2, r2c2, r3c2)
                return True
            elif s13.get() == s23.get() and s23.get() == s33.get() and s13.get() != "":
                stopGame()
                highlight(r1c3, r2c3, r3c3)
                return True

            elif s11.get() == s22.get() and s22.get() == s33.get() and s11.get() != "":
                stopGame()
                highlight(r1c1, r2c2, r3c3)
                return True
            elif s13.get() == s22.get() and s22.get() == s31.get() and s13.get() != "":
                stopGame()
                highlight(r1c3, r2c2, r3c1)
                return True

        def onSquare(num, btn):
            nonlocal ai_wins, player_wins
            if sign_menu["state"] == "disabled" and len(squares_strings) > 0:
                btn.config(state="disabled")
                if num == 11:
                    s11.set(player_sign.get())
                    squares_strings.remove(s11)

                elif num == 12:
                    s12.set(player_sign.get())
                    squares_strings.remove(s12)
                elif num == 13:
                    s13.set(player_sign.get())
                    squares_strings.remove(s13)
                elif num == 21:
                    s21.set(player_sign.get())
                    squares_strings.remove(s21)
                elif num == 22:
                    s22.set(player_sign.get())
                    squares_strings.remove(s22)
                elif num == 23:
                    s23.set(player_sign.get())
                    squares_strings.remove(s23)
                elif num == 31:
                    s31.set(player_sign.get())
                    squares_strings.remove(s31)
                elif num == 32:
                    s32.set(player_sign.get())
                    squares_strings.remove(s32)
                elif num == 33:
                    s33.set(player_sign.get())
                    squares_strings.remove(s33)
                if checkResult():
                    feedback_lbl.config(text="{} won the game !".format(id_entry.get()))
                    player_wins += 1
                    player_score_lbl.config(text=player_wins)
                    updateDB()
                if not checkResult() and len(squares_strings) == 0:
                    feedback_lbl.config(text="Tide !")
                    player_wins += 1
                    ai_wins += 1
                    updateDB()
                if len(squares_strings) > 0 and not checkResult():
                    feedback_lbl.config(text="AI's Turn", fg="blue")
                    feedback_lbl.after(500, playAi)  # Some delay as if AI is thinking

        def submit():
            p_id = id_entry.get()
            if len(p_id) > 0:
                id_entry.config(state="disabled")
                sign_menu.config(state="disabled")
                feedback_lbl.config(text="Game Started", fg="green")
                submit_btn.config(state="disabled")
                updateResult()
                player_score_lbl.config(text=int(player_wins))
                ai_score_lbl.config(text=int(ai_wins))

            else:
                feedback_lbl.config(text="Enter you Name first !")

        player_sign = StringVar()
        player_sign.set("X")
        sign_menu = OptionMenu(window, player_sign, "X", "O")
        sign_menu.place(x=170, y=110)

        header = Label(window, anchor="center", bg="grey", fg="orange", height=2, text="Welcome to TicTacToe",
                       font="none 15 bold")
        header.grid(row=0, column=0)

        empty_row = Label(window, text="", bg="grey")
        empty_row.grid(row=1, column=0)

        id_lbl = Label(window, anchor="w", bg="grey", fg="black", height=1, text="Player ID : ",
                       font="none 12 ")
        id_lbl.place(x=15, y=70)

        id_entry = Entry(window, bg="white", width=20)
        id_entry.place(x=170, y=70)

        submit_btn = Button(window, text="Submit", width=6, fg="orange", bg="grey", font="none 12 bold",
                            command=submit)
        submit_btn.place(x=310, y=110)

        empty_row2 = Label(window, text="", bg="grey")
        empty_row2.grid(row=3, column=0)

        sign_lbl = Label(window, anchor="w", bg="grey", fg="black", height=1, text="Sign : ", font="none 12 ")
        sign_lbl.place(x=15, y=110)

        Label(window, text="--------------------------------------------------------------------------------------",
              fg="black",
              bg="grey").place(x=0, y=150)

        r1c1 = Button(window, textvariable=s11, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(11, r1c1))
        r1c1.place(
            height=50, x=40, y=290)
        r1c2 = Button(window, textvariable=s12, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(12, r1c2))
        r1c2.place(
            height=50,
            x=145,
            y=290)
        r1c3 = Button(window, textvariable=s13, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(13, r1c3))
        r1c3.place(
            height=50,
            x=250,
            y=290)
        r2c1 = Button(window, textvariable=s21, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(21, r2c1))
        r2c1.place(height=50, x=40, y=340)

        r2c2 = Button(window, textvariable=s22, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(22, r2c2))
        r2c2.place(height=50, x=145, y=340)

        r2c3 = Button(window, textvariable=s23, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(23, r2c3))
        r2c3.place(height=50, x=250, y=340)

        r3c1 = Button(window, textvariable=s31, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(31, r3c1))
        r3c1.place(height=50, x=40, y=390)

        r3c2 = Button(window, textvariable=s32, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(32, r3c2))
        r3c2.place(height=50, x=145, y=390)

        r3c3 = Button(window, textvariable=s33, bg="white", fg="black", font="none 15 bold", width=8,
                      command=lambda: onSquare(33, r3c3))
        r3c3.place(height=50, x=250, y=390)

        feedback_lbl = Label(window, text="Enter ID to and submit to start", fg="brown", bg="grey", font="none 13 ")
        feedback_lbl.place(x=40, y=170)

        player_score_lbl = Label(window, text="0", fg="black", bg="white", font="Arial 35 bold")
        player_score_lbl.place(x=80, y=210)

        two_points_lbl = Label(window, text=":", fg="black", bg="grey", font="Arial 35 bold")
        two_points_lbl.place(x=180, y=210)

        ai_score_lbl = Label(window, text="0", fg="black", bg="white", font="Arial 35 bold")
        ai_score_lbl.place(x=270, y=210)

        def playAi():
            btns = [r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3]

            if len(squares_strings) > 0 and not checkResult():  # There is at least one free place
                choice = random.choice(squares_strings)
                choice.set(getAiSign())
                feedback_lbl.config(text="{}'s Turn".format(id_entry.get()), fg="blue")
                squares_strings.remove(choice)
                if checkResult():
                    feedback_lbl.config(text="You lost !")
                    nonlocal ai_wins
                    ai_wins += 1
                    ai_score_lbl.config(text=str(ai_wins))
                    updateDB()  # CHANGE TO ENUMS

            for btn in btns:  # To prevent player from selecting a position that is full
                if btn["text"] != "":
                    btn.config(state="disabled")

        def updateDB():
            id_ = id_entry.get()
            new_score_a = ai_score_lbl["text"]
            new_score_p = player_score_lbl["text"]


            with open("../Backup/Results.txt", "r") as f:
                current = [x for x in f.readlines() if not x.startswith(id_)]
            with open("../Backup/Results.txt", "w") as f:
                f.writelines(current)
                f.write("{}-{},AI-{}\n".format(id_, new_score_p, new_score_a))

        def updateResult():
            nonlocal player_wins, ai_wins
            player_wins, ai_wins = getPlayerScore()

        def exit_f():
            root.destroy()

        exit_btn = Button(window, text="Exit", width=15, fg="red", font="none 12 bold", command=exit_f)
        exit_btn.place(x=40, y=450, height=30)

        def restart():
            btns = [r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3]

            nonlocal squares_strings  # so that the outer list variable updated
            squares_strings = [s11, s12, s13, s21, s22, s23, s31, s32, s33]
            for sqr in squares_strings:
                sqr.set("")
            for btn in btns:
                btn.config(state="active", bg="white")
            feedback_lbl.config(text="Game Restarted")

        restart_button = Button(window, text="Restart", width=15, fg="green", font="none 12 bold", command=restart)
        restart_button.place(x=200, y=450, height=30)

        def stopGame():
            btns = [r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3]
            for btn in btns:
                btn.config(state="disabled")


RegisteredPlayer(root)
root.mainloop()