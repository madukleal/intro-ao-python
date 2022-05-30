# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class CarroDaMadu:
    def __init__(self):
        self.on = False
        self.color = 'pink: #ffc0cb'
        self.model = 'MADU01'
        self.speed = 0

    def girar_chave(self, direcao):
        if direcao == 'horario':
            self.on = True
        else:
            self.on = False

    def speedup(self):
        if self.on:
            self.speed += 1

    def slowdown(self):
        self.speed -= 1

    def stop(self):
        while self.speed > 0:
            self.slowdown()



# Crie uma instância da classe carro.
carro_01 = CarroDaMadu()

# Faça o carro "andar" utilizando os métodos da sua classe.

# ligando o carro
sentido_da_chave = 'horario'
carro_01.girar_chave(sentido_da_chave)
print(f'você girou a chave no sentido: {sentido_da_chave} e o carro ligou')

for _ in range(25):
    carro_01.speedup()
print(f'a velocidade do carro é {carro_01.speed} km/h')

# Faça o carro "parar" utilizando os métodos da sua classe.
carro_01.stop()
print(f'a velocidade do carro é {carro_01.speed} km/h')
