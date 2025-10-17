# 🧩 Tercer Punto – Optimización de Horarios con Algoritmo Genético

## 🎯 Objetivo
El objetivo de este ejercicio es **crear un horario escolar óptimo** que cumpla con las siguientes condiciones:
1. No se superpongan clases para un mismo grupo.  
2. Asignar profesores disponibles sin conflictos de horario.  
3. Respetar preferencias horarias para ciertas materias.  
4. Lograr una distribución balanceada de asignaturas entre los grupos.

Para resolverlo, se utiliza un **Algoritmo Genético** que busca mejorar iterativamente una población de posibles horarios hasta encontrar una combinación con el mejor “puntaje de ajuste” o *fitness*.

---

## ⚙️ Estructura del código

La solución está implementada dentro de una clase:

```python
class ScheduleOptimizer:
```

Esta clase encapsula toda la lógica del algoritmo genético y permite ajustar fácilmente la tasa de mutación, número de generaciones y tamaño de la población.

### 🔹 Inicialización 
Se definen los datos del problema:
- Profesores disponibles.
- Materias a dictar.
- Grupos de estudiantes.
- Franja horaria semanal.
- Preferencias horarias para ciertas materias.

Además, se inicializan parámetros genéticos como:
- `mutation_rate`: probabilidad de mutación.  
- `generations`: cantidad de iteraciones evolutivas.  
- `pop_size`: tamaño de la población.

---

## 🧬 Etapas del Algoritmo Genético

### 1️⃣ Creación de la población inicial
Cada individuo de la población representa un horario completo generado de forma aleatoria.

```python
def create_schedule(self):
    schedule = []
    for time in self.time_slots:
        for group in self.groups:
            teacher = np.random.choice(self.teachers)
            subject = np.random.choice(self.subjects)
            schedule.append((time, group, teacher, subject))
    return schedule
```

---

### 2️⃣ Evaluación de fitness
Cada horario es evaluado según las restricciones del problema.

**Criterios de evaluación:**
- Penalización por superposición de profesores en un mismo horario.
- Penalización por materias fuera de sus horarios preferidos.
- Recompensa (mayor puntaje) por distribución equilibrada de materias.

```python
def evaluate_schedule(self, schedule):
    score = 100
    # Penalizar superposición
    # Penalizar horarios no preferidos
    # Recompensar distribución equilibrada
    return score
```

---

### 3️⃣ Cruce 
Se seleccionan dos padres y se combinan para crear un nuevo individuo (horario).

```python
def crossover(self, parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child
```

---

### 4️⃣ Mutación
Introduce variaciones aleatorias en algunos genes (cambios en profesor o materia) para evitar estancamiento.

```python
def mutate(self, schedule):
    if random.random() < self.mutation_rate:
        idx = random.randint(0, len(schedule) - 1)
        time, group, teacher, subject = schedule[idx]
        new_teacher = np.random.choice(self.teachers)
        new_subject = np.random.choice(self.subjects)
        schedule[idx] = (time, group, new_teacher, new_subject)
    return schedule
```

---

### 5️⃣ Evolución y convergencia
El algoritmo evoluciona durante varias generaciones, guardando el mejor puntaje de cada iteración.  
Finalmente, se obtiene el horario más óptimo encontrado.

```python
best_schedule, best_score, best_score_history = optimizer.run()
```

---

## 📊 Comparación de tasas de mutación

Se ejecuta el optimizador con **cuatro tasas de mutación distintas**:
- `0.01`
- `0.09`
- `1.70`
- `2.50`

Cada una se representa con un color diferente en la gráfica de convergencia.

---

## 📈 Visualización de resultados

Se genera una gráfica que muestra cómo evoluciona el puntaje máximo de fitness a lo largo de las generaciones para cada tasa de mutación.

[Convergencia ](https://github.com/RogueOne-22/Laboratorio_3/blob/8db581842b6e2f8f5ea0afae29178e9a61dea037/Punto%203/optimizacion_horarios_fitness.png)

---
###**Horarios**

[Horario 1](https://github.com/RogueOne-22/Laboratorio_3/blob/8db581842b6e2f8f5ea0afae29178e9a61dea037/Punto%203/horario_optimo_mut_1.png)

[Horario 2](https://github.com/RogueOne-22/Laboratorio_3/blob/8db581842b6e2f8f5ea0afae29178e9a61dea037/Punto%203/horario_optimo_mut_5.png)

[horario 3](https://github.com/RogueOne-22/Laboratorio_3/blob/8db581842b6e2f8f5ea0afae29178e9a61dea037/Punto%203/horario_optimo_mut_10.png)

## 🧾 Resultados esperados

- El algoritmo mejora progresivamente el puntaje de fitness.
- Las diferentes tasas de mutación producen ligeras variaciones en el resultado:
  - Tasas bajas → convergencia más estable pero más lenta.  
  - Tasas altas → más exploración, pero posible inestabilidad.  
- Se obtiene un **horario óptimo** que cumple las restricciones y respeta las preferencias.

Ejemplo de salida en consola:
```
--- MUTACIÓN 0.10 ---
Mejor puntaje: 96.0
Horario óptimo encontrado:
('Lun-9:00', 'Grupo1', 'ProfB', 'Matemáticas')
('Lun-9:00', 'Grupo2', 'ProfA', 'Ciencias')
('Lun-9:00', 'Grupo3', 'ProfC', 'Historia')
...
```

---

## 💡 Conclusiones

- El uso del **algoritmo genético** permite resolver problemas combinatorios complejos como la planificación de horarios.  
- Ajustar la **tasa de mutación** cambia el equilibrio entre exploración y explotación del espacio de búsqueda.  
- Con una buena definición de restricciones y parámetros, el modelo genera horarios viables y adaptados a las condiciones deseadas.

---

🧬 *Autor:* Paula S