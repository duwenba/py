from PyQt6 import QtWidgets
import sys
# import win32con
# win32con.SW_SHOW
app = QtWidgets.QApplication(sys.argv)
lab = QtWidgets.QLabel('hello world')
print(lab.windowType())
lab.show()
sys.exit(app.exec())
