import numpy as np

def dijkstra(graph, start):
    num_vertices = len(graph)
    # Растояния до каждой вершины
    distances = [float('inf')] * num_vertices

    # Посещенные вершины
    visited = [False] * num_vertices

    # Начальное растоние 0
    distances[start] = 0

    # Поиск индекса вершины с минимальным расстоянием среди непосещенных
    def min_distance_vertex():
        min_distance = float('inf')
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v
        return min_index

    # Кратчайший путь
    for _ in range(num_vertices):
        # минимальное расстояние
        min_index = min_distance_vertex()

        # Посещенная вершина
        visited[min_index] = True

        # Расстояния до смежных вершин
        for v in range(num_vertices):
            if not visited[v] and graph[min_index][v] != 0 and distances[min_index] + graph[min_index][v] < distances[v]:
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances

graph = [
    [0, 4, 0, 0, 0],
    [4, 0, 8, 0, 0],
    [0, 8, 0, 7, 0],
    [0, 0, 7, 0, 9],
    [0, 0, 0, 9, 0]
]

start_vertex = 0
distances = dijkstra(graph, start_vertex)
print("Кратчайшие расстояния от вершины", start_vertex, "до всех остальных вершин:")
for i, distance in enumerate(distances):
    print("До вершины", i, "расстояние =", distance)
