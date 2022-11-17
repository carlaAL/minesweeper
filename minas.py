from tkinter import *
from cell import  Cell

import settings
import utils

root = Tk()
# window configuration overrides
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # WxH
root.title('BuscaMinas')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)  # 720/4
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# Create button with tkinter
# btn1 = Button( center_frame, bg='blue', text='First button')
# btn1.place(x=0,y=0)

# use cell class
# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(column=0,row=0)
#
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(column=0,row=1)

# Create buttons for mines
def init_cells():
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):

            cell = Cell(x,y)
            cell.create_btn_object(center_frame)
            cell.cell_btn_object.grid(column=x,row=y)

    Cell.randomize_mines()


# print(len(Cell.all))
# print(Cell.all)

# Restart game function
def restart(event):
    for index in range(len(Cell.all)):
        Cell.all.pop()
    init_cells()



# Create button with tkinter
btn_restart = Button( left_frame, bg='blue', text='Restart game')
btn_restart.place(x=utils.width_prct(15),y=0)
btn_restart.bind('<Button-1>', restart)

# Init game
init_cells()


# Run window
root.mainloop()
