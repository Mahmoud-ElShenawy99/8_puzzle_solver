import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer

from Model.UninformedSearchAgents import UninformedSearch
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
        self.search = UninformedSearch()
        self.timer = QTimer()
        self.timer.timeout.connect(self.changeState)
        self.path_to_goal=None
        self.current=0
        self.ui.BFSButton.clicked.connect(self.BFS)
        self.ui.DFSButton.clicked.connect(self.DFS)


    def BFS(self):
        self.current=0
        self.initial=int(self.ui.initialLineEdit.text()) if self.ui.initialLineEdit.text().isnumeric() else 12345678
        self.goal=int(self.ui.finalLineEdit.text()) if self.ui.finalLineEdit.text().isnumeric() else 12345678

        solved, path_to_goal, cost, explored, time = self.search.BFS(self.initial,self.goal)
        # print("Time= " + str(time))
        # print("Path= " + str(path_to_goal))
        # print("Cost= " + str(cost))
        # print("Explored= " + str(explored))
        # print("Explored Number= " + str(len(explored)))
        # print("Depth= " + str(cost))
        self.path_to_goal=path_to_goal
        self.path_to_goal.reverse()
        self.timer.start(1500)

    def DFS(self):
        self.current=0
        self.initial = int(self.ui.initialLineEdit.text()) if self.ui.initialLineEdit.text().isnumeric() else 12345678
        self.goal = int(self.ui.finalLineEdit.text()) if self.ui.finalLineEdit.text().isnumeric() else 12345678
        solved, path_to_goal, cost, explored, time = self.search.DFS(self.initial,self.goal)
        # print("Time= " + str(time))
        # print("Path= " + str(path_to_goal))
        # print("Cost= " + str(cost))
        # print("Explored= " + str(explored))
        # print("Explored Number= " + str(len(explored)))
        # print("Depth= " + str(cost))
        self.path_to_goal=path_to_goal
        self.path_to_goal.reverse()
        self.timer.start(1500)

    def changeState(self):
        if self.current == len(self.path_to_goal):
            self.timer.stop()
            return
        state = self.path_to_goal[self.current]
        state = str(state)
        if state.find("0") == -1:
            state = "0" + state
        for label, i in zip(self.labels, range(0, 9, 1)):
            label.setText(state[i] if state[i] != '0' else "")
            label.setStyleSheet(self.normal_style_sheet if state[i] != '0' else self.upnormal_style_sheet)
        self.current+=1
