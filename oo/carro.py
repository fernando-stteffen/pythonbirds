""""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes

1) Motor
2) Direcao

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelarar, que deverá incrementar a velocidade de uma unidade
3) Método frear, que deverar decretar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção.
ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Lest, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

    N
O       L
    S

    Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade()
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    # Teste Direcao
    >>> direcao = Direcao()
    >>> direcao.sentido
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.sentido
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.sentido
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.sentido
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.sentido
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.sentido
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.sentido
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.sentido
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.sentido
    'Norte'

    #Teste Carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""