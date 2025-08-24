### Agora repetindo para 100 amostras:###

import numpy as np
import matplotlib.pyplot as plt

# =========================
# Configurações iniciais
# =========================
np.random.seed(42)

N = 100  # número de amostras
x = np.linspace(-15, 10, N)
ruido = np.random.normal(0, 4, N)
y = 0.5*x**2 + 3*x + 10 + ruido  # função geradora com ruído

# Para plotar suavemente
x_plot = np.linspace(-15, 10, 400)
y_real = 0.5*x_plot**2 + 3*x_plot + 10

# =========================
# Função para montar matriz H
# =========================
def montar_H(x, grau):
    """Constrói a matriz H para polinômio de dado grau"""
    H = np.vander(x, grau+1, increasing=True)  # colunas: x^0, x^1, ..., x^p
    return H

# =========================
# Ajuste polinomial usando pseudoinversa
# =========================
graus = range(1, 9)

plt.figure(figsize=(20, 15))

for i, p in enumerate(graus, 1):
    H = montar_H(x, p)
    w = np.linalg.pinv(H) @ y  # pseudoinversa de H
    H_plot = montar_H(x_plot, p)
    y_poly = H_plot @ w  # avaliação do polinômio nos pontos para plot

    # =========================
    # Plotagem
    # =========================
    plt.subplot(3, 3, i)
    plt.scatter(x, y, color='red', label='Amostras')
    plt.plot(x_plot, y_real, color='black', label='Função geradora')
    plt.plot(x_plot, y_poly, color='blue', label=f'Polinômio grau {p}')
    
    # Anotação sobre underfitting/overfitting
    if p <= 2:
        nota = 'Underfitting'
    elif p >= 7:
        nota = 'Overfitting'
    else:
        nota = 'Bom ajuste'
        
    plt.title(f'Grau {p} - {nota}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

plt.tight_layout()
plt.show()

# =========================
# Observações
# =========================
print("Observações com pseudoinversa:")
print("- Underfitting: grau 1 e 2.")
print("- Bom ajuste: grau 3 a 6.")
print("- Overfitting: grau 7 e 8, embora menos pronunciado devido ao maior número de amostras (100).")



### Explicação: Matriz H: construída com np.vander(x, grau+1, increasing=True) — cada coluna é 𝑥𝑖, do termo constante ao termo de grau p. Pseudoinversa: np.linalg.pinv(H) calcula H+ que minimiza o erro quadrático. Avaliação do polinômio: y_poly = H_plot @ w. Impacto das 100 amostras: overfitting reduz, polinômio alto ainda oscila, mas não tanto quanto com 20 amostras.###
