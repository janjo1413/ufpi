from simplesmenteEncadeada import ListaEncadeada
from duplamenteEncadeada import ListaDuplamenteEncadeada
def main():

    choice = int(input("Para Lista Encadeada Simples - 1\nPara Lista Encadeada Dupla - 2\n"))

    match choice:
        case 1:
            lista_encadeada = ListaEncadeada()

            while True:
                print("\nOpções:")
                print("1. Inserir no início")
                print("2. Inserir no final")
                print("3. Verificar se um elemento existe")
                print("4. Excluir um elemento")
                print("5. Mostrar todos os elementos")
                print("6. Sair")

                opcao = int(input("Escolha uma opção (1-6): "))

                match opcao:
                    case 1: 
                        elemento = (input("Digite o valor a ser inserido no início: "))
                        lista_encadeada.inserir_no_inicio(elemento)
                    case 2: 
                        elemento = (input("Digite o valor a ser inserido no final: "))
                        lista_encadeada.inserir_no_final(elemento)        
                    case 3:
                        elemento = (input("Digite o valor a ser procurado: "))   
                        if lista_encadeada.busca(elemento):
                            print(f"O elemento {elemento} está na lista.")
                        else:
                            print(f"O elemento {elemento} não está na lista.")    
                    case 4:
                        elemento = (input("Digite o valor a ser excluído: "))
                        lista_encadeada.deletar(elemento)
                    case 5:
                        lista_encadeada.printar_lista()
                    case 6:
                        print("Encerrando a aplicação")
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")

        case 2:
            lista_encadeada = ListaDuplamenteEncadeada()

            while True:
                print("\nOpções:")
                print("1. Inserir um elemento (em ordem crescente)")
                print("2. Verificar se um elemento existe")
                print("3. Excluir um elemento")
                print("4. Mostrar todos os elementos")
                print("5. Sair")

                opcao = int(input("Escolha uma opção (1-5): "))

                match opcao:
                    case 1:
                        elemento = input("Digite o valor a ser inserido: ")
                        lista_encadeada.inserir_ordenado(elemento)
                    case 2:
                        elemento = input("Digite o valor a ser procurado: ")
                        if lista_encadeada.busca(elemento):
                            print(f"O elemento {elemento} está na lista.")
                        else:
                            print(f"O elemento {elemento} não está na lista.")
                    case 3:
                        elemento = input("Digite o valor a ser excluído: ")
                        lista_encadeada.deletar(elemento)
                    case 4:
                        lista_encadeada.printar_lista()
                    case 5:
                        print("Encerrando a aplicação.")
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()