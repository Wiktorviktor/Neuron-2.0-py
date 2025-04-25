import Neuron: 

    def__init__(self, inputs): 

 # Inicialize the neuron with a list of inputs \ ініціалізуємо ваги випадковими значеннями

        self.weights = np.random.rand (inputs)
        self.bias = np.random.randn()


    def activate (self, x):
        # Activation function (ReLU) \ функція активації (ReLU)
        return 1/ (1 + np.exp(-x))
    def forward (self, inputs): # Forward pass \ прямий прохід \ обчислюємо зважені суми + зміщення (bias)
    
        total = np.dot(self.weights, inputs) + self.bias
        return self.activate(total) # Return the activated output \ повертаємо активоване значення