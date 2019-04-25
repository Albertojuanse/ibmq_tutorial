from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import BasicAer
from qiskit import execute
from qiskit import IBMQ

# Solo es preciso la primera vez
IBMQ.save_account("3c999a701a95c71f427401a4fae986b7eae6a2366e45126fc15ad970849a0d98f0eff6d72b8edfdaf402101541b5076caef0c582d43b4bed78864a6121a400cc")
IBMQ.load_accounts()

quantum_register = QuantumRegister(1)
classical_register = ClassicalRegister(1)
circuit = QuantumCircuit(quantum_register, classical_register)

circuit.h(quantum_register[0])

circuit.measure(quantum_register, classical_register)

backend = BasicAer.get_backend('statevector_simulator')
job = execute(circuit, backend)
result = job.result()
outputstate = result.get_statevector(circuit, decimals=3)
print(outputstate)