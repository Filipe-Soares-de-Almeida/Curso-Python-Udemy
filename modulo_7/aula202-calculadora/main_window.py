from PySide6.QtWidgets import (
  QMainWindow,
  QVBoxLayout,
  QWidget,
  QMessageBox,
)


class MainWindow(QMainWindow):
  def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
    super().__init__(parent, *args, **kwargs)

    self.cWidget = QWidget()
    self.vLayout = QVBoxLayout()
    self.cWidget.setLayout(self.vLayout)

    # wiget principal
    self.setCentralWidget(self.cWidget)

  def adjustFixedSize(self):
    self.adjustSize()
    self.setFixedSize(self.width(), self.height())

  def addWidgetToVLayout(self, widget):
    self.vLayout.addWidget(widget)


  def makeMsgBox(self):
    return QMessageBox(self)