# Jednoduchá simulace lesa

strom = {
    "id": 1,
    "x": 5,
    "y": 5,
    "age": 0,
    "energy": 50,
    "alive": True,
}

print(strom)
# Jeden krok simulace
strom["age"] += 1
strom["energy"] = min(100, strom["energy"] + 2)

print("Po jednom kroku:", strom)
# Dalších pět kroků simulace
for krok in range(5):
    strom["age"] += 1
    strom["energy"] = min(100, strom["energy"] + 2)
    print("Věk:", strom["age"], "Energie:", strom["energy"])
    # Společný předpis pro nové stromy
class Tree:
    def __init__(self, id, energy):
        self.id = id
        self.energy = energy
        self.age = 0


# Vytvoření dvou samostatných stromů
strom_1 = Tree(1, 30)
strom_2 = Tree(2, 50)

print("První strom:", strom_1.energy)
print("Druhý strom:", strom_2.energy)
