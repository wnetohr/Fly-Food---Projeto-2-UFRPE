import itertools
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
#print(matriz)

#Funções:

#função para achar os pontos A,B,C,D e adicionar eles em uma lista
def achar_pontos(matriz,linha,coluna,lista={},ponto_r=(0,0)):
    for l in range(linha):
        for c in range(coluna):
            if matriz[(l,c)] != '0' and matriz[(l,c)] != 'R':
                lista[(l,c)] = matriz[(l,c)]
    return lista

#função para encontrar o ponto R
def achar_r(matriz,linha,coluna):
    for l in range(linha):
        for c in range(coluna):
            if matriz[(l,c)] == 'R':
                return l,c

#função para botar o ponto R no começo e no final
def caminhos(lista,r,path):
    path.append(r)
    for i in lista:    
        path.append(i)
    path.append(r)
    return path

# Para calcular o custo precisa pegar o ponto atual(x,y) e subtrair com o seguinte pegar os valores positivos e somar 
# o x com o y e adicionar na variável custos
def custos(tuplas,custo=0):
    for i in range(len(tuplas)-1):
        var = tuple(map(lambda x, y: x - y, tuplas[i], tuplas[i+1]))
        custo+= abs(var[0]) + abs(var[1])
    return custo

def main():
    inicio = time.time()
    lista_pontos = achar_pontos(matriz,linha,coluna)
    ponto_r =(achar_r(matriz,linha,coluna))
    dict_custo = {}
    pontos_permutados = itertools.permutations(lista_pontos)
    for i in pontos_permutados:
        path = caminhos(i,ponto_r,path=[])
        dict_custo[i] = custos(path)

    #usando uma função lambda para pegar o segundo elemento da tupla como chave para função min
    menor = min(dict_custo.items(), key=lambda x: x[1]) 
    caminho = menor[0]

    #Output
    
    for n in caminho:
        print(matriz[n],' ',end='')
    print()
    #print('{0} {1} {2} {3}'.format(matriz[caminho[0]],matriz[caminho[1]],matriz[caminho[2]],matriz[caminho[3]]))
    
    fim = time.time()
    print(fim - inicio)






if __name__ == "__main__":
    main()