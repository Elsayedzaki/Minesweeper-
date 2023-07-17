from tkinter import *
import settings
from oop import Cell
import tkinter.font as tkfont
root = Tk()
# The setting of the window
root.configure(bg='black')
root.geometry(f'{settings.width}x{settings.hight}')
root.title('Minesweeper Game')
root.resizable(False,False)
# the top 
top_frame = Frame(root,
                  bg='black',
                  width=settings.width,
                  height=settings.height_per(25))
top_frame.place(x=0,y=0)
# beside
left_frame = Frame(root,
                   bg='black',
                   width=settings.width_per(25),
                   height=settings.height_per(75))
left_frame.place(x=0,y=settings.height_per(25))
# The center
center_frame = Frame(root,
                     bg='black',
                     width=settings.width_per(75),
                     height=settings.height_per(75))
center_frame.place(x=settings.width_per(25),
                   y=settings.height_per(25))
bold_font = tkfont.Font(weight='bold')
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('Roman',50)
)
game_title.place(x=settings.width_per(27),y=50)


# To generate the cells 
for x in range(settings.gird_count):
    for y in range(settings.gird_count):
        cell = Cell(x,y)
        cell.creat_cells(center_frame)
        cell.cell_btn_object.grid(
            column=x,
            row=y
        )
# Cell.count_other_cells()
counter_lbl = Cell.counter_lbl_object(left_frame)
Cell.lbl_object.place(x=35,y=settings.height_per(20))

Cell.randomize_mines()
# The displaying of the window
root.mainloop()


