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

        if (i + 1) % 10 == 0 and i > 1:
            print()
            # print("|", end="")


print(
    "Welcome To Mine Sweeper!\nSelect any number from the board, if there is a bomb at your selected location the game is over but if not you can continue playng.\nNote:Do not enter zero for numbers smaller than 10"
)


def revealBombs(board, location):
    def right():
        # to right
        if board[location + 1] in bombs:
            board[location] = " X"
        else:
            board[location] = "  "

    def left():
        # to left
        if board[location - 2] in bombs:
            board[location - 2] = " X"
        else:
            board[location - 2] = "  "

    def top():
        # to top
        if board[location - 9] in bombs:
            board[location - 11] = " X"
        else:
            board[location - 11] = "  "

    def down():
        # to bottom
        if board[location + 9] in bombs:
            board[location + 9] = " X"
        else:
            board[location + 9] = "  "

    # location at centre--------------------------------------------
    if location > 11 and location < 90:
        # to right
        right()
        # to bottom
        down()
        # to top
        top()
        # to left
        left()

        return

    # location left wall----------------------------------
    elif location % 10 == 1:
        if location == 1:
            # to right
            right()

            # to bottom
            down()
        elif location == 91:
            # to right
            right()
            # to top
            top()
        else:
            # to right
            right()
            # to bottom
            down()
            # to top
            top()
        return

    # location top wall-------------------------------------
    elif location // 10 <= 1:
        # to right
        right()
        # to bottom
        down()

        # to left
        left()
        
        return

    # location right wall ----------------------------
    elif location % 10 == 0:
        if location == 10:
            # to left
            left()
            # to bottom
            down()
        elif location == 100:
            # to left
            left()

            # to top
            top()
        else:
            # to right
            right()
            # to bottom
            down()
            # to top
            top()
        return

    # location bottom wall
    else:
        # to right
        right()
        # to top
        top()
        # to left
        left()
        
        return


# bomb_density = input('Choose difficulty:\nEasy(10bombs)\nMedium(20 Bombs)\nImpossible(40 Bombs)')

printBoard(board)

bombs = choices(board, k=20)

chances = 3

while chances > 0:
    location = int(input("\nEnter your choice: "))
    if location in bombs:
        chances -= 1
        board[location - 1] = " X"
        printBoard(board)
        print("Oppsie, you stepped on a bomb.\nChances left: ", chances)

    else:
        board[location - 1] = "  "
        revealBombs(board, location)
        printBoard(board)

print("Game over!")
