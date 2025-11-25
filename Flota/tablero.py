class Tablero:

    def __init__(self, tamano):

        self.dimensiones = (tamano, tamano)
        self.casillas = []

        for fila in range(tamano):
            fila_actual = []
            for columna in range(tamano):
                fila_actual.append(0)
            self.casillas.append(fila_actual)
