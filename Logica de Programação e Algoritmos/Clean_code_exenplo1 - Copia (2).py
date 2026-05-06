#Codigo Ruim
a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = (a + b + c + d) /4

if x >= 5:
    print("OK")
elif x >= 5:
    print("REC")
else:
    print("NO")

#CLEAN CODE 1

#CLEAN CODE 2
notas = []

for i in range(4):
    notas.append(float(input(f"Digitema {i+1}ª nota:")))
media = sum(notas)/len(notas)

if(media >= 7):
    print("Aprovado!")
if(media >= 5):
    print("Recuperaçao!")
elif(media < 5):
    print("Reprovado!")
else:
    print("Dados invalido!")


