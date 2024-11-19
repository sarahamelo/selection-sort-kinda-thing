# Análise de Algoritmos de Busca com Selection Sort

## 1. Objetivo dos Códigos com Selection Sort

Este repositório tem como objetivo explorar e comparar a eficiência de diferentes tipos de busca em um baralho de cartas, utilizando o algoritmo de ordenação **Selection Sort**. Duas abordagens foram implementadas:
- **Código 1**: Realiza a busca linear em ambos os tipos de baralhos (organizado e desorganizado).
- **Código 2**: Realiza a busca binária em um baralho organizado e a busca linear em um baralho desorganizado.

Os códigos são usados para simular quantos passos são necessários para encontrar um número específico em cada tipo de baralho e para gerar gráficos que ajudam a visualizar as diferenças de desempenho entre as abordagens.

## 2. Análise Sintática dos Códigos

### Código 1: Busca Linear em Ambos os Baralhos

**Descrição**: Este código realiza uma busca linear tanto em um baralho organizado quanto em um desorganizado. A busca linear percorre a lista de forma sequencial, verificando cada elemento até encontrar o alvo.

**Funções Principais**:
- `selection_sort(deck)`: Ordena o baralho usando o algoritmo **Selection Sort**, com complexidade \( O(n^2) \).
- `linear_search_steps(deck, target)`: Realiza a busca linear no baralho e conta o número de passos necessários para encontrar o número desejado. A complexidade é \( O(n) \).

**Código**:
```python
def selection_sort(deck):
    for i in range(len(deck)):
        min_idx = i
        for j in range(i + 1, len(deck)):
            if deck[j] < deck[min_idx]:
                min_idx = j
        if min_idx != i:
            deck[i], deck[min_idx] = deck[min_idx], deck[i]
    return deck

def linear_search_steps(deck, target):
    steps = 0
    for num in deck:
        steps += 1
        if num == target:
            break
    return steps
```

**Funcionamento**:
1. O baralho é ordenado usando o **Selection Sort**.
2. A busca linear é aplicada tanto no baralho organizado quanto no desorganizado.
3. O número de passos necessários para encontrar cada número é contado e armazenado para análise.

### Código 2: Busca Binária no Baralho Organizado e Busca Linear no Baralho Desorganizado

**Descrição**: Este código utiliza a busca binária em um baralho organizado e a busca linear em um baralho desorganizado. A busca binária é mais eficiente em listas ordenadas, pois divide o espaço de busca pela metade a cada iteração. Porém, acaba sendo menos eficiente pelo deck de cartas ser menor.

**Funções Principais**:
- `binary_search_steps(deck, target)`: Realiza a busca binária no baralho ordenado e conta o número de passos necessários para encontrar o número. A complexidade é \( O(\log n) \).
- `linear_search_steps(deck, target)`: Mesma função do código 1, com complexidade \( O(n) \).

**Código**:
```python
def binary_search_steps(deck, target):
    steps = 0
    left, right = 0, len(deck) - 1
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if deck[mid] == target:
            return steps
        elif deck[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps

def linear_search_steps(deck, target):
    steps = 0
    for num in deck:
        steps += 1
        if num == target:
            break
    return steps
```

**Funcionamento**:
1. O baralho é ordenado usando o **Selection Sort**.
2. A busca binária é aplicada no baralho organizado e a busca linear no baralho desorganizado.
3. O número de passos é contado para análise comparativa.

## 3. Análise dos Gráficos

### Gráfico 1: Número de Passos para Encontrar Cada Número
![linear_search_graph](https://github.com/user-attachments/assets/032000ba-b8a8-4086-ac6b-4cb447a018a6)

Este gráfico compara a quantidade de passos necessários para encontrar cada número em ambos os baralhos:
- **Busca Linear em Ambos os Baralhos (Código 1)**:
  - A quantidade de passos depende da posição do número. Se o número estiver próximo do início, a busca é mais rápida. Se estiver no final, são necessários mais passos.

### Gráfico 2: Probabilidade de a Busca Binária Ser Mais Rápida
![linear_and_binary_search_graph](https://github.com/user-attachments/assets/9cd71dcf-f667-4d5f-8c7f-308348cf5d59)

- **Busca Binária vs. Busca Linear (Código 2)**:
  - A busca binária no baralho organizado geralmente requer menos passos, especialmente em listas maiores, enquanto a busca linear pode levar mais tempo em um baralho desorganizado.
    
- **Conclusão dos Gráficos**:
  - Como o número de cartas são poucas, o baralho desorganizado acaba tendo uma maior perfomance, pois a probabilidade de você encontrar um número alto no começo é maior que encontrá-lo em um baralho organizado. Claro, na vida real, acabamos por decorar o que nós mesmos embaralhamos, mas por código, tentando ser o mais realista possível, o desorganizado é mais eficiente.

## 4. Tempo de Execução e Notação Big O

### Complexidade dos Algoritmos
- **Busca Linear (ambos os códigos)**: Tem complexidade de tempo \( O(n) \). O tempo de execução cresce linearmente com o número de elementos na lista. É simples e direta, mas ineficiente para listas grandes.
- **Busca Binária (Código 2)**: Tem complexidade de tempo \( O(\log n) \). O tempo de execução cresce de forma logarítmica em relação ao número de elementos, tornando-a muito mais eficiente em listas grandes.
- **Selection Sort (em ambos os códigos)**: Tem complexidade de tempo \( O(n²) \). É uma etapa de pré-processamento para ordenar o baralho e permite o uso da busca binária no código 2.

### Análise do Tempo de Execução
- **Listas Pequenas**: A diferença de tempo entre busca linear e busca binária pode ser pequena. A busca linear pode até ter um desempenho similar ao da busca binária em listas pequenas.
- **Listas Grandes**: A busca binária se destaca por reduzir significativamente o número de comparações. Ela é muito mais eficiente do que a busca linear, que continua percorrendo a lista inteira no pior caso.

## O Papel do Selection Sort
O **Selection Sort** é um algoritmo de ordenação que organiza os elementos de uma lista em ordem crescente (ou decrescente). No contexto de um baralho de cartas, ele ordena as cartas de forma que a estrutura do baralho se torne adequada para a aplicação de buscas mais eficientes, como a **busca binária**.

### Por Que o Baralho Precisa Estar Ordenado?
A **busca binária** só pode ser aplicada em listas ordenadas. Isso ocorre porque a busca binária funciona dividindo repetidamente o intervalo de busca pela metade, comparando o elemento do meio com o valor alvo e descartando a metade em que o alvo não pode estar. Se o baralho não estiver ordenado, essa técnica não pode ser usada, pois não há uma estrutura definida para saber em qual metade o alvo pode estar.

### Importância do Selection Sort para a Busca Binária
- **Preparação para Busca Eficiente**: O **Selection Sort** organiza o baralho de forma que ele possa ser pesquisado usando a **busca binária**, que é significativamente mais rápida em termos de complexidade de tempo (\( O(\log n) \)) em comparação com a **busca linear** (\( O(n) \)). Isso faz com que a busca por cartas específicas no baralho ordenado seja muito mais eficiente.
- **Aplicação em Situações de Vida Real**: Em cenários onde há necessidade de buscar frequentemente por elementos em um conjunto de dados (como em jogos de cartas ou consultas em bases de dados), ter os dados ordenados é vantajoso. O **Selection Sort** é uma forma de pré-processar esses dados para que as futuras buscas possam ser feitas rapidamente.

### Desvantagens do Selection Sort
Embora o **Selection Sort** tenha sua importância, ele não é o algoritmo de ordenação mais eficiente. Sua complexidade de tempo é \( O(n^2) \), o que significa que ele não é ideal para ordenar listas muito grandes. No entanto, para listas pequenas ou em situações onde a simplicidade da implementação é suficiente, o **Selection Sort** pode ser uma escolha aceitável.

## 5. Conclusão Geral

### Insights Obtidos:
- **Busca Binária em Listas Ordenadas**: Mostra-se superior em termos de eficiência de tempo em listas grandes. Ela é ideal para cenários em que a lista pode ser pré-ordenada.
- **Busca Linear em Listas Desorganizadas**: Funciona bem em listas pequenas, mas seu desempenho cai em listas maiores devido ao crescimento linear da quantidade de passos.
- **Ordenação com Selection Sort**: Embora o **Selection Sort** tenha uma complexidade de \( O(n²) \), ele permite que a busca binária seja aplicada posteriormente, o que é vantajoso para listas que precisam ser pesquisadas frequentemente.

### Conclusão:
- Para listas grandes, é vantajoso ter um baralho ordenado e usar a busca binária devido à sua eficiência \( O(\log n) \).
- Em listas pequenas ou para buscas únicas em listas desorganizadas, a busca linear pode ser suficientemente rápida e mais simples de implementar.

Este repositório fornece uma visão detalhada sobre como diferentes tipos de busca se comportam em listas ordenadas e desorganizadas, destacando a importância da escolha de algoritmos com base no tamanho da lista e na frequência de pesquisa.
