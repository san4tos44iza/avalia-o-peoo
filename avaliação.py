#alunas:Maria Eloiza Santos da silva e Rudmylla Monteiro Souza
class IngressoCinema:
    def __init__(self, data, sala, valor):
        self.data = data
        self.sala = sala
        self.valor = valor

    def calcular_desconto(self, idade):
        desconto = 0
        if 12 <= idade <= 15:
            desconto = self.valor * 0.4
        elif 16 <= idade <= 20:
            desconto = self.valor * 0.3
        elif idade > 20:
            desconto = self.valor * 0.2
        print(f"O valor do seu desconto é {desconto}")

    def set_sala(self, nova_sala):
        self.sala = nova_sala

    def get_sala(self):
        return self.sala


def main():
    data = input("Digite a data do ingresso: ")
    sala = int(input("Digite o número da sala: "))
    valor = float(input("Digite o valor do ingresso: "))

    ingresso = IngressoCinema(data, sala, valor)

    idade = int(input("Digite a sua idade para calcular o desconto: "))
    ingresso.calcular_desconto(idade)

    nova_sala = int(input("Digite o novo número da sala: "))
    ingresso.set_sala(nova_sala)
    print("A nova sala é:", ingresso.get_sala())

main()