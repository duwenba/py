import sys
from time import sleep

import ui_untitled
from PyQt6.QtWidgets import QApplication, QFrame
# from PyQt6 import QtCore,QtGui
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)
fram =QFrame()
fram.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)#WA_TranslucentBackground)  # 窗体背景透明
fram.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)  #窗口置顶，无边框，在任务栏不显示图标
# fram.setWindowFlags(Qt.WindowType.FramelessWindowHint)#(PyQtWindowMinMaxButtonsHint | Qt::FramelessWindowHint)
ui = ui_untitled.Ui_Frame()
ui.setupUi(fram)
fram.show()
sys.exit(app.exec())