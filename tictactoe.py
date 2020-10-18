board = [[' ', ' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']
         ]
Already = []
Taken = []

class Player:
    def __init__(self , name  , Taken):
        self.name = name
        run = True
        while run:
            if 'X' in Taken:
                self.pawn = 'Y'
                run = False
            elif 'Y' in Taken:
                self.pawn = 'X'
                run = False
            else:
                self.pawn = input(f"Enter 'X' or 'Y' {name}: ")
                self.pawn = self.pawn.capitalize()
                if self.pawn == 'X':
                    Taken.append(self.pawn)
                    run = False
                elif self.pawn == 'Y':
                    Taken.append(self.pawn)
                    run = False
                else:
                    print("Please enter X or Y")
    def check(self , board):
        for i in range(len(board)):
            if board[i][0] == self.pawn and board[i][1] == self.pawn and board[i][2] == self.pawn:
                return True
        for i in range(len(board)):
            if board[0][i] == self.pawn and board[1][i] == self.pawn and board[2][i] == self.pawn:
                return True
        for i in range(1):
            if board[i][i] == self.pawn and board[1][1] == self.pawn and board[2][2] == self.pawn:
                return True
        for i in range(1):
            if board[0][2] == self.pawn and board[1][1] == self.pawn and board[2][0] == self.pawn:
                return True
        return None
            
class Main_board(object):
    def game_board(self , board):
        for i in range(len(board)):
            if i!=0:
                print("------")
            for j in range(len(board[0])):
                if j!=0:
                    print("|" , end = '')
                if j == 2:
                    print(board[i][j])
                else:
                    print(board[i][j] , end = '')
    def enter_position(self , board , Already):
        run = True
        while run:
            try:
                self.position = int(input("Enter a number from 1-9: "))
            except:
                print("Please enter a number")
            else:
                if self.position >0 and self.position < 10:
                    if self.position not in Already:
                        Already.append(self.position)
                        run = False
                    else:
                        print("Position Already occupied..try another number")
                else:
                    print("Please enter a number from 1-9")
    def place_hold(self , board , choise):
        if self.position > 6 and self.position < 10:
            bo = board[2]
            bo[self.position - 7] = choise
        elif self.position > 3 and self.position < 7:
            bo = board[1]
            bo[self.position - 4] = choise
        else:
            bo = board[0]
            bo[self.position - 1] = choise

print("!!!!RULES!!!!!")
print("Each box represents a number")
print("For example: \n\n1|2|3\n-----\n4|5|6\n-----\n7|8|9")
print('\n')
name1 = input("P1 name:")
n1 = name1.capitalize()
name2 = input("P2 name: ")
n2 = name2.capitalize()
P1 = Player(n1 , Taken)
P2 = Player(n2 , Taken)
print('\n')
print(f"{n1} is {P1.pawn} and {n2} is {P2.pawn}")

running = True
while running:
    if len(Already) < 9:
        main = Main_board()
        main.game_board(board)
        main.enter_position(board , Already)
        main.place_hold(board , P1.pawn)
        if P1.check(board):
            main.game_board(board)
            print(f"{n1} Wins!!")
            break
    else:
        print("The game is drawn")
        break
    if len(Already) < 9:
        main = Main_board()
        main.game_board(board)
        main.enter_position(board , Already)
        main.place_hold(board , P2.pawn)
        if P1.check(board):
            main.game_board(board)
            print(f"{n2} Wins!!")
            break
    else:
        print("The game is drawn")
        break
