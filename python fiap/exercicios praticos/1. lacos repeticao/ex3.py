# Exercício 3: Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v' ou 'd'.

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario = float(input('Salário: '))
    sexo = input('(F) ou (M)')
    estado_civil = input('(s), (c), (v), ou (d)')
    if (
    len(nome) <= 3 or (idade < 0 or idade > 150 ) or salario <= 0 or sexo.lower() not in ('f', 'm') or estado_civil not in ('s', 'c', 'v', 'd')
):
        print('Dados Inválidos. Digite novamente')
    continue

    break