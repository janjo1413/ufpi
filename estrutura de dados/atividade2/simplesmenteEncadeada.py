class Node:
    def __init__(self, entrada):
        self.data = entrada.lower() #dado armazenado no nó, garantindo que seja sempre minúsculo
        self.next = None #próxima refência, inicialmente é None

class ListaEncadeada:
    def __init__(self):
        self.head = None #lista, inicialmente, vazia

    def ja_existe(self, entrada):
        node_atual = self.head
        while node_atual:
            if node_atual.data == entrada.lower(): #assegurar a comparação case-insensitive
                return True
            node_atual = node_atual.next
        return False    

    #método para inserir um novo node no início de cada lista
    def inserir_no_inicio(self, entrada):
        if self.ja_existe(entrada):
            print("Já cadastrado.")
            return
        new_node = Node(entrada) #cria um novo node
        new_node.next = self.head # o novo aponta para o antigo primeiro nó
        self.head = new_node #atualiza a cabeça da lista para o novo nó

    #método para inserir um novo nó no final de cada lista
    def inserir_no_final(self, entrada):
        if self.ja_existe(entrada):
            print("Já cadastrado.")
            return
        new_node = Node(entrada)  #Cria um novo nó com o dado fornecido

        #se a lista estiver vazia, o novo nó que será a cabeça
        if self.head is None:
            self.head = new_node
            return
        
        ultimo_node = self.head
        while ultimo_node.next:
            ultimo_node = ultimo_node.next #percorre até o último node
        ultimo_node.next = new_node #aponta o último nó para o novo nó     

    #método para verificar se um elemento existe na lista
    def busca(self, entrada):
        node_atual = self.head

        while node_atual:
            if node_atual.data == entrada.lower():
                return True #elemento foi encontrado
            node_atual = node_atual.next

        return False

    #método para remover um elemento da lista
    def deletar(self, entrada):
        node_atual = self.head

        #caso a lista esteja vazia
        if node_atual is None:
            print("A lista está vazia")
            return

        #se o elemento a ser removido for o elemento cabeça
        if node_atual.data == entrada.lower():
            self.head = node_atual.next #a cabeça passa a ser o próximo node
            node_atual = None
            return
        
        #percorre a lista para encontrar o node a ser deletado
        node_anterior = None
        while node_atual and node_atual.data != entrada.lower():
            node_anterior = node_atual
            node_atual = node_atual.next

        #se o elemento não foi encontrado
        if node_atual is None:
            print(f"O elemento {entrada} não está na lista.")
            return

        #remover o node
        node_anterior.next = node_atual.next
        node_atual = None    

    #método para imprimir os elementos da lista
    def printar_lista(self):
        node_atual = self.head
        contador = 0
        
        if node_atual is None:
            print('A lista está vazia.')
            return
        
        print("Elementos da lista:", end=" ")
        while node_atual:
            print(node_atual.data, end=" -> ")
            contador += 1
            node_atual = node_atual.next
        print("None") #indica o final da lista
        print(f"Quantidade de elementos: {contador}")     


