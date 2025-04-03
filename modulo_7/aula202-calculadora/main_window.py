from PySide6.QtWidgets import (
  QMainWindow,
  QVBoxLayout,
  QWidget,
  QLabel
)

class MainWindow(QMainWindow):
  def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
    super().__init__(parent, *args, **kwargs)

    self.c_widget = QWidget()
    self.v_layout = QVBoxLayout()
    self.c_widget.setLayout(self.v_layout)

    self.label_teste = QLabel('Label teste Calculadora')
    self.label_teste.setStyleSheet('font-size: 40px;')
    self.v_layout.addWidget(self.label_teste)

    self.setCentralWidget(self.c_widget)

  def adjustFixedSize(self):
    self.adjustSize()
    self.setFixedSize(self.width(), self.height())