class Rectangle:

    Nrect      = 0
    MaxSurface = None

    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

        Rectangle.Nrect += 1

        surface = largeur * hauteur
        if Rectangle.MaxSurface is None or surface > Rectangle.MaxSurface:
            Rectangle.MaxSurface = surface

    @classmethod
    def getNrect(cls):
        return cls.Nrect

    @classmethod
    def getMaxSurface(cls):
        return cls.MaxSurface

    def __repr__(self):
        return f"Rectangle({self.__largeur}, {self.__hauteur})"

    def __str__(self):
        surface = self.__largeur * self.__hauteur
        return f"Rectangle : largeur={self.__largeur}, hauteur={self.__hauteur}, surface={surface}"

    @staticmethod
    def le_plus_grand(r1, r2):
        s1 = r1._Rectangle__largeur * r1._Rectangle__hauteur
        s2 = r2._Rectangle__largeur * r2._Rectangle__hauteur
        if s1 >= s2:
            return r1
        else:
            return r2


r1 = Rectangle(2, 3)
r2 = Rectangle(5, 4)
r3 = Rectangle(1, 7)

print(r1)
print(r2)
print(r3)

print()

try:
    print(r1.largeur)
except AttributeError as e:
    print(f"r1.largeur   → ERREUR : {e}")

try:
    print(r1.__largeur)
except AttributeError as e:
    print(f"r1.__largeur → ERREUR : {e}")

print()

print(f"Nombre de rectangles créés : {Rectangle.getNrect()}")
print(f"Plus grande surface        : {Rectangle.getMaxSurface()}")

print()

print(f"repr(r1) → {repr(r1)}")
r4 = eval(repr(r1))
print(f"r4 reconstruit via eval(repr(r1)) → {r4}")

print()

grand = Rectangle.le_plus_grand(r1, r2)
print(f"Le plus grand entre r1 et r2 → {grand}")

grand = Rectangle.le_plus_grand(r2, r3)
print(f"Le plus grand entre r2 et r3 → {grand}")
