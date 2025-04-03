from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from environment_constants import (
  BIG_FONT_SIZE, 
  TEXT_MARGIN, 
  MINIMUM_WIDTH
)


class Display(QLineEdit):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.alFlag = Qt.AlignmentFlag

    self.configStyle()

  def configStyle(self):
    self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
    self.setMinimumHeight(BIG_FONT_SIZE * 2)
    self.setMinimumWidth(MINIMUM_WIDTH)
    self.setAlignment(self.alFlag.AlignRight)
    self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])