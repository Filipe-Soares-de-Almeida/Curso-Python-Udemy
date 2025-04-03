from PySide6.QtGui import QIcon
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from environment_constants import (
  WINDOW_TITLE,
  WINDOW_ICON_PATH
)
import sys

def configureWindowsIcon(icon: QIcon):
  if not sys.platform.startswith('win'):
    return
  
  import ctypes
  
  version_info_path = \
    'CompanyName.ProductName.SubProduct.VersionInformation'

  ctypes \
    .windll \
    .shell32 \
    .SetCurrentProcessExplicitAppUserModelID(version_info_path)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.setWindowTitle(WINDOW_TITLE)
  icon = QIcon(str(WINDOW_ICON_PATH))

  window.setWindowIcon(icon)
  app.setWindowIcon(icon) 
  configureWindowsIcon(icon)
  
  # mantem a janela fixa
  window.adjustFixedSize()

  window.show()
  app.exec()