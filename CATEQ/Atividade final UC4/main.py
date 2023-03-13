from Controle.classConexao import Conexao
import psycopg2


def inserirOpcoes(con):
    cursor = con.cursor()
    ambiente = input("Insira o local de atendimento: ")
    tipodeatendimento = input("Insira o tipo de atendimento: ")
    tipodedocumento = input("Insira o tipo documento de identificação: ")
    tipodepessoa = input("Insira o tipo de pessoa(Fisica ou Jurídica): ")
    atendente = input("Insira o nome do atendente: ")
    tarefa = input("Insira a tarefa: ")
    resultado = input("Insira a conclusão: ")
    motivo = input("Insira o motivo do nao encaminhamento: ")
    titulo = input("Insira a vaga correspondente: ")

    cursor.execute(f'''
    INSERT INTO "Opcoes"
    VALUES ('{ambiente}', '{tipodeatendimento}','{tipodedocumento}',
    '{tipodepessoa}','{atendente}','{tarefa}','{resultado}','{motivo}','{titulo}')
    ''')

    con.commit()

    cursor.close()

try:
    con = psycopg2.connect(database="Atendimento",host="localhost",port="5432",user="postgres",password="postgres")

except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro -",error)

while True:
    try:

        print('''
        1. Inserir Opções
        0. Sair
        ''')
        opcoes = input("Escolha uma opção: ")

        match opcoes:

            case "1":
                inserirOpcoes(con)
                

            case "0":
                con.close()
                break

            case _:
                print("Opção inválida")

        input("Tecle Enter para continuar")

    except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro",error)        
    