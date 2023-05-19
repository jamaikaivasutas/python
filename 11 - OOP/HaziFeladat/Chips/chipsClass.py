class Chips:
    def __init__(self, brand: str, flavor: str, price: int):
        self.brand: str  = brand 
        self.flavor: str  = flavor
        self.price: int = price

    def __str__(self) -> str:
        return f"Márka: {self.brand}\n Íz: {self.flavor}\n Ár: {self.price} Ft "