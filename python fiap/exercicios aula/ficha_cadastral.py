print('Cadastro de doadores de sangue')

nome = input("Insira seu nome completo: ")
peso = float(input("Insira seu peso: "))
altura = int(input("Insira sua altura (cm): "))
ano_nascimento = int(input("Insira seu ano de nascimento: "))


idade = 2022 - ano_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso} kg\n\tALTURA: {altura} cm\n\tIDADE: {idade}\n\tTEM PESO MINIMO PARA DOAR: {tem_peso_minimo}\n\tTEM IDADE MINIMA PARA DOAR {tem_idade_minima}"

print(texto_saida)