
productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Error: Debes introducir un valor para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Error: Debes introducir un número que sea entero para la cantidad.")
    
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido correctamente.\n")

def ver_productos():
    if len(productos) == 0:
        print("No hay productos en el inventario.\n")
        return

    print("\nLista de productos:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()


def actualizar_producto():
    nombre = input("Introduce el nombre del producto que quieres actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto}")
            nuevo_nombre = input("Introduce el nuevo nombre del producto (dejar em vacío para no cambiar): ")
            if nuevo_nombre:
                producto["nombre"] = nuevo_nombre
            
            while True:
                nuevo_precio = input("Introduce el nuevo precio del producto (dejar en vacío para no cambiar): ")
                if nuevo_precio == "":
                    break
                try:
                    producto["precio"] = float(nuevo_precio)
                    break
                except ValueError:
                    print("Error: Debes introducir un valor para el precio.")
            
            while True:
                nueva_cantidad = input("Introduce la nueva cantidad del producto (dejar en vacío para no cambiar): ")
                if nueva_cantidad == "":
                    break
                try:
                    producto["cantidad"] = int(nueva_cantidad)
                    break
                except ValueError:
                    print("Error: Debes introducir un número que sea entero para la cantidad.")
            
            print(f"Producto '{producto['nombre']}' actualizado correctamente.\n")
            return
    print(f"No se encontró un producto con el nombre '{nombre}'.\n")


def eliminar_producto():
    nombre = input("Introduce el nombre del producto que quieres eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.\n")
            return
    print(f"No se encontró un producto con el nombre '{nombre}'.\n")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente en 'productos.txt'.\n")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados correctamente desde 'productos.txt'.\n")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'. Se va a iniciar con una lista vacía.\n")


def menu():
    cargar_datos()
    
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción  que si sea válida.\n")

menu()

