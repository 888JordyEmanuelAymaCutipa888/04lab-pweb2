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
    aux = self.img
    negativeImagen = []
    lineaNueva = ""

    cont = 0
    i = (len(aux[cont])-1)
    limite = (len(aux)-1)
    caracter = "";

    while i>=0:
        caracter = aux[cont][i]
        lineaNueva = self._invColor(caracter) + lineaNueva
        i -= 1;
        if i < 0:
            negativeImagen.append(lineaNueva)
            lineaNueva = ""
            i = (len(aux[cont])-1)
            cont += 1
            if cont > limite:
                i = -1

    return Picture(negativeImagen)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    aux = self.img
    imagenParametro = p.img;
    unionDerecha = []
    nuevaLinea = ""

    limite =len(aux)
    i = 0

    while i < limite:
        nuevaLinea = aux[i] + imagenParametro[i]
        unionDerecha.append(nuevaLinea)
        i += 1

    return Picture(unionDerecha)

  def up(self, p):
    aux = self.img
    immagenParametro = p.img
    unionEncima = []

    for linea in immagenParametro:
        unionEncima.append(linea)

    for linea in aux:
        unionEncima.append(linea)

    return Picture(unionEncima)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    imagenActual = self.img
    immagenParametro = p.img
    arregloUnder = []

    cont = 0
    limitLinea = len(imagenActual[cont])
    limitArreglo = len(imagenActual)
    i = 0

    indicador = True

    lineaDeUnder = ""

    while indicador:
        caracterParametro = immagenParametro[cont][i]
        if caracterParametro != " ":
            lineaDeUnder = lineaDeUnder + caracterParametro
        else:
            lineaDeUnder = lineaDeUnder + imagenActual[cont][i]
        i += 1
        if i == limitLinea:
            arregloUnder.append(lineaDeUnder)
            lineaDeUnder = ""
            i = 0
            cont += 1
            if cont == limitArreglo:
                indicador = False

    return Picture(arregloUnder)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    imagenActual = self.img
    horizontalRepeat= []


    cont = 0
    limitRepeticiones = n
    limitArreglo = len(imagenActual)
    i = 0

    indicador = True

    lineaRepeat = ""

    while indicador:
        i += 1
        if i == limitRepeticiones:
            i = 0
            cont += 1
            if cont == limitArreglo:
                indicador = False

    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

