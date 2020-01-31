#!/usr/bin/env python
# coding: utf-8

# # KNN 

# **k-NN** é uma algoritmo que pertence a classe de aprendizado baseado em instância. O k-NN é usado para o reconhecimento de padrões, buscando os vizinhos mais próximos dado uma distância, visto que usa a hipotese que dados similares tendem a estar na mesma região. **É um problema de otimização que busca encontrar pontos em uma determinada vizinhancia** </p> 
# <p> A Classe : 
# Instace based learning é a classe que compara as novas instâncias com de um problema com as instâncias vistas no treinamento. Ou seja, ao invés de usar de generalização ele controí hipotese diretamente com as instâncias de treinamento.</p> 
# <p> A Vantagem: 
# Capacidade de se adaptar o modelos a dados que não foram vistos antes. </p>

# Para entender melhor o funcionamento do algoritmo vamos relembrar de alguns conceitos matemático, sendo esse conceitos a *distância euclidiana*, *a distância city-block, ou Manhattan* e a *distância de Minkowski*. Vale lembrar que as distâncias podem ser entendidas como medidas de similaridade, defini o grau de semelhança entre as instâncias e agrupa de acordo com a coesão, e desimilaridade, é a diferença entre as instâncias. Sendo p=(p1, p2, ..., pn) e q=(q1, q2, ..., qn):

# - Distância euclidiana: Distância entre dois pontos num espaço Euclidiano. É definida como a soma da raiz quadrada da diferença entre duas coordenadas, em suas dimensões.

# ![image.png](attachment:image.png)

# - Distância Manhattan: Distancia entre dois pontos no espaço cartesiano. É definida como sendo a soma da diferença entre as coordenadas em cada dimensão. 

# ![image.png](attachment:image.png)

# - Distância de Minkowski: É uma métrica do espaço vetorial. Pode ser visto como sendo uma generalização das duas distâncias anteriores.

# ![image.png](attachment:image.png)

# Na literatura, existem duas regras de classificação, *maioria da votação* e *peso pela distância*, sendo a primeira todos com a mesma influêcia e a classe escolhida é aquela que possui mais representante na vizinhança e a segunda cada vizinho tem um peso inversamente proporcional a distância. 

# Para executar o algoritmo, precisa-se de um conjunto de treinamento, definição de uma métrica, usada pra calcular a distância entre os exemplos e definir um valor da quantidade de vizinho:

# Sendo assim, para executar o algoritmo temos que:
# 1.	Fixar o ponto que será analisado, esse ponto é chamado de centroide.
# 2.	Calcular a distância.
# 3.	Encontrar os k-vizinhos mais próximos.
# 4.	Predizer o rótulo do ponto analisado (centroide). 

# A imagem abaixo, representa como o algoritmo funciona

# ![image.png](attachment:image.png)
