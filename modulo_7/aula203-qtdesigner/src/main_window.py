import sys
from typing import cast

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setupUi(self)

    self.btnSend.clicked.connect(self.changeLabel)
    self.edtName.installEventFilter(self)

  def changeLabel(self):
    self.lbTexto.setText(self.edtName.text())

  def eventFilter(self, watched: QObject, event: QEvent) -> bool:
    if event.type() == QEvent.Type.KeyPress:
      event = cast(QKeyEvent, event)
      print(event.text())
      
      # Tenho certeza que o tipo é KeyPress
      event = cast(QKeyEvent, event)
      text = self.edtName.text()
      self.lbTexto.setText(text + event.text())

    return super().eventFilter(watched, event)
    

if __name__ == '__main__':
  app = QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  app.exec()