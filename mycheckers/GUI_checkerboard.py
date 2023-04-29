 
import pygame

class Checkerboard:
    def __init__(self, array, valid_moves=None):
        self.screen_size = (400, 400)
        self.square_size = 50
        self.array = array
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.colors = {'red': (255, 0, 0), 'white': (255, 255, 255)}
        self.valid_moves = valid_moves
        pygame.init()
        self.highlight = (255, 255, 0)

        self.screen = pygame.display.set_mode(self.screen_size)
        self.font = pygame.font.SysFont(None, 30)

        self.update_board(array, valid_moves)
        # self.run()
    def update_board(self, board, valid_moves=None):
        if valid_moves:
            self.moves = valid_moves.keys()
            for y in range(8):
                for x in range(8):
                    color = (234, 234, 234)
                    if (x + y) % 2 == 1:
                        color = (44, 62, 80)
                    pygame.draw.rect(self.screen, color, pygame.Rect(x * self.square_size, y * self.square_size, self.square_size, self.square_size))

                    if board[y][x] != 0:
                        if board[y][x].color == 'red':
                            pygame.draw.circle(self.screen, 'red', (int((x + 0.5) * self.square_size), int((y + 0.5) * self.square_size)), int(self.square_size * 0.4))
                            if board[y][x].king == True:
                                pygame.draw.circle(self.screen,(255,255,0),(x*50+25,y*50+25),25,5)
                        elif board[y][x].color == 'white':
                            pygame.draw.circle(self.screen, 'white', (int((x + 0.5) * self.square_size), int((y + 0.5) * self.square_size)), int(self.square_size * 0.4))
                            if board[y][x].king == True:
                                pygame.draw.circle(self.screen,(255,255,0),(x*50+25,y*50+25),25,5)
            for i in self.moves:
                    pygame.draw.rect(self.screen, self.highlight, pygame.Rect(i[1] * self.square_size, i[0] * self.square_size, self.square_size, self.square_size))

                

        else:
            for y in range(8):
                for x in range(8):
                    color = (234, 234, 234)
                    if (x + y) % 2 == 1:
                        color = (44, 62, 80)
                    pygame.draw.rect(self.screen, color, pygame.Rect(x * self.square_size, y * self.square_size, self.square_size, self.square_size))
                    if board[y][x] != 0:
                        if board[y][x].color == 'red':
                            pygame.draw.circle(self.screen, 'red', (int((x + 0.5) * self.square_size), int((y + 0.5) * self.square_size)), int(self.square_size * 0.4))
                            if board[y][x].king == True:
                                pygame.draw.circle(self.screen,(255,255,0),(x*50+25,y*50+25),25,5)
                        elif board[y][x].color == 'white':
                            pygame.draw.circle(self.screen, 'white', (int((x + 0.5) * self.square_size), int((y + 0.5) * self.square_size)), int(self.square_size * 0.4))
                            if board[y][x].king == True:
                                pygame.draw.circle(self.screen,(255,255,0),(x*50+25,y*50+25),25,5)
                

        pygame.display.flip()

    def get_clicked_piece(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.row = self.y // self.square_size
        self.col = self.x // self.square_size
        
        return self.row, self.col

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_piece = self.get_clicked_piece()
                    if clicked_piece is not None:
                        print(f"you have selected the piece at ({self.row},{self.col})")
                        return self.row, self.col
                    


        pygame.quit()

# if __name__ == '__main__':
    
     
#     array = [[0, 'white', 0, 'white', 0, 'white', 0, 'white'],
#          ['white', 0, 'white', 0, 'white', 0, 'white', 0],
#          [0, 'white', 0, 'white', 0, 'white', 0, 'white'],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          ['red', 0, 'red', 0, 'red', 0, 'red', 0],
#          [0, 'red', 0, 'red', 0, 'red', 0, 'red'],
#          ['red', 0, 'red', 0, 'red', 0, 'red', 0]]

#     board = Checkerboard(array)
#     board.run()