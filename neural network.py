import numpy as np

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases for hidden and output layers randomly
        self.weights_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.rand(1, self.hidden_size)

        self.weights_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.random.rand(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def feedforward(self, input_data):
        # Hidden layer calculation
        hidden_layer_input = np.dot(input_data, self.weights_hidden) + self.bias_hidden
        hidden_layer_output = self.sigmoid(hidden_layer_input)

        # Output layer calculation
        output_layer_input = np.dot(hidden_layer_output, self.weights_output) + self.bias_output
        output = self.sigmoid(output_layer_input)

        return output

# Example usage:
if __name__ == "__main__":
    # Define network parameters
    input_size = 3
    hidden_size = 4
    output_size = 2

    # Create a FeedForwardNN object
    neural_network = FeedForwardNN(input_size, hidden_size, output_size)

    # Example input data (single sample)
    input_data = np.array([[0.1, 0.2, 0.3]])

    # Get the output from the neural network for the input data
    output = neural_network.feedforward(input_data)

    print("Output of the neural network:", output)
