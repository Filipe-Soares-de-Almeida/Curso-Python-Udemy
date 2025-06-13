import math
from operator import eq
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QPushButton, QGridLayout, QMessageBox
from PySide6.QtCore import Slot
from shiboken6 import isValid
from environment_constants import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValidNumber, convertToNumber

if TYPE_CHECKING:
  from display import Display
  from info import Info
  from main_window import MainWindow

class Button(QPushButton):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configStyle()


  def configStyle(self):
    font = self.font()
    font.setPixelSize(MEDIUM_FONT_SIZE)  
    self.setFont(font)
    self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
  def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._gridMask = [
      ['C', '◀', '^', '/'],
      ['7', '8', '9', '*'],
      ['4', '5', '6', '-'],
      ['1', '2', '3', '+'],
      ['N',  '0', '.', '=']
    ]

    self.display = display
    self.info = info
    self.window = window

    self._equation = ''
    self._equationInitialValue = 'Sua Conta'
    self._left = None
    self._right = None
    self._op = None
    self.equation = self._equationInitialValue
    self._makeGrid()

  @property
  def equation(self):
    return self._equation

  @equation.setter
  def equation(self, value):
    self._equation = value
    self.info.setText(value) 

  def signal_connect(self, text):
    print(text)

  def _makeGrid(self): 
    self.display.eqPressed.connect(self._eq)
    self.display.clearPressed.connect(self._clear)
    self.display.delPressed.connect(self._backspace)
    self.display.inputPressed.connect(self._insertTextToDisplay)
    self.display.operatorPressed.connect(self._configOperator)

    
    for i, row in enumerate(self._gridMask):
      for j, button_text in enumerate(row):
        button = Button(button_text)

        if not isNumOrDot(button_text) and not isEmpty(button_text):
          button.setProperty("cssClass", "specialButton")
          self._configSpecialButton(button)

        self.addWidget(button, i, j)

        slot = self._makeSlot(self._insertTextToDisplay, button.text())
        self._connectButtonClicked(button, slot)

  def _connectButtonClicked(self, button: 'Button', slot: 'object'):
    button.clicked.connect(slot)

  def _configSpecialButton(self, button: 'Button'):
    text = button.text()

    if text == 'C':
      self._connectButtonClicked(button, self._clear)

    if text in '+-/*^':
      self._connectButtonClicked(
        button, 
        self._makeSlot(self._configOperator, button.text())
      )

    if text == '=':
      self._connectButtonClicked(button, self._eq)

    if text == '◀':
      self._connectButtonClicked(button, self._backspace)

    if text == 'N':
      self._connectButtonClicked(button, self._invertNumber)

  @Slot()
  def _backspace(self):
    self.display.backspace()
    self.display.setFocus()

  @Slot()
  def _invertNumber(self):
    displayText = self.display.text()
    
    if not isValidNumber(displayText):
      return
    
    number = - convertToNumber(displayText)

    self.display.setText(str(number))

  @Slot()
  def _makeSlot(self, func, *args, **kwargs):
    @Slot(bool)
    def realSlot(_):
      func(*args, **kwargs)
    return realSlot

  @Slot()
  def _insertTextToDisplay(self, text):    
    newDisplayValue = self.display.text() + text

    if not isValidNumber(newDisplayValue):
      return
    
    self.display.insert(text)
    self.display.setFocus()

  @Slot()
  def _clear(self):
    self._left = None
    self._right = None
    self._op = None
    self.equation = self._equationInitialValue

    self.display.clear()
    self.display.setFocus()

  @Slot()
  def _configOperator(self, text):
    displayText = self.display.text()
    
    self.display.clear()

    if not isValidNumber(displayText) and self._left is None:
      self._showError('Você não digitou nada')
      return
    
    if self._left is None:
      self._left = convertToNumber(displayText)


    self._op = text
    self.equation = f'{self._left} {self._op} ??'
    
    self.display.setFocus()
  
  @Slot()
  def _eq(self):
    displayText = self.display.text()

    if not isValidNumber(displayText) or self._left is None:
      self._showError('Conta incompleta!')
      return

    self._right = convertToNumber(displayText)
    self.equation = f'{self._left} { self._op} {self._right}'

    result = 'error'
    try:
      if '^' in self.equation and isinstance(self._left, float | int):
        result = math.pow(self._left, self._right)
      else: 
        result = eval(self.equation)
    except ZeroDivisionError:
      self._showError('Divisão por zero.')
    except OverflowError:
      self._showError('Essa conta não pode ser realizada.')

    self.display.clear()
    self.info.setText(f'{self.equation} = {convertToNumber(str(result))}')
    self._left = result
    self._right = None

    self.display.setFocus()

    if self._left == 'error':
      self._left = None

  def _makeDialog(self, text, icon):
    msgBox = self.window.makeMsgBox()
    msgBox.setText(text)
    msgBox.setIcon(icon)

    return msgBox

  def _showError(self, text):
    msgBox = self._makeDialog(text, QMessageBox.Icon.Critical)
    msgBox.exec()
    self.display.setFocus()

  def _showInfo(self, text):
    msgBox = self._makeDialog(text, QMessageBox.Icon.Information)
    msgBox.exec()
    self.display.setFocus()

