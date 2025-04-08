from PySide6.QtGui import QIcon
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from display import Display
from buttons import Button
from info import Info
from environment_constants import (
  WINDOW_TITLE,
  WINDOW_ICON_PATH
)
from styles import setupTheme
import sys

def configureWindowsIcon():
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
  setupTheme(app)
  
  window = MainWindow()

  info = Info('teste')
  window.addToVLayout(info)

  display = Display()
  display.setPlaceholderText('Digite um número')
  window.addToVLayout(display)
  
  button = Button('teste')
  window.addToVLayout(button)

  window.setWindowTitle(WINDOW_TITLE)

  icon = QIcon(str(WINDOW_ICON_PATH))
  window.setWindowIcon(icon)
  app.setWindowIcon(icon) 
  
  configureWindowsIcon()

  # mantem a janela fixa
  window.adjustFixedSize()

  window.show()
  app.exec()