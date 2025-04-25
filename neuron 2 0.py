import numpy as np  # Передбачаю, що використовується numpy, але імпорт його не вказано у вихідному коді.

class Neuron:
    def __init__(self, inputs):
        # Ініціалізуємо ваги випадковими значеннями
        self.weights = np.random.rand(inputs)
        self.bias = np.random.randn()

    def activate(self, x):
        # Функція активації (ReLU)
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        # Прямий прохід: обчислюємо зважені суми + зміщення (bias)
        total = np.dot(self.weights, inputs) + self.bias
        return self.activate(total)  # Повертаємо активоване значення
