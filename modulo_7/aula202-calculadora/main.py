from PySide6.QtGui import QIcon
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from display import Display
from buttons import Button, ButtonsGrid
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


def mainApp():
  app = QApplication(sys.argv)
  setupTheme(app)
  
  # janela principal
  window = MainWindow()

  # Informações
  info = Info('teste')
  window.addWidgetToVLayout(info)

  # Display de expressoes/resultados
  display = Display()
  display.setPlaceholderText('Digite um número')
  window.addWidgetToVLayout(display)

  # grid de botões
  buttonsGrid = ButtonsGrid()
  window.vLayout.addLayout(buttonsGrid)

  #botão
  # buttonsGrid.addWidget(Button('1'), 0, 0)
  # buttonsGrid.addWidget(Button('2'), 0, 1)
  # buttonsGrid.addWidget(Button('3'), 0, 2)
  # buttonsGrid.addWidget(Button('4'), 1, 2)

  window.setWindowTitle(WINDOW_TITLE)
  icon = QIcon(str(WINDOW_ICON_PATH))
  window.setWindowIcon(icon)
  app.setWindowIcon(icon) 
  
  configureWindowsIcon()

  # mantem a janela fixa
  window.adjustFixedSize()

  window.show()
  app.exec()

if __name__ == '__main__':
  mainApp()