import sys
import pygame
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('Ships.db')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('Ships')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(870, 600)
        # button

        self.setGeometry(50, 50, 900, 900)
        self.setWindowTitle('Info')

        but = QPushButton(self)
        but.setIcon(QIcon('Buran.png'))
        but.setGeometry(50, 650, 165, 105)
        but.setIconSize(QSize(150, 150))
        self.show()


        #Work
        but.clicked.connect(self.Buran)

    def Buran(L,I):
        # import the pygame module
        from PIL import Image  # read the image
        im = Image.open("Burancheme.png")
        print(im.size)
        wpercent = (1000 / float(im.size[0]))
        hsize = int((float(im.size[1]) * float(wpercent)))
        im = im.resize((1000, hsize), Image.Resampling.LANCZOS)
        im.save('Burancheme.png')
        im = Image.open("Burancheme.png")
        print(im.size)

        screen = pygame.display.set_mode(im.size)

        bg = pygame.image.load("Burancheme.png")

        pygame.mouse.set_visible(0)

        ship = pygame.image.load("Burancheme.png")
        ship_top = screen.get_height() - ship.get_height()
        ship_left = screen.get_width() / 2 - ship.get_width() / 2

        screen.blit(ship, (ship_left, ship_top))


        # Define the background colour
        # using RGB color coding.

        # Define the dimensions of
        # screen object(width,height)

        # Set the caption of the screen
        pygame.display.set_caption('Buran')

        # Fill the background colour to the screen

        # Update the display using flip
        pygame.display.flip()

        # Variable to keep our game loop running
        running = True

        # game loop
        while running:

            # for loop through the event queue
            for event in pygame.event.get():

                # Check for QUIT event
                if event.type == pygame.QUIT:
                    running = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
