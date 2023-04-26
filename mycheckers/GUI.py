import tkinter as tk
from board import *
from game import Game


class CheckersBoard:
    def __init__(self, master, array):
        self.master = master
        self.canvas = tk.Canvas(master,width=400, height=400)
        self.canvas.pack()
        self.square_size = 50
        self.colors = {
            "dark": "#2C3E50",
            "light": "#EAEAEA"
        }

        self.selected_piece = None
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.array = array
        

        # draw the checkerboard
        for row in range(8):
            for col in range(8):
                if (row+col) % 2 == 0:
                    self.canvas.create_rectangle(col*50, row*50, (col+1)*50, (row+1)*50, fill=self.colors['light'])
                else:
                    self.canvas.create_rectangle(col*50, row*50, (col+1)*50, (row+1)*50, fill=self.colors['dark'])

    def update_board(self, array):
         
        self.canvas.delete('piece')  # clear any previous pieces on the board
        for row in range(8):
            for col in range(8):
                if array[row][col] != 0:

                    if array[row][col].color == 'red':
                        self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='red', tags='piece')
                        if array[row][col].king == True:
                            self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='red', tags='piece')
                            self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=90, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
                            self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=270, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
                    elif array[row][col].color == 'white':
                        self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='white', tags='piece')
                        if array[row][col].king == True:
                            self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='white', tags='piece')
                            self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=90, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
                            self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=270, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
  

    def on_square_clicked(self, event): #selects and tells location of piece
        
        row = event.y // self.square_size
        col = event.x // self.square_size
        piece = self.array[row][col]

        if self.selected_piece == None:
            if piece is not None:
                self.selected_piece = piece
                print(f"you have selected the piece at ({row},{col})")

        else:
            if piece in self._move(self.selected_piece):
                print('it is valid move')
                self.obj._move(row, col)
                self.selected_piece = None
            else:
                print('not valid move')
                self.selected_piece = None



        # piece = self.array[row][col]
        # if piece:
        #     self.selected_piece = (row, col)
        #     print(f"Selected {piece} at ({row}, {col})")
        # else:
        #     print(f"No piece at ({row}, {col})")

            
            # if self.selected_piece:
            #     old_row, old_col = self.selected_piece

            #     if self.is_valid(old_row, old_col, row, col):
            #         print(f"Valid move from ({old_row}, {old_col}) to ({row}, {col})")
            #         # update board
            #         self.array[row][col] = self.array[old_row][old_col]
            #         self.array[old_row][old_col] = None
            #         # clear selection
            #         self.selected_piece = None
            #         # redraw board
            #         self.update_board(self.array)
            #     else:
            #         print(f"Invalid move from ({old_row}, {old_col}) to ({row}, {col})")
            #         # clear selection
            #         self.selected_piece = None




# root = tk.Tk()
# array = [
# ['white', 0, 'white', 0, 'white', 0, 'white', 0],
# [0, 'white', 0, 'white', 0, 'white', 0, 'white'],
# ['white', 0, 'white', 0, 'white', 0, 'white', 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 'red', 0, 'red', 0, 'red', 0, 'red'],
# ['red', 0, 'red', 0, 'red', 0, 'red', 0],
# [0, 'red', 0, 'red', 0, 'red', 0, 'red']
# ]
# board = CheckersBoard(root, array)
# board.update_board(array)
# root.mainloop()

