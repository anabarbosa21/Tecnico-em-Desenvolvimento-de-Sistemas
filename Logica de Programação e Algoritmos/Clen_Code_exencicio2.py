idade = int(input("Digite sua idade"))

if (idade >= 18):
    print("maior de idade")
elif(idade >= 0 and idade < 18):
    print("menor de idade")
else:
    print("idade invalida")
    