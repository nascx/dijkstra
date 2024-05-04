class Grafo:
  def __init__(self, vertices) -> None:
    self.vertices = vertices
    self.grafo = [[0] * self.vertices for i in range(self.vertices)]
  
  #origin is 
  def dijkstra (self, origin ):

    custo_vem = [[-1, 0] for i in range(self.vertices)]

    custo_vem[origin - 1] = [0, origin]
