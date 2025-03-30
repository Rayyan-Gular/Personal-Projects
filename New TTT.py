import pygame, sys, time, ctypes
pygame.init()
pygame.font.init()
ctypes.windll.user32.SetProcessDPIAware()

size = width, height = 500, 600
x, y = 'x', 'o'
score = [0,0,0]
bufferSpace, thirdWidth, twoThirdWidth= height - width, 1/3 * width, 2/3 * width
lineColour, circleColour, crossColour = 'gray10', 'red', 'blue'
endGameFont = pygame.font.SysFont('segoeprint', round(width*0.18))
scoreFont = pygame.font.SysFont('Comic Sans MS', round(width*0.07))
boardPositions = [(0,bufferSpace), (thirdWidth,bufferSpace), (twoThirdWidth,bufferSpace), 
                  (0,bufferSpace+thirdWidth), (thirdWidth,bufferSpace+thirdWidth), (twoThirdWidth,bufferSpace+thirdWidth), 
                  (0,bufferSpace+twoThirdWidth), (thirdWidth,bufferSpace+twoThirdWidth), (twoThirdWidth,bufferSpace+twoThirdWidth)]

class TTTBoard:
    def __init__(self):
        self.board = [''] * 9
        self.currentPlayer, self.nextPlayer = x, y
        screen.fill('azure3')
        pygame.draw.line(screen, lineColour, (thirdWidth,0), (thirdWidth, height),3)
        pygame.draw.line(screen, lineColour, (twoThirdWidth,0), (twoThirdWidth, height),3)
        pygame.draw.line(screen, lineColour, (0,thirdWidth+bufferSpace), (width,thirdWidth+bufferSpace), 3)
        pygame.draw.line(screen, lineColour, (0,twoThirdWidth+bufferSpace), (width,twoThirdWidth+bufferSpace), 3)
        pygame.draw.line(screen, lineColour, (0,bufferSpace), (width,bufferSpace), 2)
        screen.blit(scoreFont.render((f'X:{' '*10}Draw:{' '*10}O:'), True, 'gray10'), (65,-3))
        screen.blit(scoreFont.render((f'{score[0]}{' '*14}{score[2]}{' '*15}{score[1]}'), True, 'gray10'), (70,40))
    
    def validMoveCheck(self, position):
        if self.board[position] == '':
            return True
    
    def updateBoard(self, position):
        self.board[position] = self.currentPlayer
        if self.currentPlayer == 'o':
            pygame.draw.circle(screen, circleColour,
                              (boardPositions[position][0]+thirdWidth/2,boardPositions[position][1]+thirdWidth/2),
                              (thirdWidth/2) - 15, 5)
        else:
            pygame.draw.line(screen, crossColour, 
                            (boardPositions[position][0]+20,boardPositions[position][1]+20),
                            (boardPositions[position][0]+thirdWidth-20,boardPositions[position][1]+thirdWidth-20), 6)
            pygame.draw.line(screen, crossColour,
                            (boardPositions[position][0]+20, boardPositions[position][1]+thirdWidth-20),
                            (boardPositions[position][0]+thirdWidth-20,boardPositions[position][1]+20),6)
        self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer
        pygame.display.flip()

    def winDrawCheck(self):
        tempBoard, tempPlayer = self.board, self.nextPlayer
        if (tempBoard[0]==tempBoard[1]==tempBoard[2]==tempPlayer or
            tempBoard[3]==tempBoard[4]==tempBoard[5]==tempPlayer or
            tempBoard[6]==tempBoard[7]==tempBoard[8]==tempPlayer or
            tempBoard[0]==tempBoard[3]==tempBoard[6]==tempPlayer or
            tempBoard[1]==tempBoard[4]==tempBoard[7]==tempPlayer or
            tempBoard[2]==tempBoard[5]==tempBoard[8]==tempPlayer or
            tempBoard[0]==tempBoard[4]==tempBoard[8]==tempPlayer or
            tempBoard[2]==tempBoard[4]==tempBoard[6]==tempPlayer):

            if tempPlayer == 'x':
                score[0] += 1
            else:
                score[1] += 1
            time.sleep(0.7)
            screen.fill('azure3')
            screen.blit(endGameFont.render((tempPlayer.upper() + ' Won!!!'), True, 'gray10'), (50,200))
            pygame.display.flip()
            time.sleep(2)
            theBoard.__init__()
        elif '' not in tempBoard:
            score[2] += 1
            time.sleep(0.7)
            screen.fill('azure3')
            screen.blit(endGameFont.render('Its a draw', True, 'gray10'), (15,200))
            pygame.display.flip()
            time.sleep(2)
            theBoard.__init__()

screen = pygame.display.set_mode((size))
pygame.display.set_caption('Tic Tac Toe!')
theBoard = TTTBoard()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        if pygame.mouse.get_pressed()[0]:
            mouseClick = pygame.mouse.get_pos()
            for cord in range(9):
                if mouseClick[1] < bufferSpace:
                    break
                elif (mouseClick[0] < boardPositions[cord][0] + thirdWidth
                    and mouseClick[1] < boardPositions[cord][1] + thirdWidth):

                    if theBoard.validMoveCheck(cord):
                        theBoard.updateBoard(cord)
                        break
                    else:
                        break
            theBoard.winDrawCheck()
            time.sleep(0.3)

        pygame.display.flip()
    
if __name__ == '__main__':
    main()
