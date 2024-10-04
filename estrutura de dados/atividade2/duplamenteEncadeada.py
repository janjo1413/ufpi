class Node:
    #método construtor da classe Node
    def __init__(self, entrada):
        self.data = entrada.lower()  #Conteúdo qeu vai ser armazenado no nó, passado pelo usuário
        self.next = None  #Ponteiro que aponta para o nó sucessor, inicializado com None para indicar que não possui sucessor ainda
        self.prev = None  #Ponteiro que aponta para o nó anterior, incializado com None para indicar que não possui antecessor ainda

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None  # A lista começa vazia, pois ponteiro cabeça é None

    # Inserir um elemento em ordem crescente
    def inserir_ordenado(self, entrada):
        new_node = Node(entrada) #cria um novo nó

        # Se a lista estiver vazia, o novo nó se torna a cabeça
        if self.head is None:
            self.head = new_node
            return #sai do método

        # Se o elemento for menor que o elemento da cabeça, insere antes da cabeça
        if entrada < self.head.data:
            new_node.next = self.head #aqui o ponteiro next do novo nó vai apontar para o nó que era a antiga cabeça
            self.head.prev = new_node #aqui o ponteiro prev da antiga cabeça agora vai apontar para o novo nó
            self.head = new_node #aqui atualiza o ponteiro head, para que o novo nó seja a cabeça
            return

        # Caso contrário, percorre a lista para encontrar a posição correta
        atual = self.head #inicia a variável "atual" apontando para o primeiro nó da lista(cabeça)
        while atual.next and atual.next.data < entrada.lower(): #atual.next verifica se o nó atual tem um proximo nó, caso ele aponte para None sabemos que está no final da lista
            #atual.next.data < data verifica se o valor armazenado no proximo nó é menor do que o valor que vamos inserir, se for menor, continua, caso contrário, achamos a posição
            atual = atual.next #atualiza o nó atual, avançando até encontrar a posição correta

        # Inserção no final
        if atual.next is None: #se o nó atual apontar para None, ele é o último
            atual.next = new_node #se for o último nó, vamos inserí-lo após o nó atual
            new_node.prev = atual #atualiza o ponteiro prev do novo nó para apontar para o nó atual
        else:
            # Inserção vai ser realizada entre dois nós
            new_node.next = atual.next #faz o ponteiro next do novo nó apontar para o próximo nó
            atual.next.prev = new_node # faz o ponteiro prev do próximo nó apontar para o novo nó
            atual.next = new_node #faz o ponteiro next do nó atual apontar para o novo nó
            new_node.prev = atual #faz o ponteiro prev do novo nó apontar para o, agora, nó anterior

    # Verificar se um elemento existe na lista
    def busca(self, entrada):
        node_atual = self.head #inicia a busca pela cabeça
        while node_atual: #percorre a lista enquanto restarem nós
            if node_atual.data == entrada.lower():
                return True #retorna true caso encontre o elemento buscado
            node_atual = node_atual.next #avança para o próximo nó
        return False

    # Remover um elemento da lista
    def deletar(self, entrada):
        node_atual = self.head

        # Se a lista estiver vazia
        if node_atual is None: #se a cabeça for None
            print("A lista está vazia.")
            return

        # Se o elemento a ser removido for a cabeça
        if node_atual.data == entrada.lower():
            self.head = node_atual.next #a cabeça agora vai ser o próximo elemento
            if self.head: #esse if é executado caso a cabeça não aponte para um valor nulo, significando que existe um próximo elemento
                self.head.prev = None #agora atualizamos o valor que o ponteiro prev aponta para nulo, pois o novo nó cabeça não pode ter um nó anterior
            node_atual = None #atualiza o valor do elemento a ser removido(node_atual) para None, assegurando a remoção
            return

        # Percorrer a lista para encontrar o nó a ser deletado
        while node_atual and node_atual.data != entrada.lower():
            node_atual = node_atual.next

        # Se o nó não foi encontrado
        if node_atual is None:
            print(f"O elemento {entrada} não está na lista.")
            return

        # Ajustar os ponteiros para remover o nó
        if node_atual.next:
            node_atual.next.prev = node_atual.prev
        if node_atual.prev:
            node_atual.prev.next = node_atual.next
        node_atual = None

    # Mostrar todos os elementos e a quantidade
    def printar_lista(self):
        node_atual = self.head
        contador = 0

        if node_atual is None:
            print("A lista está vazia.")
            return

        print("Elementos da lista:", end=" ")
        while node_atual:
            print(node_atual.data, end=" <-> ")
            contador += 1
            node_atual = node_atual.next
        print("None")  # Indica o final da lista
        print(f"Quantidade de elementos: {contador}")

    