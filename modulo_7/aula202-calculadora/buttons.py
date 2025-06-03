from PySide6.QtWidgets import QPushButton, QGridLayout
from environment_constants import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot

class Button(QPushButton):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configStyle();

  def configStyle(self):
    font = self.font()
    font.setPixelSize(MEDIUM_FONT_SIZE)  
    self.setFont(font)
    self.setMinimumSize(75, 75)
    # self.setProperty("cssClass", "specialButton")

class ButtonsGrid(QGridLayout):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._grid_mask = [
      ['C', '◀', '^', '/'],
      ['7', '8', '9', '*'],
      ['4', '5', '6', '-'],
      ['1', '2', '3', '+'],
      ['',  '0', '.', '=']
    ]

    self._makeGrid()

  def _makeGrid(self):
    for i, row in enumerate(self._grid_mask):
      for j, button_text in enumerate(row):
        button = Button(button_text)

        if not isNumOrDot(button_text) and not isEmpty(button_text):
          button.setProperty("cssClass", "specialButton")
          button.setEnabled(False)

        button.clicked.connect()
        self.addWidget(button, i, j)
