# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(749, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(522422, 1603))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")

        self.verticalLayout_11.addLayout(self.horizontalLayout_25)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.RightToLeft)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_contato = QPushButton(self.centralwidget)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_tables = QPushButton(self.centralwidget)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.centralwidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_outro = QPushButton(self.centralwidget)
        self.btn_outro.setObjectName(u"btn_outro")
        self.btn_outro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_outro.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout.addWidget(self.btn_outro)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setEnabled(True)
        self.Pages.setMinimumSize(QSize(729, 0))
        self.Pages.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_14 = QLabel(self.pg_home)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"\n"
"background-color: rgb(170, 170, 255);")

        self.verticalLayout_7.addWidget(self.label_14)

        self.pushButton_3 = QPushButton(self.pg_home)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-colorrgb(0, 85, 127);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.Pages.addWidget(self.pg_home)
        self.pg_tables = QWidget()
        self.pg_tables.setObjectName(u"pg_tables")
        self.verticalLayout_2 = QVBoxLayout(self.pg_tables)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Base = QTabWidget(self.pg_tables)
        self.Base.setObjectName(u"Base")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_6 = QVBoxLayout(self.tables)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tables)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout_3.addWidget(self.btn_open)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_Estoque = QVBoxLayout()
        self.tb_Estoque.setObjectName(u"tb_Estoque")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.tb_Estoque.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setFrameShape(QFrame.NoFrame)

        self.tb_Estoque.addWidget(self.tw_estoque)

        self.pushButton = QPushButton(self.tables)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.tb_Estoque.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.tb_Estoque)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_importar = QPushButton(self.tables)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:10px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.btn_gerar = QPushButton(self.tables)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:10px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.pushButton_8 = QPushButton(self.tables)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:10px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.Base.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.Base.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.Base)

        self.Pages.addWidget(self.pg_tables)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_13 = QLabel(self.page)
        self.label_13.setObjectName(u"label_13")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_13)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.txt_nome = QLineEdit(self.page)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txt_usuario = QLineEdit(self.page)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_senha = QLineEdit(self.page)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_novasenha = QLineEdit(self.page)
        self.txt_novasenha.setObjectName(u"txt_novasenha")
        self.txt_novasenha.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_novasenha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_novasenha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.cb_perfil = QComboBox(self.page)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy2)
        self.cb_perfil.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 2px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")

        self.horizontalLayout_10.addWidget(self.pushButton_2)

        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 711, 461))
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.verticalLayout_9.addWidget(self.label)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_11.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_11.addWidget(self.lineEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_12.addWidget(self.lineEdit_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.comboBox_8 = QComboBox(self.widget)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.horizontalLayout_13.addWidget(self.comboBox_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_14.addWidget(self.label_17)

        self.comboBox_6 = QComboBox(self.widget)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_14.addWidget(self.comboBox_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_15.addWidget(self.label_25)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_15.addWidget(self.lineEdit_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_16.addWidget(self.label_18)

        self.comboBox_7 = QComboBox(self.widget)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_16.addWidget(self.comboBox_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_24.addLayout(self.verticalLayout_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_19.addWidget(self.label_19)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_19.addWidget(self.lineEdit_6)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_17.addWidget(self.label_21)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_17.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_22.addWidget(self.label_24)

        self.comboBox_5 = QComboBox(self.widget)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_22.addWidget(self.comboBox_5)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_21.addWidget(self.label_23)

        self.comboBox_4 = QComboBox(self.widget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_21.addWidget(self.comboBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_18.addWidget(self.label_20)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_18.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_20.addWidget(self.label_22)

        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_20.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_24.addLayout(self.verticalLayout)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SetFixedSize)
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)

        self.horizontalLayout_23.addWidget(self.label_26)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")
        self.pushButton_4.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.pushButton_4)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)

        self.horizontalLayout_23.addWidget(self.label_27)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.Pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_28 = QLabel(self.page_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(160, 30, 401, 91))
        self.label_28.setStyleSheet(u"font-color:rgb(255, 255, 255)")
        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(60, 190, 351, 20))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.page_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(440, 190, 191, 21))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 12px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")
        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(240, 300, 261, 31))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 1px;\n"
"font-size:14px;\n"
"background-color: rgb(170, 170, 255);}\n"
"QPushButton:hover{background-color:#fff;color:black}")
        self.Pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_29 = QLabel(self.page_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 711, 431))
        self.Pages.addWidget(self.page_4)

        self.verticalLayout_10.addWidget(self.Pages)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(5)
        self.Base.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Planilha", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", u"Novo atendimento", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Sistema de Controle de Atendimento </span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#55007f;\">CATEQ</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Novo Usu\u00e1rio", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Gest\u00e3o dos atendimentos</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"PCD", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Motivo se n\u00e3o encaminhado", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Tarefa", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"CBO", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Atendente", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Ambiente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"N\u00ba Documento", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"PIS/PASEP/CPF/CNPJ", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Data", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Novo Atendimento", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.Base.setTabText(self.Base.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Sistema de Controle de Atendimento </span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#55007f;\">CATEQ</span></p></body></html>", None))
        self.Base.setTabText(self.Base.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Tela para cadastro </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"1\"/></p><p><span style=\" color:#000000;\">Cadastro de Atendente</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nova Senha", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Perfil do usuario", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Atendente", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_11.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_12.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">Atendimento</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PCD", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Sim", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"N\u00e3o", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Pis/Pasep/CPF/CNPJ", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"PIS/PASEP", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"CPF", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"CNPJ", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"N\u00ba Doc.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ambiente", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"SINE", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"NO MEU BAIRRO", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"EMPREENDEDORES", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"QUALIFICA\u00c7\u00c3O", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("MainWindow", u"CEARA CREDI", None))
        self.comboBox_7.setItemText(6, "")

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Atendente", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CBO", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Para adicionar", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Encaminhado", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"N\u00e3o Encaminhado", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Baixa em encaminhamento", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Orientado", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Habilitado", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Acerto Feito", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"Encaminhado MTE", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"Pr\u00e9-Sele\u00e7\u00e3o", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"Emitido", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"Realizado", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"Emitida/Impressa", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("MainWindow", u"Formalizado", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("MainWindow", u"Enc. para Audit\u00f3rio", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("MainWindow", u"Enc. para Empreendedorismo", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("MainWindow", u"Enc. Prosperar", None))
        self.comboBox_5.setItemText(15, "")

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Motivo se n\u00e3o encaminhado", None))
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Escolaridade", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Sem experi\u00eancia na fun\u00e7\u00e3o", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Recusa do trabalhador", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Mora distante da empresa", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"PCD", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"Sem vaga no perfil", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"IMO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"SD FORM.", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"SD JUST.", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Convoca\u00e7\u00e3o", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"MEI", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Jovem Aprendiz", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Ceara Credi", None))
        self.comboBox.setItemText(8, "")

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Tarefa", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"IMO - ALTERA\u00c7\u00c3O DE CADASTRO", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"IMO - CONSULTA DE VAGAS", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"IMO - PR\u00c9-SELE\u00c7\u00c3O", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"CONSULTA - SD", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"HABILITA\u00c7\u00c3O - SD", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"ACERTOS -SD", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"ORIENTA\u00c7\u00c3O - SD", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"ALT.CADASTRAL - MEI", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"BOLETOS - MEI", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"DECLARA\u00c7\u00c3O - MEI ", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"FORMALIZA\u00c7\u00c3O - MEI", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"BAIXA - MEI", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"PARCELAMENTO - MEI", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("MainWindow", u"QUALIFICA\u00c7\u00c3O", None))
        self.comboBox_3.setItemText(14, QCoreApplication.translate("MainWindow", u"CONSULTORIA", None))
        self.comboBox_3.setItemText(15, QCoreApplication.translate("MainWindow", u"OFICINAS", None))
        self.comboBox_3.setItemText(16, QCoreApplication.translate("MainWindow", u"EVENTOS", None))
        self.comboBox_3.setItemText(17, QCoreApplication.translate("MainWindow", u"CONVOCA\u00c7\u00c3O", None))
        self.comboBox_3.setItemText(18, "")

        self.label_26.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Criar atendimento", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#000000;\">Importar XML</span></p></body></html>", None))
        self.lineEdit_4.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">Sistema desenvolvido para controle </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">de atendimento no CATEQ</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">Desenvolvedoras: Ge\u00e2ngela e Juliana</span></p></body></html>", None))
    # retranslateUi

