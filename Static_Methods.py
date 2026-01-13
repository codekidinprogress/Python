class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Janitor"))