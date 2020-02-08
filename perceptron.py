import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_input = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

training_output = np.array([[0,1,1,0]]).T 

np.random.seed()

synaptic_weights = 2 * np.random.rand((3,1)) - 1

print(" Random init weights:")
print(synaptic_weights)

# Back Propogation Method
for i in range(5000):
    input_layer = training_input
    output = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_output - output
    adjustments = np.dot(input_layer.T, error * (output * (1 - output)))

    synaptic_weights += adjustments

print(" Weights after learning:")
print(synaptic_weights)

print(" Result after learning:")
print(output)