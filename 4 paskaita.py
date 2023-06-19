#-----TIC TAC TOE---GAME--

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        print("----------")
        for row in [self.board[i:i+3] for i in range(0,9,3)]:    #padarem cikla, kuris eis per kiekviena masyvo elementa, i:i+3 reiskia kad bus trijose vietose
            print("|", end="")
            for cell in row:
                print(f"{cell} |", end="")
            print("\n----------")    #\n reiskia new line

    def make_move(self, position):     #kiekviena karta kai irasome skaiciu, ta lenta atsinaujins automatiskai.
        if  self.board [position] == " ":    #reiskia tuscia vieta
            self.board[position] = self.current_player
            self.current_player = "0" if self.current_player == "X" else "X"    #palyginsime X, jei tai bus 0, kad nedubliuoti tu paciu vietu, .Po kiekvieno ejimo, turime keisti zenkla
        else:
            print("Invalid move, try again")


    def check_winner(self):
        winning_combinations = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in winning_combinations:
            a, b, c = combo                                      #destructive assignment, leis priskirti atskirus saraso elementus, atitinkama kintamajam, abc bus konkretus kintamieji kurie atitiks
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        if " " not in self.board:
            return "Tie"
        return None
    def play_game(self):
        print("Welcome")
        self.print_board()  #funcija visada turi tureti skliaustus

        while True:
            position = int(input("player " + self.current_player + " make your move (0-8): "))
            self.make_move(position)
            self.print_board()

            winner = self.check_winner()
            if winner:
                if winner == "Tie":
                    print("It's a tie")
                else:
                    print("Player " + winner + " wins")
                break

game = TicTacToe()
game.play_game()