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



        #Work


from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Galaxy_War.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.Buran)
        # Обратите внимание: имя элемента такое же как в QTDesigner

        pixmap = QPixmap('Buran.png')
        self.label.setPixmap(pixmap)

        # Optional, resize window to image size
        self.resize(pixmap.width(), pixmap.height())



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
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

