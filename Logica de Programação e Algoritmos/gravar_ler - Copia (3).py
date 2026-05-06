#importar as bibliotecas
import pandas as pd
import os

dados = {
    "Nome": [],
    "Idade": [],
    "Cidade": []
}

deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    dados["Nome"].append(nome)
    dados["Idade"].append(idade)
    dados["Cidade"].append(cidade)
    
    deseja_continuar = input("Deseja continuar? (s/n)").strip().lower()
    #strip() -> tirar espaços em branco
    #lower() -> transformar em minúsculo

df = pd.DataFrame(dados)
print(df)

print("\n Escolher o formato para salvar os dados:")
print("1 - CSV \n2 - JSON \n 3 - TXT")
escolha_arquivo = input("Digite o numero do formato desejado: ")

#definir o caminho onde sera salvo o arquivo
os.chdir("C:\\Users\\56646708860\\Documents\\Gravação_Letura_Arquivos_Python\\")

if(escolha_arquivo == "1"):
    df.to_csv("dados.csv", index=False)
    print("Dados salvo em 'dados.csv'!")
elif(escolha_arquivo == "2"):
    df.to_json("dados.json", orient="records", indent=4)
    print("Dados salvo em 'dados.json'!")
elif(escolha_arquivo == "3"):
    df.to_csv("dados.txt", sep="\t", index=False)
    print("Dados salvo em 'dados.txt'!")
else:
    print("Escolha invalida! os dados foram salvos!")

#Leitura dos arquivos
ler_arquivo = input("\n Deseja carregar dados? (s/n):").strip().lower()
if(ler_arquivo == "s"):
    print("\n Escola o formato para ler o arquivo: ")
    print("1 - CSV \n2 - JSON \n 3 - TXT")
    escolha_formato = input("Digite o numero do formato desejado:")
    #try -> tenta executar esse bloco
    try:
        if(escolha_formato == "1"):
            df_lido = pd.read_csv("dados.csv")
        elif(escolha_formato == "2"):
             df_lido = pd.read_json("dados.json")
        elif(escolha_formato == "3"):
             df_lido = pd.read_csv("dados.txt", sep="\t")
        else:
            print("Formato Invalido!")
            df_lido = None

        if(df_lido is not None):
            print("\n Dados Carregados: ")
            print(df_lido)
    except FileNotFoundError:
        print("\n Arquivo não encontrado!")
