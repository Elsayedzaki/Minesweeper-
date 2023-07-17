from tkinter import Button,Label
import random
import settings
import ctypes

class Cell:
    all = []
    stop_cells = False
    count_cells = 0
    lbl_object = None
    def __init__(self,x,y,is_mine = False):
        self.cell_btn_object = None
        self.cell_mine_cantidate = False
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.is_opened = False
        Cell.count_cells += 1
        Cell.all.append(self)

    def creat_cells(self,location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        if not self.is_mine:
            btn.bind('<Button-1>', self.left_click_mouse ) # Left Click
            btn.bind('<Button-3>', self.right_click_mouse ) # Right Click
            self.cell_btn_object = btn
        else:
            self.cell_btn_object.unbind('<Button-1>')
            self.cell_btn_object.unbind('<Button-3>') 
    @staticmethod
    def counter_lbl_object(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f'Number Cells: {Cell.count_cells}',
            font=('Roman',20)
        )
        Cell.lbl_object = lbl

    def left_click_mouse(self, event):
        if self.is_mine:
            self.show_mine()
            Cell.stop_game()
            Cell.show_all_mines()
        else:
            if not self.is_opened:
                Cell.count_cells -= 1
                self.cell_btn_object.configure(text=self.show_cell_surounding_length) 
                if Cell.lbl_object:
                    Cell.lbl_object.configure(text=f'Number Cells: {Cell.count_cells}')

            if Cell.count_cells == settings.mines_count:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)

            self.is_opened = True
            # Cell.count_other_cells()
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>') 

    def right_click_mouse(self,event):
        if not self.cell_mine_cantidate:
            self.cell_btn_object.configure(bg='orange')
            self.cell_btn_object.unbind('<Button-1>')
            self.cell_mine_cantidate = True
            if Cell.stop_cells:
                if self.is_mine:
                    self.cell_btn_object.configure(bg='red')
                else:
                    self.cell_btn_object.configure(bg='SystemButtonFace')
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.cell_btn_object.bind('<Button-1>', self.left_click_mouse )
            self.cell_mine_cantidate = False

    @property
    def surounding_cell(self):
        list_surounded_cell = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x , self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y + 1),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x - 1, self.y)
        ]
        list_surounded_cell = [filtered_list for filtered_list in list_surounded_cell if filtered_list != None]
        return list_surounded_cell

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine','Game Over',0)
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>') 

    @property
    def show_cell_surounding_length(self):
        cell_mines_count = 0
        for mine_cell in self.surounding_cell:
            if mine_cell.is_mine:
                cell_mines_count += 1
        return cell_mines_count
    
    @staticmethod
    def stop_game():
        for cell in Cell.all:
            if cell.is_mine:
                for cell_1 in Cell.all:
                    cell_1.cell_btn_object.unbind('<Button-1>')
                    cell_1.cell_btn_object.unbind('<Button-3>') 

    @staticmethod
    def show_all_mines():
        mines = [cell for cell in Cell.all if cell.is_mine]
        for red_mines in mines:
            red_mines.cell_btn_object.configure(bg='red')
            
    @staticmethod
    def randomize_mines():
        random_cells = random.sample(Cell.all,settings.mines_count)
        for random_cell in random_cells:
            random_cell.is_mine = True

    def __repr__(self):
        return f'Cell of {self.x}, {self.y}'