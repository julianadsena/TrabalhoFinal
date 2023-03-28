from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QMainWindow,QMessageBox)
from ui_main import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6 import QtCore
from database import Data_base


import sys
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gestão de Atendimento")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        ######Botão menu###
        self.pushButton_2.clicked.connect(self.leftMenu)
        #####paginas####
        self.pushButton.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_atendimento.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_atendim))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_usuario))
        self.btn_grafico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        #####
        self.pushButton_7.clicked.connect(self.cadastrar_atendimentos)
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuarios)
        
    def leftMenu(self):
        width = self.left_container.width()
        if width == 9:
            newWidth = 200 
        else:
            newWidth = 9 
        self.animation = QtCore.QPropertyAnimation(self.left_container,b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def cadastrar_atendimentos(self):
            db = Data_base()
            db.connect()

            fullDataSet = (

                self.txt_amb.text(), self.txt_atendente.text(), self.txt_cbo.text(), self.txt_cpf.text(),
                self.txt_data.text(), self.txt_doc.text(), self.txt_motivo.text(), self.txt_nome.text(),
                self.txt_nome.text(), self.txt_pcd.text(), self.txt_resultado.text(),self.txt_tarefa.text(),self.txt_tipo.text()
            )

            #CADASTRAR NO BANCO DE DADOS
            resp = db.register_atendimento(fullDataSet)
            if resp == "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Casdastro Realizado")
                msg.setText("Cadastro Realizado com sucesso")
                msg.exec()
                db.close_connection()
                return
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro")
                msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
                msg.exec()
                db.close_connection()
                return
    def cadastrar_usuarios(self):
            db = Data_base()
            db.connect()

            fullDataSet = (

                self.cb_perfil.text(), self.txt_data_2.text(), self.txt_nome_2.text(), self.txt_senha.text(),
                self.txt_senha1.text(), self.txt_usuario.text())      

            #CADASTRAR NO BANCO DE DADOS
            resp = db.register_atendimento(fullDataSet)
            if resp == "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Casdastro Realizado")
                msg.setText("Cadastro Realizado com sucesso")
                msg.exec()
                db.close_connection()
                return
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro")
                msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
                msg.exec()
                db.close_connection()
                return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()