conjunto1 = set(input("Digite cores para o primeiro conjunto, separadas por espaço: ").split())
conjunto2 = set(input("Digite cores para o segundo conjunto, separadas por espaço: ").split())
conjunto3 = set(input("Digite cores para o terceiro conjunto, separadas por espaço: ").split())

menu = 0

while menu != 4:
    menu = int(input("\nBem-vindo ao menu\n(1) União de listas\n(2) Interseção de listas\n(3) Diferença de listas\n(4) Sair\nO que vai fazer agora?: "))

    if menu == 1:

        escolha = input("Quais das listas você quer unir? (12, 123, 23, 13): ")

        if escolha == "12":

            conjuntouniao = conjunto1.union(conjunto2)

        elif escolha == "23":

            conjuntouniao = conjunto2.union(conjunto3)

        elif escolha == "13":

            conjuntouniao = conjunto1.union(conjunto3)

        elif escolha == "123":

            conjuntouniao = conjunto1.union(conjunto2).union(conjunto3)

        print(f"União: {conjuntouniao}")

    elif menu == 2:

        escolha = input("Quais das listas você quer ver a interseção? (12, 123, 23, 13): ")

        if escolha == "12":

            conjuntointersecao = conjunto1.intersection(conjunto2)

        elif escolha == "23":

            conjuntointersecao = conjunto2.intersection(conjunto3)

        elif escolha == "13":

            conjuntointersecao = conjunto1.intersection(conjunto3)

        elif escolha == "123":

            conjuntointersecao = conjunto1.intersection(conjunto2).intersection(conjunto3)

        print(f"Interseção: {conjuntointersecao}")

    elif menu == 3:

        escolha = input("Quais das listas você quer ver a diferença? (12, 123, 23, 13): ")

        if escolha == "12":

            conjuntodiferenca = conjunto1.difference(conjunto2)

        elif escolha == "23":

            conjuntodiferenca = conjunto2.difference(conjunto3)

        elif escolha == "13":
            
            conjuntodiferenca = conjunto1.difference(conjunto3)

        elif escolha == "123":

            conjuntodiferenca = conjunto1.difference(conjunto2).difference(conjunto3)

        print(f"Diferença: {conjuntodiferenca}")

    elif menu == 4:

        print("Programa encerrado.")

    else:
        
        print("Opção inválida! Tente novamente.")
