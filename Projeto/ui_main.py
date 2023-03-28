# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import img__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
" border: none\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 0, 9)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.SizeVerCursor))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color:#E6E6FA;\n"
"}\n"
"QToolBox{\n"
"	text-align:left;\n"
"	background-color:#E6E6FA;	\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color:#E6E6FA;\n"
"	text-align:left;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        font = QFont()
        font.setPointSize(11)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"color:black;\n"
"	background-color:#E6E6FA;\n"
"	border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"   border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 16, 465))
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-11, 9, 191, 132))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_atendimento = QPushButton(self.layoutWidget)
        self.btn_atendimento.setObjectName(u"btn_atendimento")
        self.btn_atendimento.setFont(font)
        self.btn_atendimento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atendimento.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_atendimento)

        self.btn_grafico = QPushButton(self.layoutWidget)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setFont(font)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_grafico)

        self.btn_sobre = QPushButton(self.layoutWidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.btn_usuario = QPushButton(self.layoutWidget)
        self.btn_usuario.setObjectName(u"btn_usuario")
        self.btn_usuario.setFont(font)
        self.btn_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usuario.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.btn_usuario)

        self.toolBox.addItem(self.page, u"Op\u00e7\u00f5es")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 65, 465))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: black")

        self.verticalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.top_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.top_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_framer = QFrame(self.main_container)
        self.main_framer.setObjectName(u"main_framer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_framer.sizePolicy().hasHeightForWidth())
        self.main_framer.setSizePolicy(sizePolicy)
        self.main_framer.setFrameShape(QFrame.StyledPanel)
        self.main_framer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.main_framer)
        self.verticalLayout_17.setSpacing(9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 9, 9, 9)
        self.Pages = QStackedWidget(self.main_framer)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 9)
        self.label_5 = QLabel(self.pg_home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 127);")

        self.verticalLayout_6.addWidget(self.label_5)

        self.Pages.addWidget(self.pg_home)
        self.pg_atendim = QWidget()
        self.pg_atendim.setObjectName(u"pg_atendim")
        self.verticalLayout_7 = QVBoxLayout(self.pg_atendim)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_atendim)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_data = QLineEdit(self.frame_4)
        self.txt_data.setObjectName(u"txt_data")
        self.txt_data.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_data.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_data, 1, 0, 1, 2, Qt.AlignVCenter)

        self.txt_pcd = QLineEdit(self.frame_4)
        self.txt_pcd.setObjectName(u"txt_pcd")
        self.txt_pcd.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_pcd.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_pcd, 2, 3, 1, 1)

        self.txt_tipo = QLineEdit(self.frame_4)
        self.txt_tipo.setObjectName(u"txt_tipo")
        self.txt_tipo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_tipo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_tipo, 4, 0, 1, 1)

        self.txt_tarefa = QLineEdit(self.frame_4)
        self.txt_tarefa.setObjectName(u"txt_tarefa")
        self.txt_tarefa.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_tarefa.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_tarefa, 5, 0, 1, 1)

        self.txt_atendente = QLineEdit(self.frame_4)
        self.txt_atendente.setObjectName(u"txt_atendente")
        self.txt_atendente.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_atendente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_atendente, 2, 0, 1, 1)

        self.txt_amb = QLineEdit(self.frame_4)
        self.txt_amb.setObjectName(u"txt_amb")
        self.txt_amb.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_amb.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_amb, 3, 0, 1, 2)

        self.txt_cpf = QLineEdit(self.frame_4)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_cpf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cpf, 2, 2, 1, 1)

        self.txt_doc = QLineEdit(self.frame_4)
        self.txt_doc.setObjectName(u"txt_doc")
        self.txt_doc.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_doc.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_doc, 3, 2, 1, 2)

        self.txt_cbo = QLineEdit(self.frame_4)
        self.txt_cbo.setObjectName(u"txt_cbo")
        self.txt_cbo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_cbo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cbo, 4, 2, 1, 2)

        self.txt_resultado = QLineEdit(self.frame_4)
        self.txt_resultado.setObjectName(u"txt_resultado")
        self.txt_resultado.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_resultado.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_resultado, 5, 2, 1, 1)

        self.txt_motivo = QLineEdit(self.frame_4)
        self.txt_motivo.setObjectName(u"txt_motivo")
        self.txt_motivo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_motivo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_motivo, 5, 3, 1, 1)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 2, 1, 2, Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    background-color: red;\n"
"    color: white;\n"
"	border-radius: 20px;\n"
"	font-size:15px;\n"
"border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: green;\n"
"    color: white;\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableView {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #E6E6FA;\n"
"}")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.btn_procurar = QPushButton(self.frame_3)
        self.btn_procurar.setObjectName(u"btn_procurar")
        self.btn_procurar.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_procurar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_atendim)
        self.pg_usuario = QWidget()
        self.pg_usuario.setObjectName(u"pg_usuario")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_usuario)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tabWidget_2 = QTabWidget(self.pg_usuario)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_6 = QFrame(self.tab_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 30, 461, 361))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 40, 542, 361))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_15.addWidget(self.label_8)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_nome_2 = QLineEdit(self.layoutWidget1)
        self.txt_nome_2.setObjectName(u"txt_nome_2")
        self.txt_nome_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_nome_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nome_2, 0, 0, 1, 1)

        self.cb_perfil = QComboBox(self.layoutWidget1)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setStyleSheet(u"\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"")

        self.gridLayout_2.addWidget(self.cb_perfil, 2, 0, 1, 1)

        self.txt_senha1 = QLineEdit(self.layoutWidget1)
        self.txt_senha1.setObjectName(u"txt_senha1")
        self.txt_senha1.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_senha1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_senha1, 1, 1, 1, 1)

        self.txt_usuario = QLineEdit(self.layoutWidget1)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_usuario.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_usuario, 0, 1, 1, 1)

        self.txt_senha = QLineEdit(self.layoutWidget1)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_senha, 1, 0, 1, 1)

        self.txt_data_2 = QLineEdit(self.layoutWidget1)
        self.txt_data_2.setObjectName(u"txt_data_2")
        self.txt_data_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E6E6FA; /*cor lil\u00e1s claro*/\n"
"    border-top-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    font-size: 10pt; /*tamanho da fonte*/\n"
"}")
        self.txt_data_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_data_2, 2, 1, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_2)

        self.btn_cadastrar = QPushButton(self.layoutWidget1)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: red;\n"
"    color: white;\n"
"	border-radius: 20px;\n"
"	font-size:15px;\n"
"border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: green;\n"
"    color: white;\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.btn_cadastrar)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_13 = QVBoxLayout(self.tab_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_5 = QFrame(self.tab_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_2 = QTableWidget(self.frame_5)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableView {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #E6E6FA;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #DBB1EA;\n"
"    min-width: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
""
                        "    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #DBB1EA;\n"
"    min-width: 30px;\n"
"    border-radius: 7px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.tableWidget_2)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_procurar_2 = QPushButton(self.frame_5)
        self.btn_procurar_2.setObjectName(u"btn_procurar_2")
        self.btn_procurar_2.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_procurar_2)

        self.btn_editar = QPushButton(self.frame_5)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_editar)

        self.btn_adicionar = QPushButton(self.frame_5)
        self.btn_adicionar.setObjectName(u"btn_adicionar")
        self.btn_adicionar.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_adicionar)

        self.btn_excluir_2 = QPushButton(self.frame_5)
        self.btn_excluir_2.setObjectName(u"btn_excluir_2")
        self.btn_excluir_2.setStyleSheet(u" \n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #E6E6FA;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: green;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_excluir_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.horizontalLayout_7.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_usuario)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.Pages.addWidget(self.pg_sobre)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_16 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.pg_contato)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_16.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_contato)

        self.verticalLayout_17.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_framer)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_atendimento.setText(QCoreApplication.translate("MainWindow", u"Atendimento", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_usuario.setText(QCoreApplication.translate("MainWindow", u"Novo Usu\u00e1rio", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Sistema de Controle de Agendamento</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/img/img/cateq2023.png\"/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Cadastro</span></p></body></html>", None))
        self.txt_data.setText("")
        self.txt_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.txt_pcd.setText("")
        self.txt_pcd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PCD", None))
        self.txt_tipo.setText("")
        self.txt_tipo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo de Atendimento", None))
        self.txt_tarefa.setText("")
        self.txt_tarefa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tarefa Realizada", None))
        self.txt_atendente.setText("")
        self.txt_atendente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Atendente", None))
        self.txt_amb.setText("")
        self.txt_amb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ambiente de Atendimento", None))
        self.txt_cpf.setText("")
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PIS/PASEP/CPF/CNPJ", None))
        self.txt_doc.setText("")
        self.txt_doc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba Documento", None))
        self.txt_cbo.setText("")
        self.txt_cbo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CBO", None))
        self.txt_resultado.setText("")
        self.txt_resultado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.txt_motivo.setText("")
        self.txt_motivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Motivo se n\u00e3o encaminhado", None))
        self.txt_nome.setText("")
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Novo Atendimento", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline; color:#000000;\">Atendimentos realizados</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Atendente", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PIS/PASEP/CPF/CNPJ", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N\u00ba Documento", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PCD", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ambiente de Atendimento", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tipo de Atendimento", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Tarefa realizada", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Principal Pretens\u00e3o Profissional (CBO)", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Motivo se n\u00e3o encaminhado", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_procurar.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Controle de Atendimentos", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.txt_nome_2.setText("")
        self.txt_nome_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Atendente", None))

        self.txt_senha1.setText("")
        self.txt_senha1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmar senha", None))
        self.txt_usuario.setText("")
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.txt_senha.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_data_2.setText("")
        self.txt_data_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Senha", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Confirmar senha", None));
        self.btn_procurar_2.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_excluir_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Projeto elaborado para o Projeto Ninho de Desenvolvedores no CATEQ</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Desenvolvedores: Juliana e Ge\u00e2ngela</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sistema de Controle de Agendamento</p></body></html>", None))
    # retranslateUi

