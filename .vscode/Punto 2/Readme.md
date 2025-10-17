# 🚗 Problema del Viajante (TSP) con Algoritmo Genético

Este proyecto implementa una solución al **Problema del Viajante (Travelling Salesman Problem, TSP)** utilizando un **Algoritmo Genético**.  
El objetivo es encontrar el **camino más corto** para que visita todas las ciudades exactamente una vez y regresa a la ciudad de origen.

---

## 🎯 Objetivo del Problema

Dadas **10 ciudades con coordenadas aleatorias**, se desea encontrar el **recorrido óptimo** que minimiza la distancia total recorrida.

Cada ciudad se representa por un punto en el plano 2D:

\[
d(i, j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
\]

La distancia total del recorrido es la suma de las distancias entre ciudades consecutivas, incluyendo el retorno a la primera ciudad.

---

## ⚙️ Implementación del Algoritmo

La solución se implementa dentro de una clase llamada `TSPGeneticAlgorithm`, lo que permite ajustar fácilmente los parámetros como la **tasa de mutación**, el **tamaño de la población**, y el **número de generaciones**.

### 🔧 Principales componentes:

1. **Inicialización de la población**
   - Cada individuo representa un orden posible en el que visitar las ciudades.
   - La población inicial se genera aleatoriamente.

   ```python
   self.population = [np.random.permutation(self.num_cities) for _ in range(self.pop_size)]
   ```

2. **Evaluación del fitness**
   - El fitness es el inverso de la distancia total del recorrido (ya que queremos minimizar la distancia).

   ```python
   fitness = 1 / np.array([self.total_distance(route) for route in self.population])
   ```

3. **Selección**
   - Se seleccionan dos individuos al azar y se conserva el que tenga mejor fitness.

   ```python
   def tournament_selection(self, fitness):
       i, j = np.random.randint(0, self.pop_size, 2)
       return self.population[i] if fitness[i] > fitness[j] else self.population[j]
   ```

4. **Cruce / Crossover**
   - Se aplica un cruce tipo **Order Crossover (OX)**, que mantiene parte del orden de las ciudades de los padres.

   ```python
   start, end = sorted(np.random.randint(0, self.num_cities, 2))
   child = [None]*self.num_cities
   child[start:end] = parent1[start:end]
   pointer = end
   for city in parent2:
       if city not in child:
           if pointer >= self.num_cities:
               pointer = 0
           child[pointer] = city
           pointer += 1
   ```

5. **Mutación**
   - Se intercambian dos posiciones del recorrido con cierta probabilidad (`mutation_rate`).
   - Este paso introduce **diversidad genética** y evita que el algoritmo se estanque en mínimos locales.

   ```python
   if np.random.rand() < self.mutation_rate:
       i, j = np.random.randint(0, self.num_cities, 2)
       child[i], child[j] = child[j], child[i]
   ```
---

## 📊 Resultados

Para comparar el comportamiento del algoritmo, se ejecutó la clase `TSPGeneticAlgorithm` con **cuatro tasas de mutación diferentes**:

| Escenario | Tasa de mutación | Color en la gráfica |
|------------|------------------|----------------------|
| GA1 | 0.01 | 🔵 Azul |
| GA2 | 0.70 | 🟢 Verde |
| GA3 | 1.50 | 🟡 Amarillo |
| GA4 | 3.30 | 🔴 Rojo |

Cada ejecución genera:
1. La gráfica de **convergencia del fitness** a lo largo de las generaciones.

![Convergencia](https://github.com/RogueOne-22/Laboratorio_3/blob/4b6fe8935f7a132250a2c2915aad44f935861a1c/.vscode/Punto%202/Punto_2_convergencia.png)

2. Una **visualización del recorrido óptimo** encontrado para esa configuración.

La representación del recorrido óptimo:

![Recorrido](https://github.com/RogueOne-22/Laboratorio_3/blob/4b6fe8935f7a132250a2c2915aad44f935861a1c/.vscode/Punto%202/Punto_2_recorridos.png)

---

## 🧩 Cambios realizados para mejorar la diversidad

En las primeras versiones, el algoritmo obtenía **resultados idénticos** sin importar la tasa de mutación.  
Para solucionar esto se realizaron las siguientes mejoras:

1. **Mutación basada en intercambio aleatorio múltiple**  
   - En lugar de intercambiar solo una pareja de ciudades, se permite realizar varios intercambios según la tasa de mutación.

2. **Inicialización completamente aleatoria en cada ejecución**  
   - Se resembró el generador de números aleatorios (`np.random.seed(None)`) antes de cada corrida.

3. **Selección por torneo en lugar de ruleta**  
   - Esto introduce más presión selectiva, lo que cambia la dinámica del algoritmo según la tasa de mutación.

4. **Aumento del tamaño de población y número de generaciones**
   - Permite observar diferencias en la convergencia y diversidad de soluciones.

---

## 🧠 Conclusiones

- Tasas de mutación bajas (0.01–0.05) tienden a **converger más rápido**, pero pueden quedarse atrapadas en mínimos locales.  
- Tasas más altas (0.10–0.20) ofrecen **mayor exploración del espacio de búsqueda**, generando recorridos más diversos y, en ocasiones, mejores soluciones globales.
- Ajustar los parámetros genéticos permite **balancear la explotación y exploración**, clave para resolver problemas combinatorios como el TSP.

---

🧬 *Autor:* Paula S
