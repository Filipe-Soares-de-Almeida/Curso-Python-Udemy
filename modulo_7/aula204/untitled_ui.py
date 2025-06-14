# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(640, 480)
        font = QFont()
        font.setPointSize(40)
        myWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(myWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnB1 = QPushButton(myWidget)
        self.btnB1.setObjectName(u"btnB1")

        self.gridLayout.addWidget(self.btnB1, 1, 0, 1, 1)

        self.btnB2 = QPushButton(myWidget)
        self.btnB2.setObjectName(u"btnB2")

        self.gridLayout.addWidget(self.btnB2, 1, 1, 1, 1)

        self.lbL2 = QLabel(myWidget)
        self.lbL2.setObjectName(u"lbL2")

        self.gridLayout.addWidget(self.lbL2, 0, 1, 1, 1)

        self.lbL1 = QLabel(myWidget)
        self.lbL1.setObjectName(u"lbL1")

        self.gridLayout.addWidget(self.lbL1, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"Form", None))
        self.btnB1.setText(QCoreApplication.translate("myWidget", u"B1", None))
        self.btnB2.setText(QCoreApplication.translate("myWidget", u"B2", None))
        self.lbL2.setText(QCoreApplication.translate("myWidget", u"L2", None))
        self.lbL1.setText(QCoreApplication.translate("myWidget", u"L1", None))
    # retranslateUi

