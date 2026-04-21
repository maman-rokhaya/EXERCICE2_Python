class Point3D:

    Npts = 0
    Mx   = None
    My   = None
    Mz   = None

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

        Point3D.Npts += 1

        if Point3D.Mx is None or x > Point3D.Mx:
            Point3D.Mx = x
        if Point3D.My is None or y > Point3D.My:
            Point3D.My = y
        if Point3D.Mz is None or z > Point3D.Mz:
            Point3D.Mz = z

    @classmethod
    def getNpts(cls):
        return cls.Npts

    @classmethod
    def getMaxX(cls):
        return cls.Mx

    @classmethod
    def getMaxY(cls):
        return cls.My

    @classmethod
    def getMaxZ(cls):
        return cls.Mz

    def __repr__(self):
        return f"Point3D({self.__x}, {self.__y}, {self.__z})"

    def __str__(self):
        return f"Point de coordonnées ({self.__x}, {self.__y}, {self.__z})"

    @staticmethod
    def est_sur_diagonale(x, y, z):
        return x == y == z


p1 = Point3D(1, 2, 3)
p2 = Point3D(5, 0, 7)
p3 = Point3D(3, 9, 4)
p4 = Point3D(6, 6, 6)

print(p1)
print(p2)
print(p3)
print(p4)

print()

try:
    print(p1.x)
except AttributeError as e:
    print(f"p1.x   → ERREUR : {e}")

try:
    print(p1.__x)
except AttributeError as e:
    print(f"p1.__x → ERREUR : {e}")

print(f"p1._Point3D__x = {p1._Point3D__x}")

print()

print(f"Nombre de points créés : {Point3D.getNpts()}")
print(f"Max x : {Point3D.getMaxX()}")
print(f"Max y : {Point3D.getMaxY()}")
print(f"Max z : {Point3D.getMaxZ()}")

print()

for (x, y, z) in [(1,1,1), (3,3,5), (6,6,6), (2,3,4)]:
    print(f"({x}, {y}, {z}) → {Point3D.est_sur_diagonale(x, y, z)}")

print()

print(f"str(p1)  → {str(p1)}")
print(f"repr(p1) → {repr(p1)}")
