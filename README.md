# 🔎Algoritmo de busca A*(A-estrela)

Trabalho desenvolvido para disciplina de Inteligência Artificial

Alunos: [Jhones Soares](https://github.com/Jhones257), [Jorge Castro](https://github.com/guizyyn)

# 👩‍💻Algoritmos de busca em profundidade
 Podemos classificar os algoritmos de busca em profundidade como algoritmos utilizados para explorar ou procurar vértices em grafos. São amplamente usador em computação devido à sua simplicidade e eficácia em várias aplicações, como: resolução de quebra-cabeças e detecção de ciclos em grafos.

# Algoritmo A*
O algoritmo de busca A* é um dos algoritmos mais conhecidos e amplamente utilizados para encontrar o caminho mais curto em grafos. É um algoritmo de busca informada, o que significa que ele utiliza informações heurísticas para guiar a busca de forma mais eficiente. A* é particularmente eficaz pois combina as vantagens da busca de menor custo uniforme e da busca heurística.

Podemos definir sua função de custo como:
  - Função geral: f(n) = g(n) + h(n)
    - g(n): é o custo do caminho desde o nó inicial até o nó n.
    - h(n): é uma estimativa heurística do custo do caminho mais curto até n até o nó objetivo.

# Relação entre algoritmos DFS e A*
  
- 👨‍🏫 O **DFS(Depth-First Search)** É um algoritmo de busca não informada, que explora o grafo de forma exaustiva, sem considerar o custo ou a distância dos vértices. O DFS é usado principalmente para explorar todos os nós ou encontrar qualquer caminho para o objetivo, não necessariamente o mais curto.
    - Podemos definir a complexidade de tempo e espaço dos DFS como O(V + E), onde V é o número de vértices e E é o número de arestas. A complexidade do espaço O(V), no pior caso devido à pilha de chamadas recursivas ou à pilha na implementação iterativa

- 👨‍🏫 O **A-estrela** É um algoritmo de busca informada (heurística), que procura o caminho mais curto ou de menor custo até o objetivo. O A* utiliza uma função de custo (geralmente a soma do custo do caminho até o nó atual e uma estimativa heurística do custo até o objetivo) para guiar a busca.
    - Já o algoritmo A* tem sua complexidade de tempo e espaço baseado na precisão da heurística usada. No pior caso, pode ser exponencial ao número de nós (ou seja, O(b^d), onde b é o fator de ramificação e d é a profundidade da solução), mas geralmente é mais eficiente que a busca exaustiva devido ao uso da heurística.

# 🖥Implementação do algoritmo A*

Este algoritmo funciona basicamente em 3 etapas:
  - 1 Definição da Estrutura do Grafo: Definimos como nosso grafo será representado, estabelecendo uma lista de vizinhos e custo das arestas que os conectam.
  - 2 Definição da função heurística: esta função estima o custo restante do nó atual até o objetivo. Para este algoritmo utilizamos as duas heurísticas mais comuns(Distância Euclidiana e Manhattan).
  - 3 Implementação da estrutura de dados do A*: Utilizamos os conceitos de "open sets" e "close sets" para definir a função de calculo da função de custo f(n) = g(n) + h(n).

# 👩‍💻Sobre o Projeto
Para este projeto buscamos explorar a utilização do algoritmo de busca em grafos e grades, sendo os grafos uma estrutura fixa utilizando a heurística da distância de manhattan e as grades implementamos as duas heurísticas mais comuns(Manhattan e Distância Euclidiana) para comparação de desempenho.

Suas principais funcionalidades incluem:
  - ✨Criar grades: O usuário pode criar sua própria grade para exemplificar o algoritmo de busca. 
  - ✨Vizualiação gráfica: O algoritmo demonstra todo o processo de expansão dos nós, demonstrando Open Sets, Closed sets e melhor caminho, além de pontos iniciais e finais estabelecidos pelo usuário.
  - ✨Dados da execução: Ao final da execução do algoritmo, ele retorna o total de grafos percorridos e o tempo de execução para encontrar o melhor caminho.

# 👾 Contribuição
  Gostou do projeto e encontrou algum bugzinho ou oportunidade de melhoria? Sinta-se livre para enviar sugestões que possam melhorar o código e compartilhar nossos conhecimento 🥰. 
  Segue o passo a passo abaixo que não tem erro:
  - Certifique-se que você tenha o [Python](https://www.python.org/downloads/) instalado na sua máquina.
  - Em sequida instale a biblioteca NetworkX e Pygame rodando o seguinte código no terminal:
    ```bash
      pip install networkx
      ```
    ```bash
      pip install pygame
      ```
  - Faça um Fork do Repositório.
  - Clone o repositório para o seu ambiente local.
    ```bash
      git clone https://github.com/Jhones257/A-estrela.git
      ```
  - Crie uma branch para trabalhar em sua nova contribuição.
    ```bash
      git checkout -b minha-contribuicao
      ```
  - Quando estiver tudo ok com suas mudanças, faça commit delas.
     ```bash
      git commit -m "Adicionando funcionalidade X"
      ```
  - Envie suas alterações para o repositório remoto.
    ```bash
      git push origin minha-contribuicao
      ```
  - Crie um pull Request
  - E prontinho, vou dar uma revisada na sua sugestão e adiciona-la ao projeto 😊

# Referências
 - RUSSEL, Stuart; NORVIG, Peter. Informed (Heuristic) Search Strategies: A* search: Minimizing the total estimated solution cost. In: RUSSEL, Stuart; NORVIG, Peter. Artificial Intelligence A Modern Approach. 3. ed. [S. l.: s. n.], 1995. cap. 3, p. 93-94. Disponível em: www.pearsonhighered.com. Acesso em: 16 maio 2024.
 - FERGUSON, Dave; LIKHACHEV, Maxim; STENTZ, Anthony. A Guide to Heuristic-based Path Planning. Workshop on Planning under Uncertainty for Autonomous Systems, [s. l.], 10 jun. 2005. Disponível em: http://icaps05.icaps-conference.org/. Acesso em: 17 maio 2024.
 - MARTELLI, Alberto. On the Complexity of Admissible Search Algorithms. ARTIFICIAL INTELLIGENCE , [S. l.], p. 1-13, 1 mar. 1976.
 - [A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A&t=3211s)
 - [A* Pathfinding para Iniciantes](http://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/trabalhos/t1/A%20%20%20Pathfinding%20para%20Iniciantes.pdf)
