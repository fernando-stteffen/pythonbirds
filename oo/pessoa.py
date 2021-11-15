class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=32):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    raul = Pessoa(nome='Raul')
    sophia = Pessoa(nome='Sophia')
    fernando = Pessoa(raul, sophia, nome='Fernando')

    print(Pessoa.cumprimentar(fernando))
    print(id(fernando))
    print(fernando.cumprimentar())
    print(fernando.nome)
    print(fernando.idade)

    for filho in fernando.filhos:
        print(filho.nome)

    fernando.sobrenome = 'Stteffen'
    fernando.olhos = 1
    print(fernando.__dict__)
    print(raul.__dict__)
    print(Pessoa.olhos)
    print(fernando.olhos)
    print(raul.olhos)
    print(id(Pessoa.olhos), id(fernando.olhos), id(raul.olhos))