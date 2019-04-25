import pylab
import numpy as np
from qiskit import LegacySimulators
from qiskit.tools.visualization import plot_histogram
from qiskit_aqua import QuantumInstance
from qiskit_aqua import run_algorithm
from qiskit_aqua.algorithms import Grover
from qiskit_aqua.components.oracles import SAT

with open('3sat3-5.cnf', 'r') as f:
    sat_cnf = f.read()
print(sat_cnf)

sat_oracle = SAT(sat_cnf)

grover = Grover(sat_oracle)

backend = LegacySimulators.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=100)
result = grover.run(quantum_instance)
print(result['result'])

plot_histogram(result['measurements'])

params = {
    'problem': {'name': 'search'},
    'algorithm': {
        'name': 'Grover'
    },
    'oracle': {
        'name': 'SAT',
        'cnf': sat_cnf
    },
    'backend': {
        'shots': 100
    }
}

result_dict = run_algorithm(params, backend=backend)
plot_histogram(result_dict['measurements'])