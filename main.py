from PyQt6.QtCore import QPointF
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
from PyQt6 import QtPdf, QtPdfWidgets


from os import path
import sys


PDF_PATH = "[PATH]"
# change this value to load a different starting page
PDF_STARTING_PAGE = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("PDF Viewer with QtPdf")
        self.setGeometry(0, 0, 1500, 750)

        self.pdf_view = QtPdfWidgets.QPdfView(self)
        self.pdf_view.setPageMode(QtPdfWidgets.QPdfView.PageMode.MultiPage)
        self.setCentralWidget(self.pdf_view)

        self.pdf_doc = QtPdf.QPdfDocument(self)
        self.pdf_doc.load(PDF_PATH)
        self.pdf_view.setDocument(self.pdf_doc)

        self.pdf_nav = self.pdf_view.pageNavigator()
        self.point = QPointF(0, 0)
        self.pdf_nav.jump(PDF_STARTING_PAGE, self.point)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
