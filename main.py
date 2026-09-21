import time
from src.algorithms import dijkstra, a_star, bellman_ford, bfs, dfs
from src.quantum_qaoa import run_qaoa
from utils.visualization import plot_3d_path

# Graph definition (Adjacency List: Node -> List of (Neighbor, Weight))
GRAPH = {
    0: [(1, 2.0), (2, 3.0)],
    1: [(0, 2.0), (2, 1.0), (3, 4.0)],
    2: [(0, 3.0), (1, 1.0), (3, 1.5)],
    3: [(1, 4.0), (2, 1.5), (4, 2.0)],
    4: [(3, 2.0)]
}

# 3D Coordinates for visual representation
NODE_COORDS = {
    0: (0.0, 0.0, 0.0),
    1: (1.0, 1.0, 2.0),
    2: (1.5, 0.5, 1.0),
    3: (3.0, 2.0, 2.5),
    4: (1.0, 2.0, 3.0)
}

def main():
    start_node = 0
    goal_node = 3

    print("--- Executing Classical Pathfinding ---")
    
    t0 = time.time()
    dijkstra_res = dijkstra(GRAPH, start_node)
    t_dijkstra = time.time() - t0
    print(f"Dijkstra Cost to {goal_node}: {dijkstra_res[goal_node]} (Time: {t_dijkstra:.6f}s)")

    t0 = time.time()
    astar_res = a_star(GRAPH, start_node, goal_node)
    t_astar = time.time() - t0
    print(f"A* Cost to {goal_node}: {astar_res[goal_node]} (Time: {t_astar:.6f}s)")

    t0 = time.time()
    bf_res = bellman_ford(GRAPH, start_node)
    t_bf = time.time() - t0
    print(f"Bellman-Ford Cost to {goal_node}: {bf_res[goal_node]} (Time: {t_bf:.6f}s)")

    bfs_path = bfs(GRAPH, start_node, goal_node)
    dfs_path = dfs(GRAPH, start_node, goal_node)
    print(f"BFS Path: {bfs_path}")
    print(f"DFS Path: {dfs_path}")

    print("\n--- Executing Quantum Approach (QAOA) ---")
    t0 = time.time()
    qaoa_counts = run_qaoa(GRAPH, use_ibm_hardware=False)
    t_qaoa = time.time() - t0
    print(f"QAOA Simulator Execution Time: {t_qaoa:.4f}s")

    # Plot sample trajectory
    plot_3d_path(NODE_COORDS, [0, 2, 3], title="Optimal Path [0 -> 2 -> 3]")

if __name__ == "__main__":
    main()