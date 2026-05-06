notas = []

for i in range(4):
    #Tenta solicitar as nota
    try:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if(nota < 0 or nota >  10):
            print("nota invalida. insira um valor entre 0 e 10!")
            exit()
        else:
            notas.append(notas)
    #se tiver algum erro (excesssão) de valor, retorna uma mensagem
    except ValueError:
        print("Erro: Insira um numero valido!")

#se a pessoa apenas digitou texto
if not notas:
    print("Erro: Nenhuma nata foi inserido!")
else:
    media = sum(notas)/len(notas)

    if(media >= 7):
        print(f"Media = {media} - Aprovado!")
    elif(media >= 5):
        print(f"Media = {media} - Recuperação!")
    else:
        print(f"Media = {media} - Reprovado!")
