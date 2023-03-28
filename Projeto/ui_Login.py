# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(395, 388)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 230, 204, 93))
        self.frame.setStyleSheet(u"background-color: rgba(85, 0, 127,0.2)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtUser = QLineEdit(self.frame)
        self.txtUser.setObjectName(u"txtUser")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtUser.setFont(font)
        self.txtUser.setStyleSheet(u"color: white")
        self.txtUser.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txtUser)

        self.txtSenha = QLineEdit(self.frame)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setFont(font)
        self.txtSenha.setStyleSheet(u"color:white")
        self.txtSenha.setEchoMode(QLineEdit.Password)
        self.txtSenha.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txtSenha)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 130, 101, 91))
        self.label.setStyleSheet(u"background-color:  #E6E6FA;\n"
" border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"")
        self.label.setPixmap(QPixmap(u"loginIcon.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 381, 111))
        self.label_2.setStyleSheet(u"\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    ")
        self.label_2.setPixmap(QPixmap(u"../imagens/cateq2023.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txtUser.setPlaceholderText(QCoreApplication.translate("Form", u"Usu\u00e1rio", None))
        self.txtSenha.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

