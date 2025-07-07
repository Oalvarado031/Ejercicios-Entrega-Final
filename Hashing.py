# Implementación sencilla de tabla hash con encadenamiento


class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]


    def funcion_hash(self, clave):
        # Convierte la clave en un índice entre 0 y tamaño - 1
        return hash(clave) % self.tamaño


    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        # Revisar si la clave ya existe
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)  # Actualiza valor
                return
        self.tabla[indice].append((clave, valor))  # Si no existe, agrega


    def obtener(self, clave):
        indice = self.funcion_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None  # No encontrado


    def mostrar(self):
        for i, cubeta in enumerate(self.tabla):
            print(f"Índice {i}: {cubeta}")


# Uso del código
if __name__ == "__main__":
    tabla = TablaHash(5)


    # Insertar claves y valores
    tabla.insertar("nombre", "Eduardo")
    tabla.insertar("edad", 25)
    tabla.insertar("ciudad", "Managua")
    tabla.insertar("profesion", "Ingeniero")
    tabla.insertar("edad", 26)  # Actualiza valor existente


    # Mostrar tabla completa
    tabla.mostrar()


    # Obtener un valor
    print("Edad:", tabla.obtener("edad"))
