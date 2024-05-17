from platform import node

import matplotlib.pyplot as plt
import networkx as nx

#O matplotlib.pyplot é um modulo da biblioteca do matplolib, que usamos para criação
# de de graficos e vizualizações de dados. Quando botamos o termo 'as plt' estamos apelidado o matplotlib.pyplot de plt.
#O networkx é um biblioteca que usamos para criar, manipular e estudar ad funções de grafos.

G = nx.Graph()

G.add_node('A', location='CASA')
G.add_node('B', location='RUA 02')
G.add_node('C', location='RUA 05')
G.add_node('D', location='RUA DOS LAGOS')
G.add_node('E', location='RUA 35')
G.add_node('F', location='AVENIDA DOS REIS')
G.add_node('G', location='RUA 01')
G.add_node('H', location='HOSPITAL')

#G.add_node, se refere a cada nó, esse comando adiciona o nó no grafico, location armazena os nomes de cada nó.

G.add_edge('A','B', weight= 99)
G.add_edge('A','C', weight= 82)
G.add_edge('A','F', weight= 85)
G.add_edge('B','C', weight= 98)
G.add_edge('B','D', weight= 70)
G.add_edge('C','D', weight= 128)
G.add_edge('D','E', weight= 361)
G.add_edge('E','F', weight= 82)
G.add_edge('E','G', weight= 75)
G.add_edge('F','G', weight= 90)
G.add_edge('H','E', weight= 489)
G.add_edge('F','H', weight= 147)

#G.add_edge, se refere as linhas que conecta cada nó, o weight armazena a distancia entre cada nó.

pos={
    'A':(-0.9,7),
    'B':(2.4,5),
    'C':(1.5,1.5),
    'D':(5.4,1.8),
    'E':(4.4,5),
    'F':(5.9,8),
    'G':(10,5),
    'H':(11,1)
}

#pos, se refere a posição dos nós, cada nó se posiciona nos eixos x,y

pos_node_attributes={
    'A':(-1.9,7),
    'B':(2.4,6),
    'C':(1.5,0.6),
    'D':(5.4,0.8),
    'E':(3.9,5.9),
    'F':(5.9,9.1),
    'G':(10,6.1),
    'H':(11,0.2)
}

#pos_node_attributes, se refere as posição das informações que atribuimos para os nós.

node_labels={n:(d['location']) for n,d in G.nodes(data=True)}

#node_labels, é usado para nomear os nós de um grafo, usando as informações que estão armazenada dentro de location.

edge_labels={(u,v):d['weight'] for u,v,d in G.edges(data=True)}

#edge_labels, é usando para rotular cada aresta/linha do grafo usando as informações armazenada em weigth.

nx.draw(G,pos=pos, with_labels=True, node_color='blue', node_size=3000, font_color='White', font_size=20, font_weight='bold', width=3)
nx.draw_networkx_labels(G, pos=pos_node_attributes, labels=node_labels, font_color='black', font_size=15, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
plt.margins(0.2)
plt.show()

#O termo nx.draw, ele permite que criarmos um representação grafica de um grafo.
#O termo with_labels=true, instrui que quando plotamos o grafo ele seja rotulado.
#O termo nx.draw_networkx_labels, é usado para desenhar as atribuições/rotulos em cada nó.
#O termo nx.draw_networkx_edge_labels, tem a mesma função do comando anterios, porém para desenhar as atribuições nas arestas/linhas.
