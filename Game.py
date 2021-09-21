import random


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign.upper()

    def getName(self):
        return self.name

    def getSign(self):
        return self.sign.upper()

    def play(self, board):
        pass


class Human(Player):

    def __init__(self, name, sign):
        if sign.upper() == "X" or sign.upper() == "O":
            self.sign = sign.upper()
        else:
            raise ValueError("Sign can be 'X' or 'Y'")
        Player.__init__(self, name, sign)

    def setName(self, name):
        self.name = name

    def play(self, board):
        place = ""
        while place != " ":  # so that the while loop can start.
            user_str = input("{} ,Choose a Position [1..9] : ".format(self.getName()))
            if user_str.isdigit():
                user_int = int(user_str)
            else:
                raise ValueError("Non-valid TicTacToe Position")
            place = board[user_int - 1]  # Positions in the Game starts from 1
            if place != " ":
                print("Position {} is full".format(user_int))
            else:
                board[user_int - 1] = self.getSign()

    def __str__(self):
        return "Human : name = {} , sign = {}".format(self.name, self.sign)


class Ai(Player):
    def __init__(self):
        Player.__init__(self, "AI-V1", "")  # Ai Sign will be set depending on Human Sign

    def __str__(self):
        return "AI : Name = {} , sign = {}".format(self.name, self.sign)

    def play(self, board):
        place = "xx"
        while place != " ":  # so that the while loop can start.
            ai_choice = random.randint(1, 9)
            place = board[ai_choice - 1]
            if place == " ":
                board[ai_choice - 1] = self.getSign()
                print("{}'s choice is : Position {}".format(self.getName(), ai_choice))


class Board:

    def __init__(self, liste=None):
        if liste is None:
            liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.liste = liste

    def getListe(self):
        return self.liste

    def display(self):
        places = self.liste
        print("_____________")
        print("| {} | {} | {} |".format(places[0], places[1], places[2]))
        print("|___|___|___|")
        print("| {} | {} | {} |".format(places[3], places[4], places[5]))
        print("|___|___|___|")
        print("| {} | {} | {} |".format(places[6], places[7], places[8]))
        print("|___|___|___|")
        print()

    def checkResult(self):
        board = self.getListe()
        if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
            return True
        elif board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
            return True
        elif board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
            return True

        elif board[0] == board[3] and board[3] == board[6] and board[0] != ' ':
            return True
        elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
            return True
        elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
            return True

        elif board[0] == board[4] and board[4] == board[8] and board[0] != ' ':
            return True
        elif board[2] == board[4] and board[4] == board[6] and board[2] != ' ':
            return True


class Game:
    def __init__(self, board, human, ai):
        self.board = board
        self.human = human
        self.ai = ai

    def start(self):

        this_board = self.board
        this_human = self.human
        this_ai = self.ai
        if self.human.getSign() == "X":
            self.ai.sign = "O"
        else:
            self.ai.sign = "X"

        winner = ""
        while " " in this_board.getListe():
            this_human.play(this_board.getListe())
            this_board.display()
            if this_board.checkResult():
                winner = this_human.getName()
                break
            if " " in this_board.getListe():
                this_ai.play(this_board.getListe())
                this_board.display()
                if this_board.checkResult():
                    winner = this_ai.getName()
                    break
        if winner == "":
            print("Draw ! Nobody won !")
        else:
            print("{}, won the game !".format(winner), "\n")


class Main:
    retry = True
    print("TicTacToe by Mohamad Abouras© GmbH.All Rights Reserved®.")
    name = input("Player Name : ")
    sign = input("X or O ? ")
    while retry:
        board = Board()
        board.display()
        p1 = Human(name, sign)
        a1 = Ai()
        game = Game(board, p1, a1)
        game.start()
        print("1 - Play Again")
        print("2 - Exit")
        option = input("Choose an Option : ")
        if option == "2":
            retry = False
