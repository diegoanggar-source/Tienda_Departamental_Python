from clase.classSucursal import Sucursal
from clase.classCategoria import Categoria
from clase.classProducto import Producto

import xml.etree.ElementTree as ET
from lxml import etree
import os

class AdministrarSucursales:
    def __init__(self):
        self.sucursales = []
    
    #AGREGA NUEVAS SUCURSALES
    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

    #SHOW ALL OF THE INVENTORY
    def obtener_todo_el_inventario(self):
        texto = ""
        for sucursal in self.sucursales:
            texto += sucursal.obtener_inventario_como_texto()
        return texto
    
    def obtener_nombre_sucursales(self):
        return [s.nombresucursal for s in self.sucursales]
    
    #Funcion para cargar el archivo XML
    def leer_archivo(self,nombre_archivo):
        try:
            self.sucursales = []  # limpiar antes de cargar
            arbol = ET.parse(nombre_archivo)
            raiz = arbol.getroot() # <Sucursales>
        
            #Itera sobre cada <Sucursal>
            for elemento_sucursal in raiz.findall('Sucursal'):
                nombre_sucursal = elemento_sucursal.get('nombre')
                nueva_sucursal = Sucursal(nombre_sucursal)
                self.sucursales.append(nueva_sucursal)

                #Itera sobre cada <Categoria> dentro de la Sucursal
                for elemento_categoria in elemento_sucursal.findall('categoria'):
                    nombre_categoria = elemento_categoria.get('nombre')

                    #Itera sobre cada <Producto> dentro de la Categoria
                    for elemento_producto in elemento_categoria.findall('producto'):
                        #Extraccion y conversion de tipos
                        nombre_producto = elemento_producto.get('nombre')
                        precio_producto = float(elemento_producto.get('precio',0.0))
                        stock_producto = int(elemento_producto.get('existencia',0))

                        #Crear el objeto Producto
                        producto = Producto(
                        nombre_categoria,
                        nombre_producto,
                        precio_producto,
                        stock_producto,
                        nombre_sucursal
                        )

                        #Usar el metodo de la Sucursal para agregar el producto
                        #Este metodo se encarga de crear/encontrar la Categoria y agregar el Producto
                        nueva_sucursal.agregar_producto(nombre_categoria, producto)
                        
        except FileNotFoundError:
            print(f"Error El archivo '{nombre_archivo}' no fue encontrado.")
        except Exception as e:
            print(f"Ocurrio un error durante el proceso del XML: {e}")
            
    #Funcion de validar el archivo XML
    def validar_xml_con_dtd(self, nombre_archivo_xml: str, nombre_archivo_dtd: str) -> bool:

        try:
            #1. Cargar el DTD
            dtd = etree.DTD(nombre_archivo_dtd)

            #2. Crear un parser estandar sin argumentos dtd
            parser = etree.XMLParser()

            #3. Parsear el XML
            #Nota:  Lxml primero parsea el XML para encontrar la referencia al DTD
            tree = etree.parse(nombre_archivo_xml, parser)

            #4. Validar el arbol parseado contra el DTD cargado
            if dtd.validate(tree):
                print(f"¡El archivo '{nombre_archivo_xml}' es valido estructuralmente!")
                return True
            else:
                print(f"¡El arhivo XML NO es valido. Errores de validacion!")
                #Mostrar los errores especifios del DTD
                for error in dtd.error_log:
                    print(f" - Línea {error.line}, columna {error.column}: {error.message}")
                return False
            
        except etree.DTDParseError as e:
            print(f"Error al parsear el DTD(Revisar la sintaxis del DTD): {e}")
            return False
        except etree.XMLSyntaxError as e:
            #Esto captura errores de sintaxis basicos en el XML (malformado)
            print(f"Error de sintaxis XML : {e}")
            return False
        except FileExistsError:
            print("Error: Uno de los archivos (XML o DTD) no fue encontrado")
            return False
        except Exception as e:
            print(f"Ocurrio un Error inesperado durante la validacion: {e}")
            return False