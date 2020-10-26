import pygame
pygame.init()


screen = pygame.display.set_mode((170, 170))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(pygame.Color(0, 0, 0))

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

x = 5
y = 5
px = 55
height = 50
width = 50
margin = 5
rowGrid = 0
colGrid = 0
rowCol = 0
playerX = True
game = True
for col in range(3):
    for row in range(3):
        # print(row)
        #print(x + px*row)
        pygame.draw.rect(screen, (250, 250, 250),
                         ((x + px*row), (y + px*col), width, height))


def drawX(a, b):
    pygame.draw.line(screen, (0, 0, 0), (a, b), ((a+40), (b+40)), 5)
    pygame.draw.line(screen, (0, 0, 0), ((a+40), b), (a, (b+40)), 5)


def drawO(a, b):
    pygame.draw.circle(screen, (0, 0, 0), (a, b), 20, 5)


def assignDim(rowCol, pos, identifier):
    global row
    global col
    if pos > 0 and pos < 55:
        rowCol = 0
    elif pos > 55 and pos < 110:
        rowCol = 1
    elif pos > 110 and pos < 170:
        rowCol = 2
    if identifier == 0:
        row = rowCol
    if identifier == 1:
        col = rowCol


def drawXO(row, col):
    global playerX
    if grid[col][row] == 0:
        if(playerX):
            grid[col][row] = 1
            drawX(row*55 + 10, col*55+10)
        else:
            grid[col][row] = 2
            drawO(row*55 + 30, col*55+30)
        playerX = not playerX


def validateWin():
    global grid
    global game
    rowMatch = False
    winner = 0
    for row in range(3):
        if(grid[row][0] == grid[row][1] == grid[row][2] and grid[row][2] != 0):
            rowMatch = True
            winner = grid[row][0]

        elif(grid[0][row] == grid[1][row] == grid[2][row] and grid[2][row] != 0):
            rowMatch = True
            winner = grid[0][row]
        elif(grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]) and grid[1][1] != 0:
            rowMatch = True
            winner = grid[1][1]
    if rowMatch == True:

        winnerXO = "X" if winner == 1 else "O"
        print(winnerXO, " has won!")
        game = False
    else:
        foundZero = False
        for row in range(3):
            for col in range(3):
                if(grid[row][col] == 0):
                    foundZero = True
        if(not foundZero):
            print("Game Tie")
            game = False


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and game:
                pos = pygame.mouse.get_pos()
                assignDim(rowGrid, pos[0], 0)
                assignDim(colGrid, pos[1], 1)
                drawXO(row, col)
                validateWin()
                print(grid)
                # scale for X : 10 scale for O : 30

    clock.tick(60)
    pygame.display.update()

pygame.quit()
