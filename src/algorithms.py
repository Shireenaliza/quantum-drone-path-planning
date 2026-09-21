import heapq
from collections import deque

def dijkstra(graph, start):
    pq = [(0, start)]
    shortest_paths = {start: 0}
    visited = set()
    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            if neighbor not in shortest_paths or new_cost < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return shortest_paths

def heuristic(node, goal):
    # Euclidean distance or positional heuristic approximation
    return 0.0

def a_star(graph, start, goal):
    pq = [(0, start)]
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_node == goal:
            return g_score
        for neighbor, weight in graph.get(current_node, []):
            tentative_g = g_score[current_node] + weight
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, neighbor))
    return g_score

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor, _ in graph.get(node, []):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for neighbor, _ in graph.get(start, []):
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path + [neighbor])
            if result:
                return result
    return None