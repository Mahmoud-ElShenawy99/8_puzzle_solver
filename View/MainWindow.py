# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Solver(object):
    def setupUi(self, Solver):
        Solver.setObjectName("Solver")
        Solver.resize(1205, 804)
        Solver.setStyleSheet("\n"
"background-color: rgb(6, 40, 61);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Solver)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainlabel = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(223, 246, 255);\n"
"color: rgb(37, 109, 133);\n"
"\n"
"border-radius: 15px;")
        self.mainlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainlabel.setObjectName("mainlabel")
        self.verticalLayout.addWidget(self.mainlabel)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.index8 = QtWidgets.QLabel(self.centralwidget)
        self.index8.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index8.setAlignment(QtCore.Qt.AlignCenter)
        self.index8.setObjectName("index8")
        self.gridLayout_2.addWidget(self.index8, 3, 3, 1, 1)
        self.index4 = QtWidgets.QLabel(self.centralwidget)
        self.index4.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index4.setAlignment(QtCore.Qt.AlignCenter)
        self.index4.setObjectName("index4")
        self.gridLayout_2.addWidget(self.index4, 1, 2, 1, 1)
        self.index6 = QtWidgets.QLabel(self.centralwidget)
        self.index6.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index6.setAlignment(QtCore.Qt.AlignCenter)
        self.index6.setObjectName("index6")
        self.gridLayout_2.addWidget(self.index6, 3, 1, 1, 1)
        self.index2 = QtWidgets.QLabel(self.centralwidget)
        self.index2.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index2.setAlignment(QtCore.Qt.AlignCenter)
        self.index2.setObjectName("index2")
        self.gridLayout_2.addWidget(self.index2, 0, 3, 1, 1)
        self.index1 = QtWidgets.QLabel(self.centralwidget)
        self.index1.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index1.setAlignment(QtCore.Qt.AlignCenter)
        self.index1.setObjectName("index1")
        self.gridLayout_2.addWidget(self.index1, 0, 2, 1, 1)
        self.index5 = QtWidgets.QLabel(self.centralwidget)
        self.index5.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index5.setAlignment(QtCore.Qt.AlignCenter)
        self.index5.setObjectName("index5")
        self.gridLayout_2.addWidget(self.index5, 1, 3, 1, 1)
        self.index7 = QtWidgets.QLabel(self.centralwidget)
        self.index7.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index7.setAlignment(QtCore.Qt.AlignCenter)
        self.index7.setObjectName("index7")
        self.gridLayout_2.addWidget(self.index7, 3, 2, 1, 1)
        self.index0 = QtWidgets.QLabel(self.centralwidget)
        self.index0.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(6, 40, 61);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;")
        self.index0.setAlignment(QtCore.Qt.AlignCenter)
        self.index0.setObjectName("index0")
        self.gridLayout_2.addWidget(self.index0, 0, 1, 1, 1)
        self.index3 = QtWidgets.QLabel(self.centralwidget)
        self.index3.setStyleSheet("font: 87 72pt \"Source Code Pro Black\";\n"
"background-color: rgb(223, 246, 255);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"")
        self.index3.setText("")
        self.index3.setAlignment(QtCore.Qt.AlignCenter)
        self.index3.setObjectName("index3")
        self.gridLayout_2.addWidget(self.index3, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DFSButton = QtWidgets.QPushButton(self.centralwidget)
        self.DFSButton.setStyleSheet("QPushButton {font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(255, 169, 20);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(207, 137, 16);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}")
        self.DFSButton.setObjectName("DFSButton")
        self.horizontalLayout_3.addWidget(self.DFSButton)
        self.BFSButton = QtWidgets.QPushButton(self.centralwidget)
        self.BFSButton.setStyleSheet("QPushButton {font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(255, 169, 20);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(207, 137, 16);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}")
        self.BFSButton.setObjectName("BFSButton")
        self.horizontalLayout_3.addWidget(self.BFSButton)
        self.AButton = QtWidgets.QPushButton(self.centralwidget)
        self.AButton.setStyleSheet("QPushButton {font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(255, 169, 20);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{font: 87 26pt \"Source Code Pro Black\";\n"
"background-color: rgb(207, 137, 16);\n"
"color: rgb(37, 109, 133);\n"
"border: 3px solid rgb(223, 246, 255);\n"
"border-radius: 20px;\n"
"}")
        self.AButton.setObjectName("AButton")
        self.horizontalLayout_3.addWidget(self.AButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        Solver.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Solver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 26))
        self.menubar.setObjectName("menubar")
        Solver.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Solver)
        self.statusbar.setObjectName("statusbar")
        Solver.setStatusBar(self.statusbar)

        self.retranslateUi(Solver)
        QtCore.QMetaObject.connectSlotsByName(Solver)

    def retranslateUi(self, Solver):
        _translate = QtCore.QCoreApplication.translate
        Solver.setWindowTitle(_translate("Solver", "8 Puzzle Solver"))
        self.mainlabel.setText(_translate("Solver", "8 Puzzle Solver"))
        self.index8.setText(_translate("Solver", "2"))
        self.index4.setText(_translate("Solver", "5"))
        self.index6.setText(_translate("Solver", "7"))
        self.index2.setText(_translate("Solver", "3"))
        self.index1.setText(_translate("Solver", "1"))
        self.index5.setText(_translate("Solver", "6"))
        self.index7.setText(_translate("Solver", "8"))
        self.index0.setText(_translate("Solver", "4"))
        self.DFSButton.setText(_translate("Solver", "DFS"))
        self.BFSButton.setText(_translate("Solver", "BFS"))
        self.AButton.setText(_translate("Solver", "A*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Solver = QtWidgets.QMainWindow()
    ui = Ui_Solver()
    ui.setupUi(Solver)
    Solver.show()
    sys.exit(app.exec_())