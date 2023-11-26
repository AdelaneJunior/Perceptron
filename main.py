import numpy as np
from random import randint

erro = 0
iteracoes = 1


def dados_entrada_treino():
    entrada_treino = [
        [1, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    return entrada_treino


def perceptron_treino(peso1, peso2, peso3):
    global iteracoes
    global erro
    if iteracoes == 1:
        print("começo")
        print("pesos iniciais: ", peso1, " ", peso2, " ", peso3,)
    neuronios = [peso1, peso2, peso3]
    entrada_treino = dados_entrada_treino()
    neuronios = treino_trabalho_neuronios(entrada_treino, neuronios)
    print("quantidade erros na", iteracoes,"iteração: ", erro)
    if erro > 0:
        iteracoes = iteracoes + 1
        erro = 0
        perceptron_treino(neuronios[0], neuronios[1], neuronios[2])
    return neuronios


def treino_trabalho_neuronios(entrada_treino, neuronios):
    valores = np.empty(3)
    for i in range(0, 4):
        # print("ciclo: ", i + 1)
        for j in range(0, 3):
            valores[j] = neuronios[j] * entrada_treino[i][j]
            # print("neuronio", j + 1, "entrada", j + 1, ": ", neuronios[j] * dados[i][j])
        neuronios = verifica_resultado(valores, i, neuronios, entrada_treino)
    return neuronios


def verifica_resultado(valores, ciclo, neuronios, entrada):
    resultado = int(np.sum(valores))
    if resultado >= 1:
        resultado = 1
    # print("resultado ciclo ", ciclo + 1, ": ", resultado)

    if ciclo == 0:
        if resultado != 0:
            return atualiza_peso_sub(ciclo, neuronios, entrada)
        return neuronios

    if ciclo == 1:
        if resultado != 1:
            return atualiza_peso_sum(ciclo, neuronios, entrada)
        return neuronios

    if ciclo == 2:
        if resultado != 1:
            return atualiza_peso_sum(ciclo, neuronios, entrada)
        return neuronios

    if ciclo == 3:
        if resultado != 0:
            return atualiza_peso_sub(ciclo, neuronios, entrada)
        return neuronios


def atualiza_peso_sub(ciclo, neuronios, entrada):
    global erro
    erro += 1
    for x in range(0, 3):
        if neuronios[x] != 0:
            neuronios[x] = neuronios[x] - entrada[ciclo][x]
    return neuronios


def atualiza_peso_sum(ciclo, neuronios, entrada):
    global erro
    erro += 1
    for x in range(0, 3):
        if neuronios[x] != 1:
            neuronios[x] = neuronios[x] + entrada[ciclo][x]
    return neuronios


def trabalho_neuronios(neuronios):
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


if __name__ == '__main__':
    neuronios_treinados = perceptron_treino(randint(0, 1), randint(0, 1), randint(0, 1))
    # neuronios_treinados = perceptron_treino(0, 0, 0, 0)
    continuar = "sim"
    print("Foram necessários " + str(iteracoes) + " para completar o aprendizado")
    while continuar != "nao":
        trabalho_neuronios(neuronios_treinados)
        continuar = input('continuar ? ')
