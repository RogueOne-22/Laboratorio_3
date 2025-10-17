# 🧠 Maximización de la función *f(x) = x² - 3x + 4*

Este ejercicio implementa tres algoritmos heurísticos diferentes para **encontrar el máximo global** de la función dentro de un intervalo definido (-50,50), y compara sus resultados gráficamente.

---

## 📘 objetivo

La función \( f(x) = x^2 - 3x + 4 \) es una parábola convexa hacia arriba (mínimo en \(x = 1.5\)), en la cual buscamos el **máximo global** en un intervalo finito, por ejemplo \([-50, 50]\).

El código implementa y compara tres métodos:

1. **Hill Climbing:**  
   Explora el entorno del punto actual y acepta movimientos que mejoran la solución.
2. **Greedy Search:**  
   Evalúa varios candidatos por iteración y siempre elige el mejor.
3. **Algoritmo Genético (GA):**  
   Usa una población de soluciones, selección, cruce y con dos tasas de mutación distintas (0.05 y 0.2).  
   Además, muestra la **curva de convergencia del fitness** a lo largo de las generaciones.


El programa genera dos gráficos:

### 1. Comparación de métodos heurísticos
Muestra la función \(f(x)\) con los puntos explorados por cada algoritmo:
- 🔵 **Hill Climbing**
- 🟢 **Greedy Search**
- 🔴 **Algoritmo Genético**

[Punto_1_comparacion_metodos.png](https://github.com/RogueOne-22/Laboratorio_3/blob/19824c6ea6d83e5b6d96c2f70c8a974ba5beee73/Punto%201/Punto_1_comparacion_metodos.png)
- 
Archivo generado:  
`comparacion_algoritmos.png`

### 2. Convergencia del Algoritmo Genético
Gráfica que muestra cómo el **fitness promedio y máximo** cambian a lo largo de las generaciones.  
Permite comparar dos tasas de mutación:
- Mutación baja (0.05)
- Mutación alta (0.2)

[Punto_1_convergencia_genetico.png](https://github.com/RogueOne-22/Laboratorio_3/blob/19824c6ea6d83e5b6d96c2f70c8a974ba5beee73/Punto%201/Punto_1_convergencia_genetico.png)
-
Archivo generado:  
`convergencia_genetico.png`

---

## 📊 Parámetros principales
| Parámetro | Descripción | Valor |
|------------|--------------|--------|
| `a, b` | Intervalo de búsqueda | `[-50, 50]` |
| `n_iter` | Iteraciones Hill/Greedy | `200` |
| `n_generations` | Generaciones GA | `100` |
| `pop_size` | Tamaño de la población GA | `30` |
| `mutation_rate` | Tasa de mutación GA | `0.05` y `0.2` |
## 🧬 Implementación del Algoritmo Genético

El **Algoritmo Genético ** es una técnica inspirada en la evolución biológica que busca aproximar la mejor solución posible a un problema.  
---

### ⚙️ Etapas principales del Algoritmo

1. **Inicialización de la población**
   - Se generan aleatoriamente varios valores de \(x\) dentro del rango \([a, b]\).
   - Cada individuo representa una posible solución al problema.

   ```python
   population = np.random.uniform(a, b, pop_size)
   ```

2. **Evaluación del fitness**
   - Cada individuo es evaluado con la función objetivo.
   - El valor de fitness corresponde directamente a \( f(x) \).

   ```python
   fitness = f(population)
   ```

3. **Selección**
   - Se utiliza el **método de torneo**: se eligen dos individuos al azar y se conserva el que tenga mayor fitness.
   - Este proceso se repite hasta llenar la población de padres.

   ```python
   i, j = np.random.randint(0, pop_size, 2)
   parents.append(population[i] if fitness[i] > fitness[j] else population[j])
   ```

4. **Cruce (recombinación)**
   - Se combinan dos padres para generar descendientes.
   - En este caso, se usa un **cruce promedio** (promedio de los valores de los padres).

   ```python
   child1 = (p1 + p2) / 2
   child2 = (p1 + p2) / 2
   ```

5. **Mutación**
   - Con una cierta probabilidad (`mutation_rate`), se altera ligeramente el valor de algunos descendientes.
   - Esto mantiene la diversidad genética y evita la convergencia prematura.

   ```python
   mutation_mask = np.random.rand(pop_size) < mutation_rate
   offspring[mutation_mask] += np.random.uniform(-1, 1, np.sum(mutation_mask))
   offspring = np.clip(offspring, a, b)
   ```

6. **Actualización**
   - La nueva generación reemplaza a la anterior.
   - Se guarda el **mejor fitness** de cada generación para analizar la convergencia.

   ```python
   fitness_history.append(np.max(fitness))
   population = offspring
   ```

---

### 📈 Visualización de la convergencia

El algoritmo se ejecuta durante **100 generaciones** con **dos tasas de mutación diferentes** (`0.02` y `0.15`).  
Se grafica la evolución del fitness máximo alcanzado en cada generación para observar la **convergencia del algoritmo**:

```python
plt.plot(ga1_fit, label='Mutación 0.02')
plt.plot(ga2_fit, label='Mutación 0.15')
plt.title('Convergencia del fitness en el algoritmo genético')
plt.xlabel('Generaciones')
plt.ylabel('Máximo fitness alcanzado')
plt.legend()
plt.grid(True)
plt.savefig("Punto_1_convergencia_genetico.png", dpi=300)
plt.show()
```

El resultado es una gráfica que muestra cómo el algoritmo mejora progresivamente las soluciones hasta estabilizarse en el máximo global de la función.


## 📦 Ejemplo Resultado
<img width="196" height="84" alt="imagen" src="https://github.com/user-attachments/assets/c8cc58c6-fcd3-4f7c-82dc-de9b33d2fe87" />

---

## 🧭 Conclusión

Los tres métodos convergen al mismo máximo global dentro del intervalo dado, pero:
- **Hill Climbing** puede atascarse si el paso es muy grande.  
- **Greedy Search** explora mejor el entorno.  
- **Genético** ofrece mayor robustez y control mediante parámetros (mutación, cruce, generaciones).

---

## ✨ Autor
**Paula S**  

