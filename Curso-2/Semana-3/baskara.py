import math, pytest

class Bhaskara:

    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)

        if d < 0:
            return 0

        raiz1 = (-b + math.sqrt(d)) / (2 * a)

        if d == 0:
            return 1, raiz1

        raiz2 = (-b - math.sqrt(d)) / (2 * a)

        return 2, raiz1, raiz2


class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara()

    def testa_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    def testa_duas_raizes(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    def testa_zero_raizes(self, b):
        assert b.calcula_raizes(10, 10, 10) == 0

    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)


def main():
    bhaskara = Bhaskara()

    a = float(input("Digite o valor de a "))
    b = float(input("Digite o valor de b "))
    c = float(input("Digite o valor de c "))
    print(bhaskara.calcula_raizes(a, b, c))

