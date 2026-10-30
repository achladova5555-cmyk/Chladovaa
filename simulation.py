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

    def live_one_step(self):
        self.age += 1
        self.energy = min(100, self.energy + 2)


strom_1 = Tree(1, 30)
strom_2 = Tree(2, 50)
strom_3 = Tree(3, 70)

# Seznam všech stromů
stromy = [strom_1, strom_2, strom_3]

# Pět kroků pro všechny stromy
for krok in range(5):



    
    for strom in stromy:







        
        strom.live_one_step()

print("První strom:", strom_1.age, strom_1.energy)
print("Druhý strom:", strom_2.age, strom_2.energy)
print("Třetí strom:", strom_3.age, strom_3.energy)
