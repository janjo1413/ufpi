import random

class Carta:
    valores = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"{self.valor}"

    def valor_numerico(self):
        return self.valores[self.valor]


class Baralho:
    def __init__(self):
        self.cartas = [Carta(valor) for valor in Carta.valores for _ in range(4)]  
        random.shuffle(self.cartas)

    def puxar_carta(self):
        return self.cartas.pop() if self.cartas else None


class Jogador:
    def __init__(self):
        self.mao = []
        self.pontuacao = 0

    def adicionar_carta(self, carta):
        self.mao.append(carta)
        

        if carta.valor == 'A':
            escolha = input("você recebeu um Ás, deseja que ele valha 11 ou 1? (Digite 11 ou 1): ")
            if escolha == '1':
                self.pontuacao += 1
            else:
                self.pontuacao += 11
        else:
            self.pontuacao += carta.valor_numerico()

    def mostrar_mao(self):
        cartas_mao = ', '.join(str(carta) for carta in self.mao)
        return f"mão: {cartas_mao} | pontuação: {self.pontuacao}"


def proximidade_de_21(pontuacao):
    return abs(21 - pontuacao)

def jogo_blackjack():
    baralho = Baralho()
    jogador = Jogador()
    
    oponente_pontuacao = random.randint(18, 23)

    tentativas = 0
    while tentativas < 4:
        carta = baralho.puxar_carta()
        if not carta:
            print("só pode pegar ate 4 cartas")
            break
        jogador.adicionar_carta(carta)
        print(jogador.mostrar_mao())
        
        if jogador.pontuacao == 21:
            print("21 !!!")
            break
        else:
            acao = input("pegar mais uma carta? (s/n): ").lower()
            if acao == 'n':
                print(f"você tem {jogador.pontuacao} pontos.")
                break
        tentativas += 1
    
    print(f"\npontuação do oponente: {oponente_pontuacao}")
    jogador_prox = proximidade_de_21(jogador.pontuacao)
    oponente_prox = proximidade_de_21(oponente_pontuacao)

    if jogador_prox < oponente_prox:
        print(f"venceu sua pontuação: {jogador.pontuacao}, oponente: {oponente_pontuacao}")
    elif jogador_prox > oponente_prox:
        print(f"perdeu sua pontuação: {jogador.pontuacao}, oponente: {oponente_pontuacao}")
    else:
        print(f"empate sua pontuação: {jogador.pontuacao}, oponente: {oponente_pontuacao}")

if __name__ == '__main__':
    jogo_blackjack()
