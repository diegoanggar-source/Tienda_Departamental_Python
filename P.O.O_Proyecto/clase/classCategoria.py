class Categoria:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__producto = []
    
    def get_nombre(self):
        return self.__nombre

    def get_productos(self):
        return self.__producto
    
    def agregar_producto(self, producto):
        for pro in self.__producto:
            if pro.getnombreproducto().lower() == producto.getnombreproducto().lower():
                return False
        
        self.__producto.append(producto)
        return True