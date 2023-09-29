from random import choices

board = [x for x in range(1, 101)]


def printBoard(board):
    print()
    for i in range(len(board)):
        if i % 2 == 0:
            print("|", end="")
        if i < 9 and type(board[i]) == int:
            print(f" 0{board[i]} ", end="")
        else:
            print(f" {board[i]} ", end="")
        if i % 2 == 0:
            print("|", end="")

        if (i+1) % 10 == 0 and i > 1:
            print()
            # print("|", end="")


print(
    "Welcome To Mine Sweeper!\nSelect any number from the board, if there is a bomb at your selected location the game is over but if not you can continue playng.\nNote:Do not enter zero for numbers smaller than 10"
)

def revealBombs(board):
    pass

# bomb_density = input('Choose difficulty:\nEasy(10bombs)\nMedium(20 Bombs)\nImpossible(40 Bombs)')

printBoard(board)

bombs = choices(board, k=20)

while True:
    location = int(input("\nEnter your choice: "))
    if location in bombs:
        print("Oppsie, you stepped on a bomb.\nGame Over!")
        break
    else:
        board[location - 1] = "  "
        printBoard(board)
