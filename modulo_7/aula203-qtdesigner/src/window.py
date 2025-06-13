# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 654)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbTexto = QLabel(self.centralwidget)
        self.lbTexto.setObjectName(u"lbTexto")
        font = QFont()
        font.setPointSize(50)
        self.lbTexto.setFont(font)
        self.lbTexto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbTexto, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbName = QLabel(self.centralwidget)
        self.lbName.setObjectName(u"lbName")
        font1 = QFont()
        font1.setPointSize(30)
        self.lbName.setFont(font1)

        self.gridLayout_2.addWidget(self.lbName, 0, 0, 1, 1)

        self.edtName = QLineEdit(self.centralwidget)
        self.edtName.setObjectName(u"edtName")

        self.gridLayout_2.addWidget(self.edtName, 0, 1, 1, 1)

        self.btnSend = QPushButton(self.centralwidget)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setFont(font1)

        self.gridLayout_2.addWidget(self.btnSend, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 835, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbTexto.setText(QCoreApplication.translate("MainWindow", u"Texto teste", None))
        self.lbName.setText(QCoreApplication.translate("MainWindow", u"Seu nome:", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

