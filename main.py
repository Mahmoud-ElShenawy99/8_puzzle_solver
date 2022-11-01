from Controller.MainWindowController import MainWindowController
from PyQt5 import QtWidgets
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindowController()
    ui.show()





    print("{DFS Done}")

    sys.exit(app.exec_())