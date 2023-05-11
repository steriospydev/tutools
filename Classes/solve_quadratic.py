import cmath

class Quad:
  def __int__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c

  def get_abc(self):
    self.a = int(input(f"Enter element a:"))
    self.b = int(input(f"Enter element b:"))
    self.c = int(input(f"Enter element c:"))

    
  def solve(self):
    d = (self.b ** 2) - (4 * self.a * self.c)
    sol1 = (-self.b - cmath.sqrt(d)) / (2 * self.a)
    sol2 = (-self.b + cmath.sqrt(d)) / (2 * self.a)
    print("The solution are {0} and {1}".format(sol1, sol2))


equation = Quad()
equation.get_abc()
equation.solve()