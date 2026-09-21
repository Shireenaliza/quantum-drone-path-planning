from qiskit import Aer, execute
from qiskit.circuit.library import QAOAAnsatz
from qiskit_optimization.applications import Maxcut
import networkx as nx

def run_qaoa(graph_dict, use_ibm_hardware=False, ibm_token=None):
    # Construct networkx graph for QUBO translation
    G = nx.Graph()
    for u, neighbors in graph_dict.items():
        for v, w in neighbors:
            G.add_edge(u, v, weight=w)
            
    max_cut = Maxcut(nx.to_numpy_array(G))
    qubo = max_cut.to_quadratic_program()
    operator, offset = qubo.to_ising()
    
    qaoa = QAOAAnsatz(operator, reps=1)
    
    if use_ibm_hardware and ibm_token:
        from qiskit import IBMQ
        IBMQ.save_account(ibm_token, overwrite=True)
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        backend = provider.get_backend('ibmq_qasm_simulator')
    else:
        backend = Aer.get_backend('qasm_simulator')
        
    job = execute(qaoa, backend, shots=1000)
    result = job.result()
    counts = result.get_counts()
    return counts