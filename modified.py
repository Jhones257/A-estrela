import pygame
import math
from queue import PriorityQueue
import time

LARGURA = 500
JANELA = pygame.display.set_mode((LARGURA, LARGURA))
pygame.display.set_caption("Path Finding - Algoritmo de busca A*")

VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 255, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165 ,0)
CINZA = (128, 128, 128)
TURQUESA = (64, 224, 208)

class Grafos:
    def __init__(self, linha, coluna, LARGURA, total_linhas):
        self.linha = linha
        self.coluna = coluna
        self.x = linha * LARGURA
        self.y = coluna * LARGURA
        self.color = BRANCO
        self.vizinhos = []
        self.LARGURA = LARGURA
        self.total_linhas = total_linhas

    def get_pos(self):
        return self.linha, self.coluna

    def is_closed(self):
        return self.color == VERMELHO

    def is_open(self):
        return self.color == VERDE

    def is_barrier(self):
        return self.color == PRETO

    def is_start(self):
        return self.color == LARANJA

    def is_end(self):
        return self.color == TURQUESA

    def reset(self):
        self.color = BRANCO

    def make_start(self):
        self.color = LARANJA

    def make_closed(self):
        self.color = VERMELHO

    def make_open(self):
        self.color = VERDE

    def make_barrier(self):
        self.color = PRETO

    def make_end(self):
        self.color = TURQUESA

    def make_path(self):
        self.color = ROXO

    def draw(self, janela):
        pygame.draw.rect(janela, self.color, (self.x, self.y, self.LARGURA, self.LARGURA))

    def atualizar_vizinhos(self, grid):
        self.vizinhos = []
        if self.linha < self.total_linhas - 1 and not grid[self.linha + 1][self.coluna].is_barrier():
            self.vizinhos.append(grid[self.linha + 1][self.coluna])

        if self.linha > 0 and not grid[self.linha - 1][self.coluna].is_barrier(): 
            self.vizinhos.append(grid[self.linha - 1][self.coluna])

        if self.coluna < self.total_linhas - 1 and not grid[self.linha][self.coluna + 1].is_barrier(): # RIGHT
            self.vizinhos.append(grid[self.linha][self.coluna + 1])

        if self.coluna > 0 and not grid[self.linha][self.coluna - 1].is_barrier(): # LEFT
            self.vizinhos.append(grid[self.linha][self.coluna - 1])

    def __lt__(self, other):
        return False

# Função utilizada para calcular a distância Manhattan entre dois pontos
def h_manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Função utilizada para calcular a distância euclidiana entre dois pontos
def h_euclidiana(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def caminho_reconstruido(veio_de, atual, draw):
    while atual in veio_de:
        atual = veio_de[atual]
        atual.make_path()
        draw()

def algorithm(draw, grid, start, end, heuristic):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for linha in grid for spot in linha}
    g_score[start] = 0
    f_score = {spot: float("inf") for linha in grid for spot in linha}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    start_time = time.time() # Inicia a contagem do tempo
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        atual = open_set.get()[2]
        open_set_hash.remove(atual)

        if atual == end:
            end_time = time.time() # Finaliza a contagem do tempo
            print("Tempo necessario:", round(end_time - start_time, 2), "segundos")
            caminho_reconstruido(came_from, end, draw)
            end.make_end()
            return True

        for vizinho in atual.vizinhos:
            temp_g_score = g_score[atual] + 1

            if temp_g_score < g_score[vizinho]:
                came_from[vizinho] = atual
                g_score[vizinho] = temp_g_score
                f_score[vizinho] = temp_g_score + heuristic(vizinho.get_pos(), end.get_pos())
                if vizinho not in open_set_hash:
                    count += 1
                    open_set.put((f_score[vizinho], count, vizinho))
                    open_set_hash.add(vizinho)
                    vizinho.make_open()

        draw()

        if atual != start:
            atual.make_closed()

    return False

def make_grid(linhas, LARGURA):
    grid = []
    gap = LARGURA // linhas
    for i in range(linhas):
        grid.append([])
        for j in range(linhas):
            spot = Grafos(i, j, gap, linhas)
            grid[i].append(spot)

    return grid

def draw_grid(janela, linhas, LARGURA):
    gap = LARGURA // linhas
    for i in range(linhas):
        pygame.draw.line(janela, CINZA, (0, i * gap), (LARGURA, i * gap))
        for j in range(linhas):
            pygame.draw.line(janela, CINZA, (j * gap, 0), (j * gap, LARGURA))

def draw(janela, grid, linhas, LARGURA):
    janela.fill(BRANCO)

    for linha in grid:
        for spot in linha:
            spot.draw(janela)

    draw_grid(janela, linhas, LARGURA)
    pygame.display.update()

def get_clicked_pos(pos, linhas, LARGURA):
    gap = LARGURA // linhas
    y, x = pos

    linha = y // gap
    coluna = x // gap

    return linha, coluna

def main(janela, LARGURA):
    ROWS = 30
    grid = make_grid(ROWS, LARGURA)

    start = None
    end = None

    heuristic_choice = None

    run = True
    while run:
        draw(janela, grid, ROWS, LARGURA)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                linha, coluna = get_clicked_pos(pos, ROWS, LARGURA)
                spot = grid[linha][coluna]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                linha, coluna = get_clicked_pos(pos, ROWS, LARGURA)
                spot = grid[linha][coluna]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end and heuristic_choice:
                    for linha in grid:
                        for spot in linha:
                            spot.atualizar_vizinhos(grid)

                    if heuristic_choice == "manhattan":
                        heuristic_func = h_manhattan
                    elif heuristic_choice == "euclidean":
                        heuristic_func = h_euclidiana

                    algorithm(lambda: draw(janela, grid, ROWS, LARGURA), grid, start, end, heuristic_func)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, LARGURA)

                if event.key == pygame.K_m:
                    heuristic_choice = "manhattan"

                if event.key == pygame.K_e:
                    heuristic_choice = "euclidean"

    pygame.quit()

main(JANELA, LARGURA)
