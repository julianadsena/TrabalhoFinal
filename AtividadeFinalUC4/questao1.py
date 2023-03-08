### Escreva um programa que leia um arquivo de texto e retorne a quantidade
### de palavras diferentes que aparecem no arquivo

arq = open("texto_Dia_Mulher.txt")
linhas = arq.readlines()
palavrasVistas = []
for linha in linhas:
    for palavra in linha.split(" "):
        if palavra not in palavrasVistas:
            palavrasVistas.append(palavra)


print(palavrasVistas)
print("Quantidade de palavras é", len(palavrasVistas))
print(f'{len("texto_Dia_Mulher")}caracteres carregados.')