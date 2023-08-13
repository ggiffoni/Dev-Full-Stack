#Geração de 1000 pontos com média 20 e desvio padrão 2.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

dados = np.random.normal(loc=20, scale=2, size=1000)

plt.hist(dados, color = "lightblue", ec = "red")

