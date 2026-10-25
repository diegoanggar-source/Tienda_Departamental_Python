class Producto:
    def __init__(self, categoriaproducto, nombreproducto, precioproducto, stock_producto, sucursal):
        self.__categoriaproducto = categoriaproducto
        self.__nombreproducto = nombreproducto
        self.__precioproducto = precioproducto
        self.__stock_producto = stock_producto
        self.sucursal = sucursal
    
    #GETTERS
    def getcategoriaproducto(self):
        return self.__categoriaproducto
    def getnombreproducto(self):
        return self.__nombreproducto
    def getprecioproducto(self):
        return self.__precioproducto
    def getstock(self):
        return self.__stock_producto

    #SETTERS
    def setcategoriaproducto(self, categoriaproducto):
        self.__categoriaproducto = categoriaproducto
    def setnombreproducto(self, nombreproducto):
        self.__nombreproducto = nombreproducto
    def setprecioproducto(self, precioproducto):
        self.__precioproducto = precioproducto
    def setstock(self, stock_producto):
        self.__stock_producto = stock_producto
    
    #METODO
    def mostrar_informacion(self):
        info = f" Inventario en la sucursal: {self.sucursal} \n Categoria: {self.__categoriaproducto}\n  - {self.__nombreproducto} - ${self.__precioproducto} ({self.__stock_producto} en stock)"
        return info