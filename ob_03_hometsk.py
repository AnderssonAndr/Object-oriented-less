import json

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Animal sound"

    def eat(self):
        return f"{self.name} питается."

class Bird(Animal):
    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} says: Карр-Карр"

class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} says: Хрю-хрю"

class Reptile(Animal):
    def __init__(self, name: str, age: int, is_venomous: bool):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        return f"{self.name} says: Ш-Ш-Ш"

# Полиморфизм 
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Employee:
    def __init__(self, name: str):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal: Animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(Employee):
    def heal_animal(self, animal: Animal):
        print(f"{self.name} is healing {animal.name}.")

# Композиция - класс содеожит и животных и сотрудников
class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.__class__.__name__}: {animal.name}, {animal.age} years old")

    def show_employees(self):
        for employee in self.employees:
            print(f"{employee.__class__.__name__}: {employee.name}")

    # Сохранение и загрузка состояния зоопарка
    def save_to_file(self, filename="zoo_data.json"):
        data = {
            "animals": [
                {
                    "type": animal.__class__.__name__,
                    "name": animal.name,
                    "age": animal.age,
                    "extra": animal.__dict__
                } for animal in self.animals
            ],
            "employees": [{
                    "type": employee.__class__.__name__,
                    "name": employee.name
                } for employee in self.employees
            ]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Zoo data saved to {filename}")

    def load_from_file(self, filename="zoo_data.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.animals = []
            for a in data.get("animals", []):
                if a["type"] == "Bird":
                    animal = Bird(a["name"], a["age"], a["extra"]["wing_span"])
                elif a["type"] == "Mammal":
                    animal = Mammal(a["name"], a["age"], a["extra"]["fur_color"])
                elif a["type"] == "Reptile":
                    animal = Reptile(a["name"], a["age"], a["extra"]["is_venomous"])
                else:
                    animal = Animal(a["name"], a["age"])
                self.animals.append(animal)

            self.employees = []
            for e in data.get("employees", []):
                if e["type"] == "ZooKeeper":
                    emp = ZooKeeper(e["name"])
                elif e["type"] == "Veterinarian":
                    emp = Veterinarian(e["name"])
                else:
                    emp = Employee(e["name"])
                self.employees.append(emp)

            print(f"Zoo data loaded from {filename}")

        except FileNotFoundError:
            print("No saved zoo data found.")


# Демонстрация работы
if __name__ == "__main__":
    zoo = Zoo("My Awesome Zoo")

    # Создаем животных
    parrot = Bird("Polly", 2, 0.25)
    lion = Mammal("Simba", 5, "golden")
    snake = Reptile("Kaa", 4, True)

    # Добавляем в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Сотрудники
    keeper = ZooKeeper("John")
    vet = Veterinarian("Alice")

    zoo.add_employee(keeper)
    zoo.add_employee(vet)

    # Демонстрация
    zoo.show_animals()
    zoo.show_employees()

    # Полиморфизм
    print("\nAnimal sounds:")
    animal_sound(zoo.animals)

    # Действия сотрудников
    keeper.feed_animal(lion)
    vet.heal_animal(snake)

    # Сохранение и загрузка
    zoo.save_to_file()
    new_zoo = Zoo("Restored Zoo")
    new_zoo.load_from_file()
    new_zoo.show_animals()
    new_zoo.show_employees()




 
