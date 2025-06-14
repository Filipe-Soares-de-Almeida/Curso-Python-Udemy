import sys
import time

from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QWidget
from untitled_ui import Ui_myWidget


class Worker1(QObject):
  started = Signal(str)
  progressed = Signal(str)
  finished = Signal(str)
  
  def doWork(self):
    value = '0'
    self.started.emit(value)

    for i in range(5):
      value = str(i)
      self.progressed.emit(value)
      time.sleep(1)

    self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
  def __init__(self, parent=None):
    super().__init__(parent=parent)
    self.setupUi(self)

    self.btnB1.clicked.connect(self.hardWork1)
    self.btnB2.clicked.connect(self.hardWork2)

  
  def hardWork1(self):
    # ao passar o worker e a thread para o atributo da classe
    # é evitado que o worker e o thread sejam removidos da memória
    # ao final da função
    self._worker = Worker1()
    self._thread = QThread()
    worker = self._worker
    thread = self._thread

    # Move o worker para o thread
    worker.moveToThread(thread)

    # thread inicia o worker
    # ao finalizar o worker, o thread também finaliza
    thread.started.connect(worker.doWork)
    worker.finished.connect(thread.quit)

    # remove o worker e o thread da memória
    thread.finished.connect(thread.deleteLater)
    worker.finished.connect(worker.deleteLater)

    worker.started.connect(self.hardWork1onStarted)
    worker.progressed.connect(self.hardWork1onProgressed)
    worker.finished.connect(self.hardWork1onFinished)

    thread.start()

  def hardWork1onStarted(self, value):
    self.lbL1.setText(value)
    self.btnB1.setDisabled(True)
    print('hardWork1 - Iniciando...')

  def hardWork1onProgressed(self, value):
    self.lbL1.setText(value)
    print('hardWork1 - ' + value)

  def hardWork1onFinished(self, value):
    self.lbL1.setText(value)
    self.btnB1.setDisabled(False)
    print('hardWork1 - Finalizado!')

  def hardWork2(self):
    # ao passar o worker e a thread para o atributo da classe
    # é evitado que o worker e o thread sejam removidos da memória
    # ao final da função
    self._worker2 = Worker1()
    self._thread2 = QThread()
    worker = self._worker2
    thread = self._thread2

    # Move o worker para o thread
    worker.moveToThread(thread)

    # thread inicia o worker
    # ao finalizar o worker, o thread também finaliza
    thread.started.connect(worker.doWork)
    worker.finished.connect(thread.quit)

    # remove o worker e o thread da memória
    thread.finished.connect(thread.deleteLater)
    worker.finished.connect(worker.deleteLater)

    worker.started.connect(self.hardWork2onStarted)
    worker.progressed.connect(self.hardWork2onProgressed)
    worker.finished.connect(self.hardWork2onFinished)

    thread.start()

  def hardWork2onStarted(self, value):
    self.lbL2.setText(value)
    self.btnB2.setDisabled(True)
    print('hardWork2 - Iniciando...')

  def hardWork2onProgressed(self, value):
    self.lbL2.setText(value)
    print('hardWork2- ' + value)

  def hardWork2onFinished(self, value):
    self.lbL2.setText(value)
    self.btnB2.setDisabled(False)
    print('hardWork2 - Finalizado!')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  myWidget = MyWidget()
  myWidget.show()
  app.exec()
