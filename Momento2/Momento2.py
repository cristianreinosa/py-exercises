class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def calcular_precio_venta(self, margen_de_venta):
        self.precio_de_venta = self.costo / (1 - margen_de_venta)

class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def imprimir_listado(self):
        for id, producto in self.productos.items():
            print(f"ID: {id}, Nombre: {producto.nombre}, Precio de Venta: {producto.precio_de_venta}")

if __name__ == "__main__":
    registro = RegistroProductos()

    while True:
        print("1. Agregar producto")
        print("2. Imprimir listado de productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            costo = float(input("Costo del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            margen_de_venta = float(input("Margen de venta (porcentaje): ")) / 100

            producto = Producto(id, nombre, descripcion, costo, cantidad)
            producto.calcular_precio_venta(margen_de_venta)
            registro.agregar_producto(producto)
            print("Producto agregado con éxito.")

        elif opcion == "2":
            registro.imprimir_listado()

        elif opcion == "3":
            break
