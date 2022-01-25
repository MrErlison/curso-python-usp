
class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return "equilátero"

        if self.a != self.b and self.a != self.c and self.b != self.c:
            return "escaleno"

        return "isósceles"

