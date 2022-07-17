# Traffic Light Simulation
from PyQt5 import QtWidgets
from GUI.Interface import Interface
from GUI.gui_mainwindow import Ui_MainWindow


def main():
    interface = Interface()
    interface.start()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
