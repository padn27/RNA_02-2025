### Q-3:###

import numpy as np
import matplotlib.pyplot as plt

# =========================
# Configurações iniciais
# =========================
np.random.seed(42)  # para resultados reproduzíveis

N = 20  # número de amostras
x = np.linspace(-15, 10, N)
ruido = np.random.normal(0, 4, N)  # ruído gaussiano (mean=0, sd=4)
y = 0.5*x**2 + 3*x + 10 + ruido  # função geradora com ruído

# Para plotar suavemente os polinômios e função real
x_plot = np.linspace(-15, 10, 200)
y_real = 0.5*x_plot**2 + 3*x_plot + 10

# =========================
# Ajuste polinomial
# =========================
graus = range(1, 9)  # polinômios do grau 1 ao 8

plt.figure(figsize=(20, 15))

for i, p in enumerate(graus, 1):
    # Ajuste polinomial
    coef = np.polyfit(x, y, p)  # encontra os coeficientes w
    y_poly = np.polyval(coef, x_plot)  # avalia o polinômio nos pontos para plot

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
    elif p >= 6:
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
print("Observações:")
print("- Underfitting ocorre para grau 1 e 2: polinômio não consegue capturar a curva quadrática.")
print("- Bom ajuste ocorre para grau 3 a 5: segue bem a tendência da função geradora.")
print("- Overfitting ocorre para grau 6 a 8: polinômio tenta passar exatamente por todos os pontos, capturando o ruído.")



### Análise de Overfitting e Underfitting ###

### Underfitting: ocorre quando o polinômio não consegue capturar a forma da função geradora (grau muito baixo, ex: p=1). ###

### Overfitting: ocorre quando o polinômio segue o ruído das amostras em vez de capturar a tendência real (grau muito alto, ex: p≥6 com 20 amostras). ###

### No caso:###

### p=1 ou p=2 → provavelmente underfitting (especialmente p=1) ###
### p=3 ou p=4 → bom ajuste (aproxima bem a função quadrática) ###
### p≥6 → overfitting (polinômio começa a oscilar para passar exatamente por cada ponto com ruído) ###

### O que esse código faz: Gera 20 amostras da função 𝑓𝑔(𝑥)=0.5𝑥^2+3𝑥+10 com ruído gaussiano, ajusta polinômios de grau 1 a 8 usando least squares (np.polyfit); Plota cada polinômio, a função real e os pontos amostrados. Marca no título se o polinômio está em underfitting, bom ajuste ou overfitting. Exibe observações sobre cada caso.### 

