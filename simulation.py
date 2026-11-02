class Tree:
    def __init__(self, id, energy, x, y):
        self.id = id
        self.energy = energy
        self.age = 0
        self.x = x
        self.y = y

    def live_one_step(self):
        self.age += 1
        self.energy = min(100, self.energy + 2)


strom_1 = Tree(1, 30, 2, 3)
strom_2 = Tree(2, 50, 5, 5)
strom_3 = Tree(3, 70, 8, 2)

# Seznam všech stromů
stromy = [strom_1, strom_2, strom_3]

# Pět kroků pro všechny stromy
for krok in range(5):  
    for strom in stromy:    
       strom.live_one_step()

for strom in stromy:
    print(
        "Strom:", strom.id,
        "Poloha:", strom.x, strom.y,
        "Věk:", strom.age,
        "Energie:", strom.energy
    )
