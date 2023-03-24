from os import access
from PySide2.QtWidgets import (QApplication,QMainWindow,QWidget,QMessageBox)
from ui_login import Ui_Form
import sys  
from ui_tela import Ui_MainWindow
from database import DataBase
import sqlite3
import pandas as pd

class MainWindow (QMainWindow,Ui_MainWindow):
    def __init__(self,username,user):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento de atendimento")
        self.user = username 
        if user.lower() == "user":
            self.pushButton_3.setVisible(False)
        # paginas do sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_tables))
        self.pushButton_3.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page))
        self.btn_outro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_2))
        self.pushButton_2.clicked.connect(self.subscribe_user)
        self.pushButton_2.clicked.connect(self.subscribe_user)

    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_novasenha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divergentes")
            msg.setText("A senha não é igual!")
            msg.exec_()
            return None
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        senha = self.txt_senha.text()
        access = self.cb_perfil.currentText()
        db = DataBase()
        db.conectar()
        db.insert_user(nome,user,senha,access)

        db.close_connection()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_novasenha.setText("")





class Login(QWidget, Ui_Form):
    
    def __init__(self) -> None:
        super(Login,self).__init__()
        self.tentativa = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.pushButton.clicked.connect(self.checkLogin)
    def checkLogin(self):
        self.users = DataBase()
        self.users.conectar()
        autenticado =  self.users.check_user(self.txtUser.text().upper(), self.txtSenha.text())

        if autenticado.lower() == "administrador" or autenticado.lower == "user":
            self.w = MainWindow(self.txtUser.text(), autenticado.lower())            
            self.w.show()
            self.close()
        else:
            if self.tentativa < 3: 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativa + 1} de 3')
                msg.exec_()
                self.tentativa += 1
            if self.tentativa == 3:
                self.users.close_connection()
                sys.exit(0)
    # def open_system(self):
    #     if self.txtSenha.text() == "123":
    #         self.w=MainWindow(autenticado.lower())
    #         self.w.show()
    #         self.close()
    #     else:
    #         print('senha inválida')
   
    
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
