# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton


app = QApplication(sys.argv)

button1 = QPushButton('Primeiro Botão')
button1.setStyleSheet('font-size: 30px; color: rgb(255, 0, 0);')
button1.show()

# button2 = QPushButton('Segundo Botão')
# button2.show()

app.exec()