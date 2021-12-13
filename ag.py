import random
import time

#abrindo arquivo e pegando as entradas
with open("entrada.txt", 'r') as arquivo:
    data = arquivo.readlines()
arquivo.close()

#tirando a quebra de linha \n de cada linha em data
for i in range(len(data)):
    data[i] = data[i].strip()

#construindo a matriz
linha, coluna = map(int, data[0].split())
matriz = {}
for l in range(linha):
    for c in range(coluna):
        matriz[(l,c)] = 0
for l in range(linha):
    lista_elementos = []
    lista_elementos = data[l+1].split()
    
    for n in range(len(lista_elementos)):
        c = int(n)
        matriz[(l,c)] = lista_elementos[c]

#Funções:

#pegando apenas os pontos
def achar_pontos(matriz,linha,coluna,lista=[]):
    for l in range(linha):
        for c in range(coluna):
            if matriz[(l,c)] != '0' and matriz[(l,c)] != 'R':
                lista.append((l,c))
            if matriz[(l,c)] == 'R':
                r = (l,c)
    return (lista,r)

#função de criar rotas aleatórias
def routes(pontos,route = []):
    temp_list = random.sample(pontos[0],len(pontos[0]))
    temp_list.insert(0,pontos[1])
    temp_list.append(pontos[1])
    return temp_list

#população inicial
def populacao_inicial(pontos):
    populacao = []
    for n in range(0,len(pontos[0])*10):
        populacao.append(routes(pontos)) 
    return populacao

#função de custos
def custos(tuplas,custo=0):
    for i in range(len(tuplas)-1):
        var = tuple(map(lambda x, y: x - y, tuplas[i], tuplas[i+1]))
        custo+= abs(var[0]) + abs(var[1])
    return custo

#rank de rotas
def rank_rotas(populacao):
    dict_rotas = []
    for n in range(0,len(populacao)):
        custo = custos(populacao[n])
        dict_rotas.append((custo,populacao[n]))
    return dict_rotas

#função de seleção
def selecao(rotas):
    new_pop = []
    new_pop.append(min(rotas))
    new_pop.append(random.choice(rotas))
    return new_pop

#função cruzamento
def cruzamento(pop_atual,pontos):
    r = pontos[1]
    lista_pontos = pontos[0]
    new_pop = []
    melhor_rota = min(pop_atual)
    new_pop.append(melhor_rota[1]) #seleciona o melhor da população anterior para a próxima
    tamanho = (len(lista_pontos))//2
    pai1 = pop_atual[0][1]
    pai2 = pop_atual[1][1]
    filho1 = []
    filho2 = []
    for m in range(0,tamanho+1):
        filho1.append(pai1[m])
        filho2.append(pai2[m])    

    #verificar cidades 
    for n in range(tamanho+1,len(pai1)):
        if pai2[n] == r:
            filho1.append(pai2[n]) 
        elif pai2[n] != r and pai2[n] not in filho1:
             filho1.append(pai2[n])
        else:
            for n in lista_pontos:
                if n not in filho1:
                    filho1.append(n)
    for n in range(tamanho+1,len(pai1)):
        if pai1[n] == r:
            filho2.append(pai1[n]) 
        elif pai1[n] != r and pai1[n] not in filho2:
             filho2.append(pai1[n])
        else:
            for n in lista_pontos:
                if n not in filho2:
                    filho2.append(n)
    #chance de um dos filhos sofrer mutação
    x = random.randint(1,11)
    if x == 7:
        filho1, filho2 = mutacao(filho1,filho2)

    new_pop.append(filho1)
    new_pop.append(filho2)
    return rank_rotas(new_pop)

#função de mutação, para cada filho novo existe uma chance sofrer uma troca entre o primeiro ponto de entrega e o último
def mutacao(filho1,filho2):

    x = random.randint(1,11)
    if x == 7:
        ponto1 = filho1[1]
        ponto2 = filho1[len(filho1)//2]
        filho1[1] = ponto2
        filho1[len(filho1)//2] = ponto1
            
    if x == 3:
        ponto1 = filho2[1]
        ponto2 = filho2[len(filho2)//2]
        filho2[1] = ponto2
        filho2[len(filho2)//2] = ponto1
    return filho1, filho2

def nova_pop(rotas,pontos):
    return cruzamento(selecao(rotas),pontos)

def main():
    inicio = time.time()
    pontos = achar_pontos(matriz,linha,coluna)
    pop_inicial = populacao_inicial(pontos)
    rotas_custo = rank_rotas(pop_inicial)
    count = 0
    new_pop = rotas_custo
    while count < 10:
        count+=1
        new_pop = nova_pop(new_pop,pontos)
    
    menor = min(new_pop)
    caminho = menor[1]
    caminho.pop(0)
    caminho.pop(len(caminho)-1)

    fim = time.time()
    print(fim-inicio)

    #Output
    
    for n in caminho:
        print(matriz[n],' ',end='')
    print()

if __name__ == "__main__":
    main()


    
    
