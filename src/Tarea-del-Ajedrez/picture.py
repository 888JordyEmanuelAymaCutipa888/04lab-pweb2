from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    aux = self.img
    vertical = []

    i = (len(aux)-1)
    while i>=0:
        vertical.append(aux[i])
        i -= 1;

    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    aux = self.img
    horizontal = []
    lineaEspejo = ""

    i = (len(aux)-1)
    cont = 0
    cantLineas = (len(aux[i])-1)

    while i>=0:
        linea = aux[cont];
        lineaEspejo =  lineaEspejo + linea[i];
        i -= 1;
        if i < 0:
            horizontal.append(lineaEspejo)
            lineaEspejo = ""
            i = (len(aux[cont])-1)
            cont += 1
            if cont > cantLineas:
                break

    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

