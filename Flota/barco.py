class Barco:


    def __init__(self, nombre, longitud):

        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0

    def recibir_impacto(self):
        self.golpes_recibidos += 1

    def esta_hundido(self):
        return self.golpes_recibidos >= self.longitud

    def mostrar_estado(self):
        print(f"{self.nombre} ({self.golpes_recibidos}/{self.longitud}) "
              f"=> {'HUNDIDO' if self.esta_hundido() else 'A FLOTE'}")