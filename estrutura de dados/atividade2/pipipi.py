class No: 
    def __init__(self, valor):
        self.valor = valor.lower()
        self.prox = None 

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def existe(self, valor):
        no_atual = self.inicio
        while no_atual:
            if no_atual.valor.lower() == valor.lower():
                return True
            no_atual = no_atual.prox
        return False

    def vazia(self):
        return self.inicio is None

    def inserir_inicio(self, valor):
        if self.existe(valor):
            print(f"O valor '{valor}' já está cadastrado.")
            return
        
        novo_no = No(valor)
        novo_no.prox = self.inicio 
        self.inicio = novo_no
        print(f"O valor '{valor}' foi inserido no início.")

    def inserir_final(self, valor):
        if self.existe(valor): 
            print(f"O valor '{valor}' já existe.")
            return 
        
        novo_no = No(valor)
        if self.vazia():
            self.inicio = novo_no
        else:
            no_atual = self.inicio
            while no_atual.prox:
                no_atual = no_atual.prox
            no_atual.prox = novo_no
        print(f"O valor '{valor}' foi inserido no fim.")

    def delete(self, valor):
        if self.vazia():
            print("Lista vazia.")
            return False 

        no_atual = self.inicio
        anterior = None 

        while no_atual:
            if no_atual.valor.lower() == valor.lower():
                if anterior is None:
                    self.inicio = no_atual.prox
                else: 
                    anterior.prox = no_atual.prox
                print(f"O valor '{valor}' foi removido.")
                return 
            anterior = no_atual
            no_atual = no_atual.prox
        
        print(f"O valor '{valor}' não foi encontrado.")

    def delete_primeiro(self):
        if self.vazia():
            print("Lista vazia.")
        else:
            delete_valor = self.inicio.valor
            self.inicio = self.inicio.prox
            print(f"O valor '{delete_valor}' foi removido do início.")

    def delete_ultimo(self):
        if self.vazia():
            print("Lista vazia.")
        elif self.inicio.prox is None:
            remove_valor = self.inicio.valor
            self.inicio = None
            print(f"O valor '{remove_valor}' foi removido. A lista está vazia.")
        else:
            anterior = None
            no_atual = self.inicio
            while no_atual.prox:
                anterior = no_atual
                no_atual = no_atual.prox
            anterior.prox = None 
            print(f"O valor '{no_atual.valor}' foi removido do fim.")

    def print_lista(self):
        no_atual = self.inicio

        if no_atual is None:
            print("Lista vazia.")
            return

        print("Elementos: ", end="")
        while no_atual:
            print(no_atual.valor, end=" -> ")
            no_atual = no_atual.prox
        print("None")

    def contar(self):
        no_atual = self.inicio
        cont = 0

        if no_atual is None:
            print("Lista vazia.")
            return
        
        while no_atual:
            cont += 1
            no_atual = no_atual.prox
        print(f"Quantidade de elementos: {cont}")  


if __name__ == "__main__":
    lista = ListaEncadeada()

    while True:
        print("\nMenu de Opções: ")
        print("1. Inserir no início")
        print("2. Inserir no final")
        print("3. Remover item")
        print("4. Remover o primeiro item")
        print("5. Remover o último item")
        print("6. Mostrar elementos")
        print("7. Contar elementos")
        print("8. Sair")

        opcao = int(input("Escolha uma opção (1-8): "))

        match opcao:
            case 1: 
                valor = input("Valor a ser inserido no início: ")
                lista.inserir_inicio(valor)
            case 2:
                valor = input("Valor a ser inserido no final: ")
                lista.inserir_final(valor)
            case 3:
                valor = input("Valor a ser removido: ")
                lista.delete(valor)
            case 4: 
                lista.delete_primeiro()
            case 5:
                lista.delete_ultimo()
            case 6:
                lista.print_lista()
            case 7:
                lista.contar()
            case 8: 
                break
            case _:
                print("Opção inválida.")
