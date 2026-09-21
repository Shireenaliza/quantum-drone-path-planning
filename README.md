# Shortest Path for Autonomous Navigation: Quantum Hybrid (QAOA) vs. Classical Approaches

**Author**: Shireen Aliza Ali

---

## Overview
This repository presents a comparative study evaluating classical pathfinding algorithms against a Quantum Approximate Optimization Algorithm (QAOA) hybrid approach for autonomous drone path planning in simulated 3D environments.

---

## Benchmark Results

### Local Execution vs. IBM Quantum Cloud Execution

| Algorithm | Execution Time (Local) | Execution Time (IBM Hardware) | Optimal Path | Total Path Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Dijkstra** | 0.0010s | 0.0021s | `[0, 2, 3]` | **4.5000** |
| **A\*** | 0.0000s | 0.0010s | `[0, 2, 3]` | **4.5000** |
| **Bellman-Ford** | 0.0010s | 0.0000s | `[0, 2, 3]` | **4.5000** |
| **BFS** | 0.0000s | 0.0000s | `[0, 1, 3]` | 5.4000 (Suboptimal) |
| **DFS** | 0.0000s | 0.0000s | `[0, 1, 3]` | 5.4000 (Suboptimal) |
| **QAOA** | 20.8786s | 4.2450s | `[0, 2, 3]` | **4.5000** |

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/quantum-drone-path-planning.git](https://github.com/YOUR_USERNAME/quantum-drone-path-planning.git)
   cd quantum-drone-path-planning