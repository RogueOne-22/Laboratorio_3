# 🧬 Proyecto de Optimización con Algoritmos Genéticos

Este proyecto reúne **tres ejercicios de optimización** resueltos mediante **algoritmos genéticos (GA)**, abarcando desde funciones matemáticas hasta problemas combinatorios complejos.

---

## ⚙️ 1. Maximización de una función cuadrática

### 🧩 Descripción
El primer ejercicio busca **maximizar la función**:

\[
f(x) = x^2 - 3x + 4
\]

usando distintos métodos heurísticos, incluyendo el **algoritmo genético**.

### 🔍 Detalles
- Se generan individuos representando valores de `x`.
- La función de aptitud (fitness) evalúa directamente `f(x)`.
- Se aplican operadores de **selección, cruce y mutación**.
- Se comparan resultados con métodos **Hill Climbing** y **Greedy**.

### 📈 Visualización
El código grafica:
- La función cuadrática.
- Los puntos óptimos hallados por cada método.
- La evolución del fitness en el algoritmo genético para distintas tasas de mutación (`0.01`, `0.70`, `1.5`, `3.0`).

![Convergencia 1](https://github.com/RogueOne-22/Laboratorio_3/blob/9ee1d412a85a225c27aa5aae2f0131abd008c81b/Punto%201/Punto_1_convergencia_genetico.png)

### 💡 Observaciones
El algoritmo genético presenta una mejor exploración del espacio de búsqueda y evita caer en mínimos locales, en comparación con los otros enfoques.

---

## 🗺️ 2. Problema del Viajante (TSP)

### 🧩 Descripción
El segundo ejercicio aborda el **TSP (Traveling Salesman Problem)** con 10 ciudades de coordenadas aleatorias.  
El objetivo es **encontrar el recorrido más corto** que visite todas las ciudades exactamente una vez.

### 🧬 Implementación del Algoritmo Genético
- **Representación:** Permutación de las ciudades.
- **Fitness:** Inverso de la distancia total del recorrido.
- **Operadores genéticos:**
  - Cruce: método de orden (OX).
  - Mutación: intercambio de posiciones aleatorias.
- **Evolución:** 100 generaciones con diferentes tasas de mutación (`0.01`, `0.09`, `1.7`, `2.5`).

### 📊 Resultados
- Se grafican las rutas óptimas obtenidas con cada tasa de mutación.
- Se muestra la convergencia del fitness a lo largo de las generaciones.
- Se observa que tasas de mutación más altas promueven mayor diversidad y evitan estancamiento en óptimos locales.

![Convergencia 2](https://github.com/RogueOne-22/Laboratorio_3/blob/9ee1d412a85a225c27aa5aae2f0131abd008c81b/Punto%202/Punto_2_convergencia.png)

---

## 🕒 3. Optimización de Horarios Escolares

### 🧩 Descripción
El tercer ejercicio aplica el algoritmo genético para **generar un horario escolar óptimo**, cumpliendo las siguientes restricciones:

- Ningún grupo tiene clases simultáneas.
- Los profesores asignados están disponibles en los horarios.
- Se respetan preferencias horarias de materias específicas.

### 🧬 Implementación
- **Representación:** Cada individuo es un conjunto de clases `(hora, grupo, profesor, materia)`.
- **Fitness:** Penaliza conflictos, indisponibilidad y violación de preferencias.
- **Cruce:** Combina subconjuntos de clases entre padres.
- **Mutación:** Intercambia materias o profesores aleatoriamente.
- **Evolución:** 100 generaciones, mostrando cómo el horario se optimiza progresivamente.

### 📈 Visualización
Se genera un gráfico que muestra:
- La evolución del fitness por generación.
- Comparación de resultados entre distintas tasas de mutación.

![Convergencia 3](https://github.com/RogueOne-22/Laboratorio_3/blob/9ee1d412a85a225c27aa5aae2f0131abd008c81b/Punto%203/optimizacion_horarios_fitness.png)

---

## 🧠 Conclusiones Generales

- Los **algoritmos genéticos** son herramientas flexibles para resolver distintos tipos de optimización, desde funciones continuas hasta combinatorias.
- Ajustar la **tasa de mutación** influye directamente en la diversidad de soluciones y en la capacidad del algoritmo para evitar estancamientos.
- Las representaciones del problema y la función de fitness son clave para obtener resultados eficientes y realistas.

---

🧬 *Autor:* Paula S

