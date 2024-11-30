import sys
import random

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.resize(500, 500)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_yellow_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_yellow_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        size = random.randrange(10, 300)
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)
        qp.drawEllipse(x, y, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
