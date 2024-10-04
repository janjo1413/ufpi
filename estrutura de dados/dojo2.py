def menu():
    print("Escolha entre as opções: ")
    print("(1) Incluir")
    print("(2) Alterar")
    print("(3) Excluir")
    print("(4) Pesquisar")
    print("(5) Listar todos")
    print("(9) Sair")

while True:
    menu()
    result = int(input("Digite sua opção:"))

    if result >= 1 and result <= 5:
        print("não disponível")
    elif result == 9:
        print("Saindo do Programa")
        break
    else:
        print("opção inválida")
