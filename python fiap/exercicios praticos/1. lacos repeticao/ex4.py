# Exercício 4: Supondo que a população de um país A seja da ordem de 80000 habitantes,
# com uma taxa anual de crescimento de 3%, e que a população de B seja 200000 habitantes,
# com uma taxa de crescimento de 1.5%, faça um programa que calcule e escreva o número
# de anos necessários para que a população do país A ultrapasse ou iguale a população
# do país B, mantidas as taxas de crescimento.

from time import sleep

pais1 = 80000
pais2 = 200000

anos = 0

while True:
    pais1 += (pais1 * 3) / 100
    pais2 += (pais2 * 1.5) / 100
    anos += 1
    print(anos)
    print(pais1)
    print(pais2)

    if pais1 >= pais2:
        print(pais1)
        print(pais2)
        print(anos)
    break
    
    sleep(5)