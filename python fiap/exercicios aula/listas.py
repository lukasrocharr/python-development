calorias = []
resposta = ""

while resposta.uppers() != "Não":
    caloria = int(input("Quantas calorias você consumiu nessa refeição?"))
    calorias.append(caloria)
    resposta = input("Você deseja informar a caloria de mais uma refeição?")

print(calorias)

total = 0
for caloria in calorias:
    print(f"Nesta refeição foram consumidas {caloria} calorias")
    total = total + caloria

    media = total / len(calorias)
    print(f"Neste dia, houve um consumo médio de {media} calorias por refeição")