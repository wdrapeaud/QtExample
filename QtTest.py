from PyQt5 import QtWidgets,uic
import main

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.closeBtn.clicked.connect(self.close)

app = QtWidgets.QApplication([])
window = MyMainWindow()
window.show()
app.exec_()
