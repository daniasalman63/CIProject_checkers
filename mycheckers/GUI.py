import tkinter as tk

class CheckersBoard:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.colors = {
            "dark": "#2C3E50",
            "light": "#EAEAEA"
        }

        # draw the checkerboard
        for row in range(8):
            for col in range(8):
                if (row+col) % 2 == 0:
                    self.canvas.create_rectangle(col*50, row*50, (col+1)*50, (row+1)*50, fill=self.colors['light'])
                else:
                    self.canvas.create_rectangle(col*50, row*50, (col+1)*50, (row+1)*50, fill=self.colors['dark'])

    # function to update the pieces on the board
    def update_board(self, array):
        self.canvas.delete('piece')  # clear any previous pieces on the board
        for row in range(8):
            for col in range(8):
                if array[row][col] == 'red':
                    self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='red', tags='piece')
                elif array[row][col] == 'white':
                    self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='white', tags='piece')
                elif array[row][col] == 'K':
                    self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='red', tags='piece')
                    self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=90, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
                    self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=270, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
                elif array[row][col] == '-K':
                    self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill='white', tags='piece')
                    self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=90, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')
                    self.canvas.create_arc(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, start=270, extent=180, style=tk.ARC, width=4, outline='yellow', tags='piece')


root = tk.Tk()
board = CheckersBoard(root)
board.update_board(array = [
['white', 0, 'white', 0, 'white', 0, 'white', 0],
[0, 'white', 0, 'white', 0, 'white', 0, 'white'],
['white', 0, '-K', 0, 'white', 0, 'white', 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 'red', 0, 'red', 0, 'red', 0, 'red'],
['red', 0, 'red', 0, 'red', 0, '-K', 0],
[0, 'red', 0, 'red', 0, 'red', 0, 'red']
])
root.mainloop()
