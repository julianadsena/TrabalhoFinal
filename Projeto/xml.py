import os
import xml.etree.ElementTree as Et

class Read_xml():
    def __init__(self,directory) -> None:
        self.directory = directory
    def all_files(self):
        return [os.path.join(self.directory,arq) for arq in os.listdir(self.directory)
        if arq.lower().endswith(".xml")]
    def check_none(self,var):
        pass
    def format_cpf(self,cpf):
        try:
            cpf = f'{cpf[:3]}.{cpf[4:7]}.{cpf[7:10]}-{cpf[10:12]}'
            return cpf
        except: 
            return ""
    def atd_data(self,xml):
        root = Et.parse(xml).getroot()
        nsData = {"ns":"file:///C:/Users/User/Desktop/Projetos%20TI/ctps/BC1_2023%20-%20CONTROLE%20DE%20ATENDIMENTO.xml"}
        
