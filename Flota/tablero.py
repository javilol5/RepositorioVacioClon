class Tablero:

    def __init__(self, tamano):

        self.dimensiones = (tamano, tamano)
        self.casillas = []

        for fila in range(tamano):
            fila_actual = []
            for columna in range(tamano):
                fila_actual.append(0)
            self.casillas.append(fila_actual)

    def mostrar_tablero(self):

        print("\nTABLERO:")
        for fila in self.casillas:
            print(" ".join(str(casilla) for casilla in fila))