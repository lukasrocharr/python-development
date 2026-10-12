opcao = 0

while opcao != 3:
    print("1 - receber um elogio")
    print("2 - calcular o fatorial")
    print("3 - sair")
    opcao = int(input("Digite a opcao desejada"))
    
    if opcao == 1:
        print("Legal")

    elif opcao == 2:
        numero = int(input("Informe o numero"))
        fat = numero

        for valor in range (1, numero , 1):
            fat = fat * valor
            print (f"O valor fatotorial é: {fat}")
    elif opcao == 3:
        print("Saindo do sistema...")
    else:
            print("escolha uma opçcao do menu")