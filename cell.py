from tkinter import Button
import settings
import random

class Cell:
    all = [] #all of our instances in one place
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.clicked = False
        #Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self,location):
        btn = Button(location,
                     # text=f'{self.x},{self.y}',
                     width=int(12*6/settings.GRID_SIZE),
                     height=int(4*6/settings.GRID_SIZE))
        #left-click
        btn.bind('<Button-1>',self.left_click_actions) #only reference of method
        #right-click
        btn.bind('<Button-3>',self.right_click_actions) #only reference of method
        self.cell_btn_object = btn

    #When cell clicked
    def left_click_actions(self,event):
        # print(event)
        # print('I am left click')
        self.clicked = True

        if self.is_mine:
            print('You loose!')
            self.show_mine()
            for cell in Cell.all:
                cell.cell_btn_object.unbind("<Button-1>")
        else:
            self.show_cell()

    def right_click_actions(self,event):
        print(event)
        print('I am right click')

    @property
    def surrounded_cells(self):
        cells = [
            self.find_cell_in_list(self.x-1,self.y-1),
            self.find_cell_in_list(self.x-1,self.y),
            self.find_cell_in_list(self.x-1,self.y+1),
            self.find_cell_in_list(self.x,self.y-1),
            self.find_cell_in_list(self.x,self.y+1),
            self.find_cell_in_list(self.x+1,self.y-1),
            self.find_cell_in_list(self.x+1,self.y),
            self.find_cell_in_list(self.x+1,self.y+1),
        ]
        cells = [ cell for cell in cells if cell is not None and cell.is_mine]

        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    #display number in cell
    def show_cell(self,method = 2):
        self.cell_btn_object.unbind("<Button-1>")
        # tutorial method
        if method == 1:
            self.cell_btn_object.configure(text=f'{self.surrounded_cells_mines_length}')
            if self.surrounded_cells_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
        #my method
        else:
            x_back = (self.x - 1 if self.x > 0
            else self.x)
            x_forward = (self.x + 1 if self.x < settings.GRID_SIZE-1
                         else self.x)
            y_back = (self.y - 1 if self.y > 0
            else self.y)
            y_forward = (self.y + 1 if self.y <  settings.GRID_SIZE-1
                         else self.y)
            number_of_mines = 0
            cells = []
            # print('from: ',self.x,self.y)
            # print('rage x: ',x_back,x_forward)
            # print('range y: ',y_back,y_forward)
            for x in range(x_back,x_forward + 1):
                for y in range(y_back,y_forward + 1):
                    # print(x,y)
                    if x != self.x or y !=self.y:
                        cell = self.find_cell_in_list(x,y,method)
                        cells.append(cell)
                        # print(cell)
                        if cell.is_mine:
                            number_of_mines +=  1

            self.cell_btn_object.configure(text=f'{number_of_mines}')

            if number_of_mines == 0 and self.clicked:
                for cell in cells:
                        cell.show_cell()



    def find_cell_in_list(self,x,y,method = 1):
        if method == 1:
            for c in Cell.all:
                    if c.x == x and c.y == y:
                        cell = c
                        return  cell #
        else:
            return [c for c in Cell.all if c.x == x and c.y == y][0]

    #Interrupt game and display message that player lost
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')


    @staticmethod
    def randomize_mines():
        # my_list = ['Jim', 'Karen', 'Pam']
        # picked_names = random.sample(my_list,2) #pick random elements from
        # print(picked_names)
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self): #print(cell.all)
        return f"Cell({self.x},{self.y}), "