'''
First Neural Network.
'''
import numpy as np

class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # Set number of nodes in input, hidden and output layers.
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Initialize weights
        self.weights_input_to_hidden = np.random.normal(0.0, self.hidden_nodes**-0.5,
                                       (self.hidden_nodes, self.input_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.output_nodes**-0.5,
                                       (self.output_nodes, self.hidden_nodes))
        self.lr = learning_rate

        #### Set this to your implemented sigmoid function ####
        # Activation function is the sigmoid function
        self.activation_function = sigmoid

        self.hidden_inputs = None
        self.hidden_outputs = None
        self.final_inputs = None
        self.final_outputs = None
        self.output_errors = None
        self.hidden_errors = None
        self.output_grad = None
        self.hidden_grad = None

    def train(self, inputs_list, targets_list):
        ''' Train the neural network by updating weights via back propagation '''
        # Convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        #### Implement the forward pass here ####
        ### Forward pass ###
        # Hidden layer
        self.hidden_inputs = np.dot(inputs, self.weights_input_to_hidden)
        self.hidden_outputs = self.activation_function(self.hidden_inputs)

        # Output layer        self.activation_function = sigmoid

        self.hidden_inputs = None
        self.hidden_outputs = None
        self.final_inputs = None
        self.final_outputs = None
        self.output_errors = None
        self.hidden_errors = None
        self.output_grad = None
        self.hidden_grad = None

    def train(self, inputs_list, targets_list):
        ''' Train the neural network by updating weights via back propagation '''
        # Convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        #### Implement the forward pass here ####
        ### Forward pass ###
        # Hidden layer
        self.hidden_inputs = np.dot(inputs, self.weights_input_to_hidden)
        self.hidden_outputs = self.activation_function(self.hidden_inputs)

        # Output layer
        self.final_inputs = np.dot(self.hidden_outputs, self.weights_hidden_to_output)
        self.final_outputs = self.final_inputs

        #### Implement the backward pass here ####
        ### Backward pass ###

        # Output error
        # error = (target - output) * f'(W * x) = (output - target) * W
        self.output_errors = np.dot((targets - self.final_outputs), self.weights_hidden_to_output)
        self.output_grad = self.output_errors * self.hidden_outputs

        # Backpropagated error
        self.hidden_errors = self.output_errors * self.weights_input_to_hidden * \
            self.hidden_outputs * (1 - self.hidden_outputs)
        self.hidden_grad = self.hidden_errors * inputs

        # Update the weights
        self.weights_hidden_to_output += self.lr * self.output_grad
        self.weights_input_to_hidden += self.lr * self.hidden_grad

    def run(self, inputs_list):
        ''' Run a forward pass through the network '''
        inputs = np.array(inputs_list, ndmin=2).T

        #### Implement the forward pass here ####
        # Hidden layer
        self.hidden_inputs = np.dot(inputs, self.weights_input_to_hidden)
        self.hidden_outputs = self.activation_function(self.hidden_inputs)

        # Output layer
        self.final_inputs = np.dot(self.hidden_outputs, self.weights_hidden_to_output)
        self.final_outputs = self.final_inputs

        return self.final_outputs
        self.final_inputs = np.dot(self.hidden_outputs, self.weights_hidden_to_output)
        self.final_outputs = self.final_inputs

        #### Implement the backward pass here ####
        ### Backward pass ###

        # Output error
        # error = (target - output) * f'(W * x) = (output - target) * W
        self.output_errors = np.dot((targets - self.final_outputs), self.weights_hidden_to_output)
        self.output_grad = self.output_errors * self.hidden_outputs

        # Backpropagated error
        self.hidden_errors = self.output_errors * self.weights_input_to_hidden * \
            self.hidden_outputs * (1 - self.hidden_outputs)
        self.hidden_grad = self.hidden_errors * inputs

        # Update the weights
        self.weights_hidden_to_output += self.lr * self.output_grad
        self.weights_input_to_hidden += self.lr * self.hidden_grad

    def run(self, inputs_list):
        ''' Run a forward pass through the network '''
        inputs = np.array(inputs_list, ndmin=2).T

        #### Implement the forward pass here ####
        # Hidden layer
        self.hidden_inputs = np.dot(inputs, self.weights_input_to_hidden)
        self.hidden_outputs = self.activation_function(self.hidden_inputs)

        # Output layer
        self.final_inputs = np.dot(self.hidden_outputs, self.weights_hidden_to_output)
        self.final_outputs = self.final_inputs

        return self.final_outputs

def sigmoid(x):
    ''' Calculate the sigmoid function for some input '''
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    ''' Calculated the derviative of the sigmoid for some input '''
    return sigmoid(x) * (1 - sigmoid(x))

