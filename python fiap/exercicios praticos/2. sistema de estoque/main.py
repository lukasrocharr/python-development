"""
Sistema de estoque

Você vai desenvolver um sistema onde o usuário informa o nome de um produto e a quantidade inicial em estoque.
Depois, o programa permite registrar entradas e saídas, atualizando o estoque automaticamente.

Regras do exercício:
- O usuário deve informar:
  - Nome do produto
  - Quantidade inicial
- O sistema deve perguntar:
  - Se deseja adicionar ou retirar itens
- Se for adicionar:
  - Somar ao estoque atual
- Se for retirar:
  - Verificar se tem quantidade suficiente
  - Se não tiver, mostrar erro
- Mostrar o estoque atualizado no final
"""

produto = str(input("Digite o nome do produto: "))
estoque = int(input("Digite a quantidade inicial: "))

print("\n O que você deseja fazer?")
print("(1) Adicionar produtos ")
print("(2) Retirar produtos ")

opcao = str(input("Escolha uma opção: "))

if opcao == "1":
    quantidade = int(input("Digite a quantidade: "))
    estoque = estoque + quantidade
    print(f"Estoque atualizado de {produto} {estoque}")
elif opcao == "2":
    quantidade = int(input("Digite a quantidade: "))
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print(f"Estoque atualizado {produto}: {estoque}")
    else: 
        print("\nErro: estoque insuficiente")
else:
    print("\nOpcao invalida")