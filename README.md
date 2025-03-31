# Implementação do Algoritmo para Caminho Hamiltoniano

## Descrição do Projeto
Este projeto implementa um algoritmo para encontrar um Caminho Hamiltoniano em um grafo utilizando uma abordagem baseada em busca recursiva (backtracking). Um Caminho Hamiltoniano é um caminho que visita cada vértice exatamente uma vez. O problema é relevante em diversas aplicações, incluindo otimização de rotas e análise de redes.

## Como o Algoritmo Funciona
O algoritmo usa um método de tentativa e erro (backtracking) para explorar diferentes caminhos possíveis no grafo e determinar se existe uma sequência de vértices que forma um Caminho Hamiltoniano.

### Passo a Passo da Implementação
1. **Representação do grafo**: Utiliza-se uma lista de adjacência para armazenar as conexões entre os vértices.
2. **Função Recursiva**: A cada passo, o algoritmo tenta adicionar um novo vértice ao caminho.
3. **Critério de Parada**: Se todos os vértices forem incluídos no caminho, um Caminho Hamiltoniano foi encontrado.
4. **Retrocesso**: Caso não seja possível adicionar mais vértices sem repetir, o algoritmo desfaz a última escolha e tenta outro caminho.
5. **Inicialização**: O processo é testado para cada vértice como ponto de partida.

## Como Executar o Projeto
### Pré-requisitos
- Python 3 instalado.

### Passos para Execução
1. Clone este repositório:
   ```bash
   https://github.com/GustavoMBarbosa/Trabalho_individual_3_FPAA.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd hamiltonian-path
   ```
3. Execute o script:
   ```bash
   python main.py
   ```

## Relatório Técnico

### Classificação de Complexidade
O problema do Caminho Hamiltoniano pertence à classe **NP-completo**, pois não se conhece um algoritmo polinomial para resolvê-lo em tempo eficiente. A sua dificuldade está associada ao Problema do Caixeiro Viajante.

### Complexidade Assintótica
- O algoritmo testa diversas possibilidades utilizando backtracking, levando a um tempo de execução exponencial **O(n!)**, no pior caso.
- Melhor caso: Se um Caminho Hamiltoniano for encontrado rapidamente, o algoritmo pode terminar antes do pior cenário.
- Caso médio: Depende da estrutura do grafo, mas ainda tende a ser exponencial.
- Pior caso: Exploração de todas as combinações possíveis de caminhos antes de concluir que não existe um Caminho Hamiltoniano.

### Aplicação do Teorema Mestre
O Teorema Mestre não pode ser aplicado diretamente nesse problema, pois não segue a forma padrão **T(n) = aT(n/b) + f(n)**. O crescimento exponencial se dá pela necessidade de testar múltiplos caminhos em um espaço de busca combinatório.
