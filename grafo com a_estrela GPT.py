import networkx as nx
import heapq
import matplotlib.pyplot as plt


def astar(graph, start_node, goal_node, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start_node, None))
    came_from = {}
    cost_so_far = {}
    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while open_set:
        current_cost, current_node, parent = heapq.heappop(open_set)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start_node)
            return list(reversed(path))

        for neighbor, _ in graph[current_node].items():
            new_cost = cost_so_far[current_node] + graph[current_node][neighbor]['weight']
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(graph.nodes[neighbor]['coordinates'],
                                                graph.nodes[goal_node]['coordinates'])
                heapq.heappush(open_set, (priority, neighbor, current_node))
                came_from[neighbor] = current_node

    return None


# Função para visualizar o processo do algoritmo A*
def visualize_astar(graph, start_node, goal_node, path):
    pos = nx.spring_layout(graph)

    nx.draw(graph, pos=pos, with_labels=True, node_color='blue', node_size=3000, font_color='white', font_size=20,
            font_weight='bold', width=3)

    nx.draw_networkx_labels(graph, pos=pos, labels={node: graph.nodes[node]['location'] for node in graph.nodes()},
                            font_color='black', font_size=15, font_weight='bold')

    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels={(u, v): graph[u][v]['weight'] for u, v in graph.edges()},
                                 label_pos=0.5)

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.margins(0.2)
    plt.show()


# Exemplo de uso
def heuristic(node, goal_node):
    # Heurística simples: distância Manhattan
    return abs(node[0] - goal_node[0]) + abs(node[1] - goal_node[1])


# Criando o grafo conforme o seu exemplo
G = nx.Graph()

G.add_node('A', location='CASA', coordinates=(0, 0))
G.add_node('B', location='RUA 02', coordinates=(2, 0))
G.add_node('C', location='RUA 05', coordinates=(4, 0))
G.add_node('D', location='RUA DOS LAGOS', coordinates=(6, 0))
G.add_node('E', location='RUA 35', coordinates=(6, 2))
G.add_node('F', location='AVENIDA DOS REIS', coordinates=(8, 2))
G.add_node('G', location='RUA 01', coordinates=(8, 0))
G.add_node('H', location='HOSPITAL', coordinates=(10, 0))

G.add_edge('A', 'B', weight=99)
G.add_edge('A', 'C', weight=82)
G.add_edge('A', 'F', weight=85)
G.add_edge('B', 'C', weight=98)
G.add_edge('B', 'D', weight=70)
G.add_edge('C', 'D', weight=128)
G.add_edge('D', 'E', weight=361)
G.add_edge('E', 'F', weight=82)
G.add_edge('E', 'G', weight=75)
G.add_edge('F', 'G', weight=90)
G.add_edge('H', 'E', weight=489)
G.add_edge('F', 'H', weight=147)

start_node = 'A'
goal_node = 'H'
path = astar(G, start_node, goal_node, heuristic)

# Visualizar o processo
visualize_astar(G, start_node, goal_node, path)
