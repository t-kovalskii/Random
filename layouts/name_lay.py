from PyQt5 import QtWidgets, QtCore, QtGui
from widgets import addListWindow
import random
import pickle

class NameLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """
        self.styleSheet = 'color: white'

        self.choiceFont = QtGui.QFont('Bahnschrift SemiLight SemiConde', 90)
        self.addFont = QtGui.QFont('Bahnschrift SemiLight SemiConde', 15)

        self.addLabel = QtWidgets.QPushButton('New List')
        self.addLabel.setFlat(True)
        self.addLabel.setFont(self.addFont)
        self.addLabel.setStyleSheet(self.styleSheet)
        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.choiceFont)
        self.choiceLabel.setStyleSheet(self.styleSheet)
        self.button = QtWidgets.QPushButton(flat = True)
        self.button.setStyleSheet(self.style)

        self.upLay = QtWidgets.QVBoxLayout()
        self.upLay.addWidget(self.addLabel, alignment = QtCore.Qt.AlignCenter)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(125)
        self.bLay.addWidget(self.button)
        self.bLay.addSpacing(125)

        self.addSpacing(20)
        self.addLayout(self.upLay)
        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter, stretch = 10)
        self.addLayout(self.bLay)
        self.addSpacing(30)

        self.addLabel.clicked.connect(self.show_win)
        self.button.clicked.connect(self.do_random)
        self.button.clicked.connect(self.animate)

    def show_win(self):
        self.addWin = addListWindow.AddWindow()
        self.addWin.show()

    def do_random(self):
        self.file_name = 'list.pic'
        self.f = open(self.file_name, 'rb')
        self.list = pickle.load(self.f)
        self.f.close()
        self.choiceLabel.setText(random.choice(self.list))

    def animate(self):
        self.x = self.button.x()
        self.y = self.button.y()
        self.w = self.button.width()
        self.h = self.button.height()

        self.move_x = self.w / 4
        self.move_y = self.h / 4
        self.new_x = self.x + self.move_x
        self.new_y = self.y + self.move_y
        self.new_w = self.w / 2
        self.new_h = self.h / 2

        self.rect = QtCore.QRect(self.x, self.y, self.w, self.h)
        self.keyRect = QtCore.QRect(self.new_x, self.new_y, self.new_w, self.new_h)

        self.anim = QtCore.QPropertyAnimation(self.button, b'geometry')
        self.anim.setStartValue(self.rect)
        self.anim.setEndValue(self.rect)
        self.anim.setKeyValueAt(0.5, self.keyRect)
        self.anim.setDuration(100)

        self.anim.start()
