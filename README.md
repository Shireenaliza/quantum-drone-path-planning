# Shortest Path for Autonomous Navigation: Quantum Hybrid (QAOA) vs. Classical Approaches

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework: Qiskit](https://img.shields.io/badge/framework-Qiskit_0.45%2B-6133BD.svg)](https://qiskit.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An empirical comparative study evaluating Classical Pathfinding Algorithms against a Quantum Approximate Optimization Algorithm (QAOA) hybrid model for 3D autonomous drone navigation.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Benchmark Results](#benchmark-results)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running on IBM Quantum Hardware](#running-on-ibm-quantum-hardware)
- [Authors & Acknowledgments](#authors--acknowledgments)
- [License](#license)

---

## Overview

Efficient path planning is critical for real-time 3D autonomous drone navigation. Classical pathfinding algorithms often experience efficiency trade-offs or scaling constraints in dynamic, large-scale search spaces. This repository explores the application of quantum optimization techniques—specifically the **Quantum Approximate Optimization Algorithm (QAOA)**—to solve spatial trajectory optimization by converting path planning constraints into Quadratic Unconstrained Binary Optimization (QUBO) / Ising Hamiltonian representations.

---

## Key Features

- **Multi-Algorithm Benchmarking**: Implements and evaluates Dijkstra, A*, Bellman-Ford, BFS, DFS, and Quantum QAOA.
- **Quantum Optimization Pipeline**: Formulates spatial flight constraints into QUBO and Ising models utilizing IBM Qiskit.
- **Hardware vs. Emulation Performance Analysis**: Benchmarks local state-vector quantum simulators against cloud-hosted IBM Quantum hardware instances.
- **3D Spatial Trajectory Visualization**: Built-in 3D matplotlib plotting utilities for path visualization.

---

## Benchmark Results

Evaluated on 3D spatial node networks:

| Algorithm | Local Time (s) | IBM Quantum Hardware Time (s) | Trajectory Path | Total Path Cost |
| :--- | :---: | :---: | :---: | :---: |
| **A\*** | **0.0000** | 0.0010 | `[0, 2, 3]` | **4.50** |
| **Dijkstra** | 0.0010 | 0.0021 | `[0, 2, 3]` | **4.50** |
| **Bellman-Ford** | 0.0010 | **0.0000** | `[0, 2, 3]` | **4.50** |
| **BFS** | 0.0000 | 0.0000 | `[0, 1, 3]` | 5.40 *(Suboptimal)* |
| **DFS** | 0.0000 | 0.0000 | `[0, 1, 3]` | 5.40 *(Suboptimal)* |
| **QAOA (Hybrid)** | 20.8786 | **4.2450** | `[0, 2, 3]` | **4.50** |

> **Key Observation**: QAOA demonstrates significant acceleration when executed on dedicated physical quantum hardware compared to local state-vector classical emulation.

---

## Project Structure

```text
quantum-drone-path-planning/
├── data/
│   └── results.csv            # Benchmarking metrics log
├── src/
│   ├── __init__.py
│   ├── algorithms.py          # Classical pathfinding implementations
│   └── quantum_qaoa.py        # QAOA circuit generation & Ising translation
├── utils/
│   ├── __init__.py
│   └── visualization.py       # 3D spatial plotting tools
├── .gitignore
├── main.py                    # Application entry point
├── README.md                  # Project documentation
└── requirements.txt           # Project dependencies
```

---

## Quick Start

### Prerequisites

- Python 3.9 or higher
- An active [IBM Quantum Experience Account](https://quantum.ibm.com/) *(optional, required only for physical hardware backend execution)*

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/quantum-drone-path-planning.git
   cd quantum-drone-path-planning
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Usage

Run the local comparison suite across all classical and simulated quantum algorithms:

```bash
python main.py
```

### Running on IBM Quantum Hardware

To route QAOA execution to physical IBM Quantum hardware backends:

1. Retrieve your IBM Quantum API token from your IBM Quantum dashboard.
2. Export your API token to your shell environment:

```bash
export IBMQ_TOKEN="your_ibm_quantum_api_token"
python main.py --use-quantum-hardware
```

---

## Authors & Acknowledgments

- **Shireen Aliza Ali** 
- **Tharun Gurunath** 
- **RS Vignesh** 

Developed as part of coursework at Vellore Institute of Technology (VIT).

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.