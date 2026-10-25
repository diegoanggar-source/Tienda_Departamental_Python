from clase.classAdministrardorSU import AdministrarSucursales
from clase.classProducto import Producto
from clase.classSucursal import Sucursal
import tkinter as tk
from tkinter import messagebox, PhotoImage, ttk
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

# LISTA DE OBJETOS
productos = []
sucursales = []
admin = AdministrarSucursales()

class MenuAplicacion:
    def __init__(self, root):
                
        self.root = root
        self.root.title("Gestión de Inventario por Sucursal")
        self.root.geometry("500x550")
        self.root.configure(bg="#f0f4f7")

        # TITULO
        titulo = tk.Label(root, text="Menu Principal", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#2c3e50")
        titulo.pack(pady=30)

        # BOTONES
        self.crear_boton("➕ Agregar sucursal",self.Agregar_sucursal_nueva)
        self.crear_boton("📦 Agregar Producto a Inventario", self.ventana_agregar_producto)
        self.crear_boton("📊 Mostrar inventario", self.mostrar_inventario_en_ventana)
        self.crear_boton("❌ Salir", self.salir)
    def salir(self):

        #--------------------------- 2 Crear el arbol XML a partir de los datos del administrador -----------------------------

        root = ET.Element("Sucursales")

        # Ahora iteramos sobre la lista de sucursales que esta dentro de nuestro objeto administrador.
        for sucursales in admin.sucursales:
            sucusal_element=ET.SubElement(root,"Sucursal", nombre=sucursales.nombresucursal)
            for categoria in sucursales.get_categoria():
                categoria_element = ET.SubElement(sucusal_element,"categoria",nombre=str(categoria.get_nombre()))
                for productos in categoria.get_productos():
                    producto_element=ET.SubElement(categoria_element,"producto",nombre=productos.getnombreproducto()
                                                   ,precio=str(productos.getprecioproducto())
                                                   ,existencia=str(productos.getstock()))
        tree=ET.ElementTree(root)
        ET.indent(tree, space = "   ", level = 0)
        tree.write("src/config/inventario.xml",encoding="utf-8",xml_declaration=True)
        self.root.destroy()

    def Agregar_sucursal_nueva(self):
        self.root.withdraw()
        ventana_N_sucursal=tk.Toplevel(self.root)
        ventana_N_sucursal.title("Agregar Sucursal")
        ventana_N_sucursal.geometry("450x350")
        
        #Titulo
        titulo_N_sucursal=tk.Label(ventana_N_sucursal,text="Agregar Sucursal",font=("Helvetica",20,"bold"),bg="#f0f4f7",fg="#2c3e50")
        titulo_N_sucursal.pack(pady=10)
        
        #Entrada de datos
        tk.Label(ventana_N_sucursal,text="Nombre de la Sucursal",font=("Helvetica", 10, "bold")).pack(pady=5)
        nombre_N_sucursal_entry=tk.Entry(ventana_N_sucursal)
        nombre_N_sucursal_entry.pack(pady=5)
        
        #GUARDADO DE DATOS
        def agregar_sucursal():
            nombre_sucursal = nombre_N_sucursal_entry.get().strip()

            #-------------------------------------------------------------------------
            for suc in admin.sucursales:
                if suc.nombresucursal.lower() == nombre_sucursal.lower():
                    messagebox.showerror("Error", "La sucursal ya existe")
                return
            #-------------------------------------------------------------------------

            #CAMPOS VACIOS
            if not nombre_sucursal:
                messagebox.showwarning("Advertencia","El campo tiene que estar lleno")
                return False
            nueva_sucursal = Sucursal(nombre_sucursal)
            admin.sucursales.append(nueva_sucursal)

            messagebox.showinfo("Exito",f"Sucursal '{nombre_sucursal}' agregada correctamente.")
            ventana_N_sucursal.destroy()
            self.root.deiconify()
                
        #BOTON PARA GUARDAR SUCURSAL
        boton_G_sucural = tk.Button(
            ventana_N_sucursal, text="💾 Guardar", command=agregar_sucursal,
            font=("Arial", 14), bg="#3498bd", fg="white", width=30, 
            height=2, relief="raised",bd=3
            )
        boton_G_sucural.pack(pady=15)            
    
    # CREACION DEL BOTON
    def crear_boton(self, texto, comando):
        boton = tk.Button(
            self.root, text=texto, command=comando,
            font=("Arial", 14), bg="#3498bd", fg="white",
            width=30, height=2, relief="raised", bd=3
        )
        boton.pack(pady=10)
    
    
    # VENTANA PARA AGREGAR OBJETOS
    def ventana_agregar_producto(self):
        if not admin.sucursales:
            messagebox.showwarning("Advertencia", "Primero debes agregar una sucursal")
            return
        self.root.withdraw()
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto a Sucursal")
        ventana.geometry("450x550")

        #TITULO
        titulo = tk.Label(ventana, text="Agregar Producto a Sucursal", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#2c3e50")
        titulo.pack(pady=10)
        
        opciones = tk.StringVar()
        opciones.set("Selecciona una sucursal")

        nombre_sucursales = [sucursal.nombresucursal for sucursal in admin.sucursales]

        combo_mostrar_opciones = tk.OptionMenu(ventana, opciones, *nombre_sucursales)
        combo_mostrar_opciones.pack(pady=5)
        
        tk.Label(ventana, text="Indique una Categoria:").pack(pady=10)
        categoria_entry = tk.Entry(ventana)
        categoria_entry.pack(pady=10)

        tk.Label(ventana, text="Nombre del Producto:").pack(pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack(pady=5)

        tk.Label(ventana, text="Precio del Producto: $").pack(pady=5)
        precio_entry = tk.Entry(ventana)
        precio_entry.pack(pady=5)

        tk.Label(ventana, text="Existencia:").pack(pady=5)
        stock_entry = tk.Entry(ventana)
        stock_entry.pack(pady=5)

        # GUARDADO DE DATOS
    
        def agregar_producto():
            categoria = categoria_entry.get()
            nombre_producto = nombre_entry.get()
            precio_producto = precio_entry.get()
            stock_producto = stock_entry.get()
            sucursal_seleccionada = opciones.get()

            sucursal_obj = None

            for suc in admin.sucursales:
                if suc.nombresucursal == sucursal_seleccionada:
                    sucursal_obj = suc
                    break

            # CREAR OBJETO            
            if self.validar_datos_producto(categoria,nombre_producto, precio_producto, stock_producto, sucursal_seleccionada):
                producto = Producto(categoria, nombre_producto, precio_producto, stock_producto, sucursal_seleccionada)

                if sucursal_obj:
                    agregado = sucursal_obj.agregar_producto(categoria, producto)

                if not agregado:
                    messagebox.showerror("Error", "El producto ya existe en esa categoría")
                    return 

                productos.append(producto)
                messagebox.showinfo("Información", "Producto agregado con Exito")
                ventana.destroy()
                self.root.deiconify()

        #BOTON PARA EL GUARDADO DE DATOS
        botonG = tk.Button(
            ventana, text="💾 Guardar", command=agregar_producto,
            font=("Arial", 14), bg="#3498bd", fg="white",
            width=30, height=2, relief="raised",bd=3
            )
        botonG.pack(pady=10)

    # VALIDACION (ahora bien declarada)
    def validar_datos_producto(self,categoria ,nombre_producto, precio_producto, stock_producto, sucursal_seleccionada):
        #1. CAMPOS VACIOS
        if not  categoria or not nombre_producto or not precio_producto or not stock_producto:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return False
        if sucursal_seleccionada == "Selecciona una sucursal":
            messagebox.showwarning("Advertencia", "Debes seleccionar una sucursal")
            return False
        #2. VALIDAR PRECIO  
        try:
            precio_producto = float(precio_producto)
            if precio_producto <= 0:
                messagebox.showerror("Error", "El precio debe de ser valido")
                return False
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido.")
            return False
        #3. VALIDAR STOCK
        try:
            stock_producto = int(stock_producto)
            if stock_producto < 0:
                messagebox.showerror("Error", "El stock debe de ser valido")
        except ValueError:
            messagebox.showerror("Error", "El stock debe ser un número entero.")
            return False
        #IF EVERYTHING IS VALID
        return True

    # MOSTRAR INVENTARIO
    def mostrar_inventario_en_ventana(self):

        if not admin.sucursales:
            messagebox.showinfo("Información", "No se encuentran productos registrados")
            return
        inventario = {}

        # ORGANIZAR PRODUCTOS POR SUCURSAL Y CATEGORIA
        for suc in admin.sucursales:
            sucursal = suc.nombresucursal

            if sucursal not in inventario:
                inventario[sucursal] = {}

            for cat in suc.get_categoria():
                categoria = cat.get_nombre()

                if categoria not in inventario[sucursal]:
                    inventario[sucursal][categoria] = []

                #ORDENAR ALFABETICAMENTE
                cat.get_productos().sort(key=lambda p: p.getnombreproducto().lower())

                for producto in cat.get_productos():
                    inventario[sucursal][categoria].append(producto)

                 # Lower: Convierte el texto a minusculas, para que pueda comparar y acomodar de manera alfabetica sin problemas
                
    
        # CONSTRUIR TEXTO
        info = ""
        for sucursal, categorias in inventario.items():
            info += f"\nInventario en la Sucursal: {sucursal}\n"
            for categoria, lista_productos in categorias.items():
                info += f"Categoria: {categoria}\n"
                for producto in lista_productos:
                    info += f"   - {producto.getnombreproducto()} - ${float(producto.getprecioproducto()):.2f} ({producto.getstock()} en stock)\n"

        messagebox.showinfo("Inventario Completo", info)

def mostrar_splash(root):
    splash = tk.Toplevel(root)
    splash.title("Pantalla de Bienvenida")
    splash.geometry("500x500")
    splash.config(bg="white")

    # 1. TÍTULO
    label_titulo = tk.Label(
        splash,
        text="Pantalla de Bienvenida",
        font=("Arial", 18, "bold"),
        bg="white"
    )
    label_titulo.pack(pady=20)

    # 2. IMAGEN
    try:
        imagen = PhotoImage(file="src/IMG/logo-blue.png")
        imagen = imagen.subsample(7)
        splash.imagen = imagen
        label_img = tk.Label(splash, image=imagen, bg="white")
        label_img.pack(pady=10)
    
    except Exception as e:
        tk.Label(splash, text="[Logo no encontrado]", bg="white").pack()

    # 3. MENSAJE
    label_mensaje = tk.Label(splash, text="Cargando, por favor espere...", font=("Arial", 12, "italic"), bg="white", fg="gray" )
    label_mensaje.pack(pady=20)

    # 4. BARRA DE PROGRESO
    progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="indeterminate")
    progress.pack(pady=10)

    progress.start(10)  # Velocidad de animación
    splash.progress = progress
    return splash

# EJECUCIÓN
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.withdraw()
    splash = mostrar_splash(ventana)

    admin = AdministrarSucursales()

    def iniciar_app():
        ruta_xml = "src/config/inventario.xml"
        ruta_dtd = "src/config/inventario.dtd"

        #VALIDACIÓN
        if admin.validar_xml_con_dtd(ruta_xml, ruta_dtd):

            admin.leer_archivo(ruta_xml)

            splash.progress.stop()
            splash.destroy()
            ventana.deiconify()
            app = MenuAplicacion(ventana)

        else:
            splash.progress.stop()
            splash.destroy()
            messagebox.showerror("Error","La estructura del archivo XML es incorrecta. Verifica el DTD/XML")
            ventana.destroy()  # opcional: cerrar app si falla

    ventana.after(5000, iniciar_app)  # puedes bajar el tiempo para pruebas
    ventana.mainloop()