import numpy as np
import matplotlib.pyplot as plt
import random
import os

# ==============================
#   FUNCIÓN OBJETIVO
# ==============================
def f(x):
    return x**2 - 3*x + 4

# ==============================
#   HILL CLIMBING
# ==============================
def hill_climbing(a, b, n_iter=200, step_size=0.5):
    x = random.uniform(a, b)
    best_x = x
    best_y = f(x)
    history_x, history_y = [x], [best_y]
    
    for _ in range(n_iter):
        x_new = x + random.uniform(-step_size, step_size)
        x_new = max(a, min(b, x_new))
        y_new = f(x_new)
        if y_new > best_y:
            x, best_x, best_y = x_new, x_new, y_new
        history_x.append(x)
        history_y.append(f(x))
    
    return best_x, best_y, history_x, history_y

# ==============================
#   GREEDY SEARCH
# ==============================
def greedy_search(a, b, n_samples=200):
    x_values = np.linspace(a, b, n_samples)
    y_values = f(x_values)
    best_idx = np.argmax(y_values)
    best_x = x_values[best_idx]
    best_y = y_values[best_idx]
    return best_x, best_y, x_values, y_values

# ==============================
#   ALGORITMO GENÉTICO
# ==============================
def genetic_algorithm(a, b, pop_size=20, n_generations=100, mutation_rate=0.05):
    # Población inicial
    population = np.random.uniform(a, b, pop_size)
    fitness_history = []

    for _ in range(n_generations):
        fitness = f(population)
        fitness_history.append(np.max(fitness))

        # Selección (torneo)
        parents = []
        for _ in range(pop_size):
            i, j = np.random.randint(0, pop_size, 2)
            parents.append(population[i] if fitness[i] > fitness[j] else population[j])
        parents = np.array(parents)

        # Cruce (promedio)
        offspring = []
        for _ in range(pop_size // 2):
            p1, p2 = random.sample(list(parents), 2)
            child1 = (p1 + p2) / 2
            child2 = (p1 + p2) / 2
            offspring += [child1, child2]
        offspring = np.array(offspring)

        # Mutación
        mutation_mask = np.random.rand(pop_size) < mutation_rate
        offspring[mutation_mask] += np.random.uniform(-1, 1, np.sum(mutation_mask))
        offspring = np.clip(offspring, a, b)

        population = offspring

    best_idx = np.argmax(f(population))
    best_x = population[best_idx]
    best_y = f(best_x)

    return best_x, best_y, fitness_history

# ==============================
#   PARÁMETROS 
# ==============================
a, b = -50, 50

# Ejecutar Hill Climbing
hc_x, hc_y, hc_hist_x, hc_hist_y = hill_climbing(a, b)

# Ejecutar Greedy Search
gr_x, gr_y, gr_hist_x, gr_hist_y = greedy_search(a, b)

# Ejecutar Algoritmos Genéticos con dos tasas de mutación
ga1_x, ga1_y, ga1_fit = genetic_algorithm(a, b, mutation_rate=0.02)
ga2_x, ga2_y, ga2_fit = genetic_algorithm(a, b, mutation_rate=0.15)

# ==============================
#   GRAFICAR RESULTADOS
# ==============================
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

# --- Figura 1: Comparación de métodos ---
plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label='f(x) = x² - 3x + 4', color='black')
plt.scatter(hc_hist_x, hc_hist_y, s=15, c='orange', label='Hill Climbing')
plt.scatter(gr_hist_x, gr_hist_y, s=10, c='blue', label='Greedy Search')
plt.scatter(hc_x, hc_y, c='red', s=80, marker='*', label='Máximo Hill')
plt.scatter(gr_x, gr_y, c='green', s=80, marker='*', label='Máximo Greedy')
plt.title('Comparación Maximización de f(x) = x² - 3x + 4 ')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# --- Tabla de resultados ---
tabla_datos = [
    ["Método", "x máximo", "f(x) máximo"],
    ["Hill Climbing", f"{hc_x:.2f}", f"{hc_y:.2f}"],
    ["Greedy Search", f"{gr_x:.2f}", f"{gr_y:.2f}"],
    ["Genético 0.02", f"{ga1_x:.2f}", f"{ga1_y:.2f}"],
    ["Genético 0.15", f"{ga2_x:.2f}", f"{ga2_y:.2f}"]
]
tabla = plt.table(cellText=tabla_datos,
                  cellLoc='center',
                  loc='lower right',
                  bbox=[0.70, 0.01, 0.30, 0.20]) #(x, y, width, height)
tabla.auto_set_font_size(False)
tabla.set_fontsize(7)
tabla.scale(1, 1)
tabla.set_zorder(10)
plt.savefig("Punto_1_comparacion_metodos.png", dpi=300)
plt.show()

# --- Figura 2: Convergencia del algoritmo genético ---
plt.figure(figsize=(8,5))
plt.plot(ga1_fit, label='Mutación 0.02')
plt.plot(ga2_fit, label='Mutación 0.15')
plt.title('Convergencia del fitness en el algoritmo genético')
plt.xlabel('Generaciones')
plt.ylabel('Máximo fitness alcanzado')
plt.legend()
plt.grid(True)
plt.savefig("Punto_1_convergencia_genetico.png", dpi=300)
plt.show()

# ==============================
#   RESULTADOS
# ==============================
print("===== Resultados =====")
print(f"Hill Climbing: x={hc_x:.4f}, f(x)={hc_y:.4f}")
print(f"Greedy Search: x={gr_x:.4f}, f(x)={gr_y:.4f}")
print(f"Genético (mut=0.02): x={ga1_x:.4f}, f(x)={ga1_y:.4f}")
print(f"Genético (mut=0.15): x={ga2_x:.4f}, f(x)={ga2_y:.4f}")


