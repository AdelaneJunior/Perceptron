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


# iniciação dos neuronios com pesos aleatórios
# e os passando para treino
def perceptron_treino(peso1, peso2, peso3):
    global ciclos
    global erro
    if ciclos == 1:
        print("começo")
        print("pesos iniciais: ", peso1, " ", peso2, " ", peso3, )
    neuronios = [peso1, peso2, peso3]
    entrada_treino = dados_entrada_treino()
    neuronios = treino_trabalho_neuronios(entrada_treino, neuronios)
    print("ciclo", ciclos, "quantidade erros: ", erro)
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


# validação do resultado obtido através dos neuronios
# conforme a iteracao em questão e envio para manutenção nos pesos
# resultado = 0 Sistemas de Informação
# resultado = 1 Engenharia Civil
def verifica_resultado(valores, iteracao, neuronios, entrada):
    resultado = int(np.sum(valores))
    if resultado >= 1:
        resultado = 1

    # validação do resultado obtido conforme a iteracao em questão
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


def teste_universo(neuronios):
    restante_universo = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 1, 1],
    ]
    print('Teste com restante do universo')
    for i in range(0, 4):
        valores = np.empty(3)
        print('valores de entrada: ', restante_universo[i][0], ' ', restante_universo[i][1], ' ',
              restante_universo[i][2])
        for j in range(0, 3):
            valores[j] = neuronios[j] * restante_universo[i][j]
        resultado = int(np.sum(valores))
        if resultado >= 1:
            resultado = 1
        print('resultado: ', resultado)
    print('\n')


# entram os neuronios treinados e realizam seu trabalho
def trabalho_neuronios(neuronios):
    continuar = "sim"
    primeira = 1
    while continuar.lower() == "sim":
        if primeira != 1:
            print('\n')
        print('Responda as perguntas com sim ou não \n'
              'Para descobrir se é um estudante de Sistemas de Informação ou Engenharia Civil')
        pergunta = input('1-Teve aulas de programação ? ')
        entrada1 = 1 if pergunta.lower() == "sim" else 0
        pergunta = input('2-Teve aula de estatística ? ')
        entrada2 = 1 if pergunta.lower() == "sim" else 0
        pergunta = input('3-Teve aula sobre dimensionamento de barragens ? ')
        entrada3 = 1 if pergunta.lower() == "sim" else 0
        entrada = [entrada1, entrada2, entrada3]
        print('Entrada para os neuronios:', entrada)
        valores = np.empty(3)
        for i in range(0, 3):
            valores[i] = neuronios[i] * entrada[i]
        resultado = int(np.sum(valores))
        if resultado >= 1:
            resultado = 1
        resposta = 'Estudante de Sistemas de Informação' if resultado == 0 else 'Estudante de Engenharia Civil'
        print("Você é:", resposta)
        continuar = input('continuar ? ')
        primeira += 1


def treina_devolve_neuronios():
    return perceptron_treino(randint(0, 1), randint(0, 1), randint(0, 1))


if __name__ == '__main__':
    neuronios_treinados = perceptron_treino(randint(0, 1), randint(0, 1), randint(0, 1))
    print("Necessário(s) " + str(ciclos) + " ciclo(s) para completar o aprendizado\n")
    teste_universo(neuronios_treinados)
    trabalho_neuronios(neuronios_treinados)
