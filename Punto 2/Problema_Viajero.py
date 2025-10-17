import numpy as np
import random
import matplotlib.pyplot as plt

class TSPGeneticAlgorithm:
    def __init__(self, num_cities=10, population_size=150, generations=400, mutation_rate=0.05):
        self.num_cities = num_cities
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.cities = self.generate_cities(num_cities)

    def generate_cities(self, n):
        """Genera coordenadas aleatorias (x, y) para las ciudades."""
        return [(np.random.rand(), np.random.rand()) for _ in range(n)]

    def distance(self, city1, city2):
        """Distancia euclidiana entre dos ciudades."""
        return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def total_distance(self, route):
        """Distancia total de una ruta."""
        return sum(self.distance(self.cities[route[i]], self.cities[route[i+1]]) 
                   for i in range(len(route)-1)) + self.distance(self.cities[route[-1]], self.cities[route[0]])

    def ordered_crossover(self, parent1, parent2):
        """Cruce OX (ordenado) más aleatorio."""
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [None] * len(parent1)
        child[start:end] = parent1[start:end]

        fill_pos = end
        for city in parent2:
            if city not in child:
                if fill_pos >= len(parent1):
                    fill_pos = 0
                child[fill_pos] = city
                fill_pos += 1
        return child

    def swap_mutation(self, route):
        """Mutación más agresiva (dependiendo del mutation_rate)."""
        route = route.copy()
        num_swaps = max(1, int(self.mutation_rate * len(route)))
        for _ in range(num_swaps):
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
        return route

    def tournament_selection(self, population, k=5):
        """Selección por torneo."""
        tournament = random.sample(population, k)
        tournament.sort(key=lambda r: self.total_distance(r))
        return tournament[0]

    def run(self):
        """Ejecuta el algoritmo genético."""
        population = [random.sample(range(self.num_cities), self.num_cities) for _ in range(self.population_size)]
        best_route = min(population, key=self.total_distance)
        best_distances = []

        for generation in range(self.generations):
            new_population = [best_route]  # elitismo: el mejor pasa directo
            for _ in range(self.population_size - 1):
                parent1 = self.tournament_selection(population)
                parent2 = self.tournament_selection(population)
                child = self.ordered_crossover(parent1, parent2)
                child = self.swap_mutation(child)
                new_population.append(child)

            population = new_population
            current_best = min(population, key=self.total_distance)
            if self.total_distance(current_best) < self.total_distance(best_route):
                best_route = current_best

            best_distances.append(self.total_distance(best_route))

        return best_route, best_distances

    def plot_routes(self, routes, mutation_rates):
        """Muestra las rutas óptimas obtenidas para cada tasa de mutación."""
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        axs = axs.ravel()
        for i, (route, rate) in enumerate(zip(routes, mutation_rates)):
            x = [self.cities[i][0] for i in route] + [self.cities[route[0]][0]]
            y = [self.cities[i][1] for i in route] + [self.cities[route[0]][1]]
            axs[i].plot(x, y, 'o-r')
            axs[i].set_title(f"Recorrido Óptimo - Mutación {rate}")
            axs[i].set_xlabel("X")
            axs[i].set_ylabel("Y")
            axs[i].grid(True)
        plt.tight_layout()
        plt.savefig("Punto_2_recorridos.png", dpi=300)
        plt.show()

    def plot_evolution(self, all_best_distances, mutation_rates):
        """Grafica la convergencia del fitness."""
        plt.figure(figsize=(10, 6))
        for distances, rate in zip(all_best_distances, mutation_rates):
            plt.plot(distances, label=f"Mutación {rate}")
        plt.title("Evolución de la Distancia Mínima (Mutaciones Comparadas)")
        plt.xlabel("Generaciones")
        plt.ylabel("Distancia mínima")
        plt.legend()
        plt.grid(True)
        plt.savefig("Punto_2_convergencia.png", dpi=300)
        plt.show()


# ===========================
#   Diferentes tasas de mutación
# ===========================
if __name__ == "__main__":
    mutation_rates = [0.01, 0.7, 1.5, 3.3]
    best_routes = []
    all_best_distances = []

    tsp = TSPGeneticAlgorithm(num_cities=10, generations=400)
    cities = tsp.cities  # mantener las mismas ciudades

    for rate in mutation_rates:
        tsp.mutation_rate = rate
        tsp.cities = cities
        print(f"\nEjecución con tasa de mutación = {rate}")
        best_route, best_distances = tsp.run()
        best_routes.append(best_route)
        all_best_distances.append(best_distances)
        print(f"→ Mejor distancia encontrada: {tsp.total_distance(best_route):.4f}")

    tsp.plot_routes(best_routes, mutation_rates)
    tsp.plot_evolution(all_best_distances, mutation_rates)
