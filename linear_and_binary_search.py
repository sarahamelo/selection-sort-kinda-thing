import matplotlib.pyplot as plt
import numpy as np

# Função de busca binária que retorna o número de passos
def binary_search_steps(deck, target):
    steps = 0
    left, right = 0, len(deck) - 1
    while left <= right:
        steps += 1  # Contagem de passos para cada comparação
        mid = (left + right) // 2
        if deck[mid] == target:
            return steps
        elif deck[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps  # Se não encontrar (não deve ocorrer nesta simulação)

# Função de busca linear que retorna o número de passos
def linear_search_steps(deck, target):
    steps = 0
    for num in deck:
        steps += 1
        if num == target:
            break
    return steps

# Função de ordenação (Selection Sort) para organizar o baralho
def selection_sort(deck):
    for i in range(len(deck)):
        min_idx = i
        for j in range(i + 1, len(deck)):
            if deck[j] < deck[min_idx]:
                min_idx = j
        if min_idx != i:
            deck[i], deck[min_idx] = deck[min_idx], deck[i]
    return deck

# Simulação de jogadas
deck = [64, 25, 12, 22, 11]

# Baralho organizado
sorted_deck = selection_sort(deck.copy())

# Baralho desorganizado
unsorted_deck = deck.copy()

# Números a serem encontrados
targets = [64, 25, 12, 22, 11]

# Contagem de passos para encontrar cada número em ambos os baralhos
steps_binary_sorted = [binary_search_steps(sorted_deck, target) for target in targets]
steps_linear_unsorted = [linear_search_steps(unsorted_deck, target) for target in targets]

# Gráfico de passos para encontrar cada número
fig, ax = plt.subplots(figsize=(12, 6))
x_labels = [str(target) for target in targets]
bar_width = 0.35
x = np.arange(len(targets))

ax.bar(x - bar_width/2, steps_binary_sorted, bar_width, label='Binária (Organizado)', color='skyblue')
ax.bar(x + bar_width/2, steps_linear_unsorted, bar_width, label='Linear (Desorganizado)', color='salmon')
ax.set_xlabel("Número")
ax.set_ylabel("Número de Passos")
ax.set_title("Número de Passos para Encontrar Cada Número (Binária vs Linear)")
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()

plt.show()
