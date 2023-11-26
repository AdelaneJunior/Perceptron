import numpy as np
from random import randint

erro = 0
ciclos = 1


# vetor com valores de inciais para o treinamento
def dados_entrada_treino():
    entrada_treino = [
        [1, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    return entrada_treino


# iniciação dos neuronios com pesos aleatórios e os passando para treino
def perceptron_treino(peso1, peso2, peso3):
    global ciclos
    global erro
    if ciclos == 1:
        print("começo")
        print("pesos iniciais: ", peso1, " ", peso2, " ", peso3, )
    neuronios = [peso1, peso2, peso3]
    entrada_treino = dados_entrada_treino()
    neuronios = treino_trabalho_neuronios(entrada_treino, neuronios)
    print("cliclo", ciclos, "quantidade erros: ", erro)
    if erro > 0:
        ciclos = ciclos + 1
        erro = 0
        perceptron_treino(neuronios[0], neuronios[1], neuronios[2])
    return neuronios


# entrada dos valores de treino e trabalho dos neuronios
def treino_trabalho_neuronios(entrada_treino, neuronios):
    valores = np.empty(3)
    for i in range(0, 4):
        # print("ciclo: ", i + 1)
        for j in range(0, 3):
            valores[j] = neuronios[j] * entrada_treino[i][j]
            # print("neuronio", j + 1, "entrada", j + 1, ": ", neuronios[j] * dados[i][j])
        neuronios = verifica_resultado(valores, i, neuronios, entrada_treino)
    return neuronios


# validação do resultado obtido através dos neuronios conforme o ciclo em questão
# e envio para manutenção nos pesos
def verifica_resultado(valores, iteracao, neuronios, entrada):
    resultado = int(np.sum(valores))
    if resultado >= 1:
        resultado = 1

    # validação do resultado obtido conforme o ciclo em questão
    if iteracao == 0:
        if resultado != 0:
            return atualiza_peso_sub(iteracao, neuronios, entrada)
        return neuronios

    if iteracao == 1:
        if resultado != 1:
            return atualiza_peso_sum(iteracao, neuronios, entrada)
        return neuronios

    if iteracao == 2:
        if resultado != 1:
            return atualiza_peso_sum(iteracao, neuronios, entrada)
        return neuronios

    if iteracao == 3:
        if resultado != 0:
            return atualiza_peso_sub(iteracao, neuronios, entrada)
        return neuronios


# manutenção dos pesos dos neuronios em caso de necessidade de subtração
def atualiza_peso_sub(iteracao, neuronios, entrada):
    global erro
    erro += 1
    for x in range(0, 3):
        if neuronios[x] != 0:
            neuronios[x] = neuronios[x] - entrada[iteracao][x]
    return neuronios


# manutenção dos pesos dos neuronios em caso de necessidade de adição
def atualiza_peso_sum(iteracao, neuronios, entrada):
    global erro
    erro += 1
    for x in range(0, 3):
        if neuronios[x] != 1:
            neuronios[x] = neuronios[x] + entrada[iteracao][x]
    return neuronios


# entrão os neuronios treinados e realizam seu trabalho
def trabalho_neuronios(neuronios):
    continuar = "sim"
    while continuar != "nao":
        primeira_pergunta = input('Primeira pergunta: ')
        entrada1 = 1 if primeira_pergunta == "sim" else 0
        segunda_pergunta = input('Segunda pergunta: ')
        entrada2 = 1 if segunda_pergunta == "sim" else 0
        terceira_pergunta = input('Terceira pergunta: ')
        entrada3 = 1 if terceira_pergunta == "sim" else 0
        entrada = [entrada1, entrada2, entrada3]
        print(entrada)
        valores = np.empty(3)
        for i in range(0, 3):
            valores[i] = neuronios[i] * entrada[i]
        resultado = int(np.sum(valores))
        if resultado >= 1:
            resultado = 1
        print("resultado: ", resultado)
        continuar = input('continuar ? ')


if __name__ == '__main__':
    neuronios_treinados = perceptron_treino(randint(0, 1), randint(0, 1), randint(0, 1))
    print("Necessário(s) " + str(ciclos) + " ciclo(s) para completar o aprendizado")
    trabalho_neuronios(neuronios_treinados)
