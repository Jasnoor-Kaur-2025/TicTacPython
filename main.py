import numpy as np
import random

grid = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])

dictPlayers = {"Human": "X", "Computer": "O"}
ourTurn = True
game = True

winPos = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
          [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
          [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]

def checkWin(symbol):
    for bundle in winPos:
        if all(grid[r][c] == symbol for r, c in bundle):
            return True
    return False

def checkCompWins():
    for bundle in winPos:
        positions = [grid[r][c] for r, c in bundle]
        if positions.count("O") == 2 and "_" in positions:
            r, c = bundle[positions.index("_")]
            grid[r][c] = "O"
            return True
    return False

def sabotagePlayer():
    for bundle in winPos:
        positions = [grid[r][c] for r, c in bundle]
        if positions.count("X") == 2 and "_" in positions:
            r, c = bundle[positions.index("_")]
            grid[r][c] = "O"
            return True
    return False

def checkDraw():
    return "_" not in grid

def printGrid():
    print("\n".join([" ".join(row) for row in grid]))

while game:
    printGrid()
    
    if checkDraw():
        print("THE GAME WAS A DRAW!")
        break

    if ourTurn:
        try:
            rowInd = int(input("Enter row (1-3): ")) - 1
            colInd = int(input("Enter column (1-3): ")) - 1

            if 0 <= rowInd < 3 and 0 <= colInd < 3 and grid[rowInd][colInd] == "_":
                grid[rowInd][colInd] = "X"
            else:
                print("Invalid input. Try again.")
                continue

            if checkWin("X"):
                printGrid()
                print("YOU WON!")
                break

            ourTurn = False
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    else:
        print("Computer's turn...")
        if not checkCompWins() and not sabotagePlayer():
            empty_cells = [(r, c) for r in range(3) for c in range(3) if grid[r][c] == "_"]
            r, c = random.choice(empty_cells)
            grid[r][c] = "O"

        if checkWin("O"):
            printGrid()
            print("COMPUTER WON!")
            break

        print("Your turn now!")
        ourTurn = True

