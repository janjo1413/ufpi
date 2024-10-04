alunos = []
menu = 0

while(menu != 5):

    menu = int(input("Bem vindo ao menu \n (1) Cadastre um aluno \n (2) Chame um aluno em especifico \n (3) Exibir a lista de alunos em ordem alfabetica \n (4) Remova um aluno da lista \n (5) Sair \n O que vai fazer agora?: "))
    
    if menu == 1:

        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)


    elif menu == 2:

        numAluno = int(input("Digite o numero do aluno (começa em 0): "))

        while numAluno >= len(alunos):

            print("Numero maior que a quantidade de alunos. Tente novamente.")
            numAluno = int(input("Digite o numero do aluno (começa em 0): "))


        print(f"Aluno {numAluno}: {alunos[numAluno]}")


    elif menu == 3:

        alunosOrdenados = sorted(alunos)
        print("Lista de alunos em ordem alfabética:")
        print(alunosOrdenados)



    elif menu == 4:

        numAluno = int(input("Digite o numero do aluno que deseja remover (começa em 0): "))

        while numAluno >= len(alunos):

            print("Numero maior que a quantidade de alunos. Tente novamente.")
            numAluno = int(input("Digite o numero do aluno que deseja remover (começa em 0): "))
            
        del alunos[numAluno]
        print("Aluno removido com sucesso.")
