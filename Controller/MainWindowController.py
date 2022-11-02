import time

from PyQt5 import QtWidgets, QtCore
from View.MainWindow import Ui_Solver
import threading

class MainWindowController(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_Solver()
        self.ui.setupUi(self)

        self.labels = [self.ui.index0, self.ui.index1, self.ui.index2, self.ui.index3, self.ui.index4, self.ui.index5,
                       self.ui.index6, self.ui.index7, self.ui.index8]

        self.normal_style_sheet = '''font: 87 72pt "Source Code Pro Black";
                    background-color: rgb(6, 40, 61);
color: rgb(37, 109, 133);
border: 3px solid rgb(223, 246, 255);
border-radius: 20px;'''
        self.upnormal_style_sheet = '''font: 87 72pt "Source Code Pro Black";
background-color: rgb(223, 246, 255);
color: rgb(37, 109, 133);
border: 3px solid rgb(223, 246, 255);
border-radius: 20px; '''
        self.thread = threading.Thread(target=self.changeState)
        self.thread.start()

    def changeState(self, state: int):

        state = str(state)
        if state.find("0") ==-1 :
            state="0"+state   # [0 1 3 4 5 6 7 2 8]
        for label, i in zip(self.labels, range(0, 9, 1)):
            label.setText(state[i] if state[i] != '0' else "")
            label.setStyleSheet(self.normal_style_sheet if state[i] != '0' else self.upnormal_style_sheet)
        # time.sleep(1)
