rota = []
menu = 0

while menu != 4:  

    
    menu = int(input("Bem vindo ao menu \n (1) Adicionar um novo ponto GPS \n (2) Remova um ponto GPS \n (3) Exibir rota atual \n (4) Sair \n O que vai fazer agora?: "))

    if menu == 1:
        inputGPS = input("Qual a rota? (Separado por virgula): ")
        rotaGPS = tuple(inputGPS.split(","))  
        rota.append(rotaGPS)  

    elif menu == 2:
        removedor = int(input("Qual ponto você deseja remover? (Começa em 0): "))
        if removedor < len(rota):  
            del rota[removedor]  
        else:
            print("indice invalido tente novamente")

    elif menu == 3:
        print("Rota atual:", rota)  

    elif menu > 4 or menu < 1:
        print("Valor incorreto")

print("Saindo do programa.")
