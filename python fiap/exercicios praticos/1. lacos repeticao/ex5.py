#Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.
from time import sleep
n = int(input())

somatorio = 1

for i in range(n, 0, -1):
    somatorio = somatorio * i
    print(somatorio)