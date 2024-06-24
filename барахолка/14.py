import networkx as nx
import matplotlib.pyplot as plt

# Создание графа с шестью вершинами
G_example_8 = nx.DiGraph()
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1, 3), (3, 5)]
G_example_8.add_edges_from(edges)

# Проверка наличия эйлерова цикла
has_eulerian_cycle = nx.is_eulerian(G_example_8)

# Проверка наличия гамильтонова цикла
try:
    hamiltonian_cycle = nx.find_cycle(G_example_8, orientation='ignore')
except nx.NetworkXNoCycle:
    hamiltonian_cycle = None

# Рисование графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_example_8)
nx.draw(G_example_8, pos, with_labels=True, node_color='lightblue', edge_color='red', arrows=True)
plt.title('Граф с эйлеровым циклом, но без гамильтонова цикла')
plt.show()

has_eulerian_cycle, hamiltonian_cycle