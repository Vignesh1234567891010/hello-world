import pygame
from parameters import display
from effects import print_text

pygame.init()


class Resource:
    def __init__(self, name, image_path):
        self.name = name
        self.amount = 0
        self.image = pygame.image.load(image_path)


class Inventory:
    def __init__(self):
        self.resources = {
            "coal": Resource('coal', 'D:\Projects\Python\Git\Dino\images\Effects\Coal.png'),
            "emerald": Resource('coal', 'D:\Projects\Python\Git\Dino\images\Effects\Emerald.png'),
            "ruby": Resource('coal', 'D:\Projects\Python\Git\Dino\images\Effects\Ruby.png')
        }

        self.inventory_panel = [None] * 4
        self.whole_inventory = [None] * 8
        self.start_cell = 0
        self.end_cell = 0

    def get_amount(self, name):
        try:
            return self.resources[name].amount
        except KeyError:
            return -1

    def increase(self, name):
        try:
            self.resources[name].amount += 1
            self.update()
            print(self.whole_inventory)
        except KeyError:
            print("Error increasing")

    def update(self):
        for name, resource in self.resources.items():
            if resource.amount != 0 and resource not in self.whole_inventory and resource not in self.inventory_panel:
                self.whole_inventory.insert(self.whole_inventory.index(None), resource)
                self.whole_inventory.remove(None)

    def draw_whole(self):
        x = y = 60
        side = 80
        step = 100

        pygame.draw.rect(display, (182, 195, 206), (x - 20, y - 20, 420, 220))

        for cell in self.whole_inventory:
            pygame.draw.rect(display, (200, 215, 227), (x, y, side, side))
            if cell is not None:
                display.blit(cell.image, (x + 15, y + 5))
                print_text(str(cell.amount), x + 30, y + 60, font_size=15)
            x += step

            if x == 460:
                x = 60
                y += step

    def draw_panel(self):
        x = 200
        y = 510
        side = 80
        step = 100

        for cell in self.inventory_panel:
            pygame.draw.rect(display, (200, 215, 227), (x, y, side, side))
            if cell is not None:
                display.blit(cell.image, (x + 15, y + 5))
                print_text(str(cell.amount), x + 30, y + 60, font_size=15)

            x += step

            if x == 460:
                x = 60
                y += step

    def set_start_cell(self, mouse_x, mouse_y):
        start_x = start_y = 60
        step = 100
        side = 80

        for y in range(0, 2):
            for x in range(0, 4):
                cell_x = start_x + x * step
                cell_y = start_y + y * step

                if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                    self.start_cell = y * 4 + x
                    print("Start" + str(y * 4 + x))
                    return

            start_x = 200
            start_y = 510

            for x in range(0, 4):
                cell_x = start_x + x * step
                cell_y = start_y

                if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                    self.start_cell = 8 + x
                    print("Start" + str(8 + x))
                    # self.swap_cells()
                    return

    def set_end_cell(self, mouse_x, mouse_y):
        start_x = start_y = 60
        step = 100
        side = 80

        for y in range(0, 2):
            for x in range(0, 4):
                cell_x = start_x + x * step
                cell_y = start_y + y * step

                if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                    self.end_cell = y * 4 + x
                    print("End" + str(y * 4 + x))
                    self.swap_cells()
                    return

            start_x = 200
            start_y = 510

            for x in range(0, 4):
                cell_x = start_x + x * step
                cell_y = start_y

                if cell_x <= mouse_x <= cell_x + side and cell_y <= mouse_y <= cell_y + side:
                    self.end_cell = 8 + x
                    print("End" + str(8 + x))
                    self.swap_cells()
                    return

    def swap_cells(self):
        if self.end_cell < 8:
            temp = self.whole_inventory[self.end_cell]
            if self.start_cell < 8:
                self.whole_inventory[self.end_cell] = self.whole_inventory[self.start_cell]
                self.whole_inventory[self.start_cell] = temp
            else:
                self.start_cell -= 8
                self.whole_inventory[self.end_cell] = self.inventory_panel[self.start_cell]
                self.inventory_panel[self.start_cell] = temp
        else:
            self.end_cell -= 8
            temp = self.inventory_panel[self.end_cell]
            if self.start_cell < 8:
                self.inventory_panel[self.end_cell] = self.whole_inventory[self.start_cell]
                self.whole_inventory[self.start_cell] = temp
            else:
                self.start_cell -= 8
                self.inventory_panel[self.end_cell] = self.inventory_panel[self.start_cell]
                self.inventory_panel[self.start_cell] = temp


inventory = Inventory()
