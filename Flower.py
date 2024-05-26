class Greenhouse:
  Greenhouse = '----[My Greenhouse]----'
  def __init__(self, name, color):
    self.name = name
    self.color = color
  def nameis(self):
    return self.name
  def coloris(self):
    return self.color

class Flowers(Greenhouse):
  age = 2
  sum = 25
  def __init__(self, name, color):
    super().__init__(name, color)
  def nameis(self):
    return super().nameis()
  def coloris(self):
    return super().coloris()
flowers = Flowers('hollyhock','pink')
print(flowers.Greenhouse)
print(f'Flower: {flowers.nameis()}, Color: {flowers.coloris()} \ninfo')
print(f'Age: {flowers.age}, Sum: {flowers.sum}')