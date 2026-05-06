notas = []

for i in range(4):
    notas.append(float(input(f"Digitema {i+1}ª nota:")))

media = sum(notas)/len(notas)
print("A media é:",media)

