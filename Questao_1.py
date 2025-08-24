import numpy as np
import matplotlib.pyplot as plt


# Criando os dados

x = np.arange(-1, 1.1, 0.1)
y = np.arange(-1, 1.1, 0.1)
X, Y = np.meshgrid(x, y)
X_flat = X.ravel()
Y_flat = Y.ravel()

# Função círculo
def circle(x, y):
    return np.sqrt(x**2 + y**2)

raio = 0.6
classe = np.where(circle(X_flat, Y_flat) > raio, 1, 0)  # 1 = vermelho, 0 = preto


# Visualizando os dados originais

plt.figure(figsize=(6,6))
plt.scatter(X_flat[classe==1], Y_flat[classe==1], color='red', label='Classe 1')
plt.scatter(X_flat[classe==0], Y_flat[classe==0], color='black', label='Classe 0')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Dados originais (não-linearmente separáveis)')
plt.legend()
plt.axis('equal')
plt.show()


# Projeção não-linear

Z = circle(X_flat, Y_flat)  # transforma os dados em 1D usando a distância ao centro


# Visualizando os dados projetados

plt.figure(figsize=(8,4))
plt.scatter(Z[classe==1], np.zeros_like(Z[classe==1]), color='red', label='Classe 1')
plt.scatter(Z[classe==0], np.zeros_like(Z[classe==0]), color='black', label='Classe 0')
plt.axvline(x=raio, color='blue', linestyle='--', label='Frente de separação linear')
plt.xlabel('z = sqrt(x^2 + y^2)')
plt.title('Dados projetados (linearmente separáveis)')
plt.legend()
plt.show()


### Explicação do código: Criação do grid: igual ao que tinha em R, de -1 a 1 para x e y. Função círculo: 𝑧=𝑥^2+𝑦^2 que mede a distância ao centro. Classe: pontos dentro do círculo são pretos (0), fora são vermelhos (1). Projeção não-linear: agora pode separar as classes apenas com uma linha vertical em z = 0.6, tornando o problema linearmente separável. Visualização: gráfico final mostra claramente a separação. ###
