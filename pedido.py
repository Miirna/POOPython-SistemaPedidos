'''
1. Crear una clase Producto con los siguientes atributos:
    -codigo
    -precio
    -nombre
Crear su contructor, getter y setter y una funcion llamada "calcular total" donde le pasaremos unas unidades y nos debe calcular
el precio final
'''
from itertools import product
from operator import index
from os import closerange
import re


class Producto:

    #constructor
    def __init__(self, codigo, nombre, precio, descuento = None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__desuento = descuento

    #getters and setters
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    '''@property
    def precio(self):
        return self.__precio'''

    @property
    def precio(self):
        if self.__desuento == None:
            return self.__precio
        else:
            return self.__desuento.aplicarDescuento(self.__precio)


    @precio.setter
    def precio(self, valor):
        #self.__precio = valor
        self.precio = valor


    #metodos
    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', Nombre: ' + self.__nombre + ', Precio: $' + str(self.__precio)

    def calcularTotal(self, cantidad):
        return self.precio * cantidad


'''
2. Crear una clase Pedido que tenga como atributos 
    -lista de productos
    -lista de cantidades
y agrega la siguiente funcionalidad
    -total de pedidos: muestra el precio final del pedido
    -mostrar productos: muestra los productos del pedido
'''

'''
3. Agregar dentro de la clase pedido la siguiente funcionalidad
    -agregar producto: Le pasamos un producto y una cantidad y agregar ese proucto y cantidad a su respectiva lista
Debemos validad que le dato que nos pasen sea valido.En caso de que no, devolver una excepcion
    -eliminar productos: Le pasamos el producto a borrar, si existe, lo eliminamos, sino devoler una excepcion indicandolo
Corroborar tambien que es un producto lo que mandan 
'''

class Pedido:
    '''def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades'''

    def __init__(self):
        self.__productos = []
        self.__cantidades = []

    def agregarProducto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('Agregar Producto: producto debe ser de la clase producto.')

        if not isinstance(cantidad, int):
            raise Exception('Agregar producto: la cantidad debe ser un numero.')

        if cantidad <= 0:
            raise Exception("Agregar Producto: cantidad debe ser mayor que 0")

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminarProducto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('Eliminar Producto: producto debe ser de la clase producto.')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        else:
            raise Exception("Eliminar Producto: producto no existe")

    def totalPedidos(self):
        total = 0

        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcularTotal(c)
        return total

    def mostrarProductos(self):
        i = 1
        for (p,c) in zip(self.__productos, self.__cantidades):
            print(i, "Producto:", p.nombre, "Cantidad: ", str(c))
            i+= i


'''
4. Crear una clase Descuento que tiene los siguientes atributos:
    -tipo: es un string y solo puede ser fijo o porcentaje
    -valor: es un numero , si es fijo debe ser mayor que 0 y si es porcentaje el valor debe ser entre 1 y 100
Metodos:
    -aplicar descuento(precio):
        -Si el tipo es Fijo, se le resta la cantidad al precio
        -si el tipo es Porcentaje se le resta el porcentaje al precio
Agregar este descuento al producto, este sera opcional y solo se aplicara si tiene descuento
Valida que el descuento se cree correctamente
'''

TIPO_DESC_FIJO = "Fijo"
TIPO_DESC_PORC = "Porcentaje"

class Descuento:
    def __init__(self, tipo, valor):
        if not isinstance(valor, int):
            raise ValueError("constructor descuento: valor debe ser un numero")

        if not isinstance(tipo, str):
            raise ValueError("constructor descuento: tipo debe ser un string")
        
        if tipo != TIPO_DESC_PORC and tipo != TIPO_DESC_FIJO:
            raise ValueError("constructor descuento: el tipo debe ser fijo o porcentaje")

        if tipo == TIPO_DESC_FIJO and valor <= 0:
            raise ValueError("constructor descuento: el valor del tipo fijo debe ser mayor que 0")

        if tipo == TIPO_DESC_PORC and (valor <= 0 or valor > 100):
            raise ValueError("constructor descuento: el valor del tipo porcentaje debe estar entre 1 y 100")

        self.__tipo = tipo
        self.__valor = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, val):
        self.__valor = val


    def aplicarDescuento(self, precio):
        if self. __tipo == TIPO_DESC_FIJO:
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        else:
            return precio - (precio *  (self.__valor / 100))





if __name__ == '__main__':

    papel = Producto(1, "Papel", 80)
    shapoo = Producto(2, "Shampoo", 65)
    cloro = Producto(3, "Cloro", 45)
    whiskas = Producto(4, "Whiskas", 150)
    rastillos = Producto(5, "Rastillos", 80)

    flag = True
    while flag:
        try:
            print("""
                ---------------------------------------------------------------------------
                ---------------------------------------------------------------------------
                Seleccione un numero:
                1. Hacer Pedido
                2. Salir del programa
                ---------------------------------------------------------------------------
                ---------------------------------------------------------------------------
            """)
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                productos = []
                cantidades = []    
                pedido = Pedido()   
                flag2 = True
                while flag2:
                    print("""
                    1. Agregar producto al pedido
                    2. Eliminar producto al pedido
                    3. Mostrar Pedido
                    """)
                    n = int(input("Seleccione una opcion: "))
                    if n == 1:
                        print("1. ", papel.nombre)
                        print("2. ", shapoo.nombre)
                        print("3. ", cloro.nombre)
                        print("4. ", whiskas.nombre)
                        print("5. ", rastillos.nombre)
                        res = int(input("Cual es el nombre del Producto que desea agregar? :"))
                        cantidad = int(input("Ingrese la cantidad: "))
                        product = Producto(0, "", 0)
                        if res == 1:
                            producto = papel
                        elif res == 2:
                            producto = shapoo
                        elif res == 3:
                            producto = cloro
                        elif res == 4:
                            producto = whiskas
                        elif res == 5:
                            producto = rastillos
                        pedido.agregarProducto(producto, cantidad)
                    elif n == 2:
                        pedido.mostrarProductos()
                        res = input("Que producto desea eliminar")
                        if res == 'Papel':
                            producto = papel
                        elif res == 'Shampoo':
                            producto = shapoo
                        elif res == "Cloro":
                            producto = cloro
                        elif res == "Whiskas":
                            producto = whiskas
                        elif res == "Rastillos":
                            producto = rastillos
                        pedido.eliminarProducto(producto)
                    elif n == 3:
                        print("--->Pedido<---")
                        pedido.mostrarProductos()
                        print("Total del pedido: $", pedido.totalPedidos(), " MX")
                    elif n > 3:
                        print("Ops! esa opcion no es valida")
            elif opcion == 3:
                flag = False
                print("Programa terminado")
            elif opcion > 3:
                print("Ops! esa opcion no es valida")
        except ValueError:
            print("Error, seleccione una opcion correcta")

    #desc1 = Descuento(TIPO_DESC_FIJO, 5)
    #desc2 = Descuento(TIPO_DESC_PORC, 50)

    #producto1 = Producto(1, 'Producto 1', 50, desc2)
    #producto2 = Producto(2, 'Producto 2', 100)

    #print(producto1)
    #print(producto2)
    #print(producto1.calcularTotal(5))
    #print(producto2.calcularTotal(5))

    #lista
    #productos = [producto1, producto2]
    #cantidades = [10, 5]
  
    
    #pedido = Pedido(productos, cantidades)
    #pedido = Pedido()
    '''try:
        
        pedido.agregarProducto(producto1, 5)
        pedido.agregarProducto(producto2, 2)

        print( "Total pedido: ", str(pedido.totalPedidos()))
        pedido.mostrarProductos()

        pedido.eliminarProducto(producto1)

        print( "Total pedido: ", str(pedido.totalPedidos()))
        pedido.mostrarProductos()

    except Exception as e:
        print(e)'''

    #print( "Total pedido: ", str(pedido.totalPedidos()))
    #pedido.mostrarProductos()
