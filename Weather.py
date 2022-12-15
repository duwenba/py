from PyQt6 import QtWidgets
# import PyQt6.
import sys
app = QtWidgets.QApplication(sys.argv)

lab = QtWidgets.QLabel()

lab.setText('你好!!')
lab.show()

sys.exit(app.exec())

