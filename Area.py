class Area:
  def __init__(self, lado):
    self.lado = lado

  def area_quadrada(self):
    return self.lado ** 2

  def area_cubica(self):
    return 6 * (self.lado ** 2)

lado = float(input("Digite o numero de termo da sequecia de fibonacci: ")

area = Area(lado)

print(f"A area quadrada: {area.area_quadrada}")

print(f"A area cubica: {area.area_cubica}")
