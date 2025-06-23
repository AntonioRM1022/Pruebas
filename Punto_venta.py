class Productos:
    def usuario(self):
        print("Cualquier usuario y contraseña")

    def discos(self):
        print("Cualquier cantidad de discos")

    def tarros(self):
        print("Cualquier cantidad de tarros")

    def tazas(self):
        print("Cualquier cantidad de tazas")

class Login(Productos):
    def __init__(self):
        self.leer = input

    def usuario(self):
        usuario_default = "Tadeo"
        contraseña_default = "1234"
        
        u = input("Ingresa tu usuario: ")
        c = input("Ingresa tu contraseña: ")
        
        if u == usuario_default and c == contraseña_default:
            print("Inicio de sesión exitoso.")
        else:
            print("Usuario o contraseña incorrectos.")
            exit()  # Detiene la ejecución del programa si el inicio de sesión falla.

class VentaDiscos(Productos):
    def __init__(self):
        self.leer = input
        self.leer2 = input
        self.cantidadd = 0
        self.pago = 0
        self.sel = 0

    def discos(self):
        self.cantidadd = int(input("Ingresa la cantidad de discos a comprar: "))
        print(f"Total: ${150 * self.cantidadd}")

        self.pago = int(input("¿Cuánto deseas pagar? "))
        while self.pago != (150 * self.cantidadd):
            if self.pago > (150 * self.cantidadd):
                print("Pago exitoso")
                print(f"Su cambio: {self.pago - (150 * self.cantidadd)}")
                break
            else:
                print("Cantidad inválida, paga de nuevo")
                self.pago = int(input("¿Cuánto deseas pagar? "))

        print("¿Deseas imprimir tu ticket?")
        print("1-----Si")
        print("2-----No")
        self.sel = int(input())
        if self.sel == 1:
            print("Vendedor: Tadeo")
            print("Producto: Discos")
            print(f"Cantidad: {self.cantidadd}")
            print(f"Total: ${self.cantidadd * 150}")
            print(f"Pago: ${self.pago}")
            print(f"Cambio: ${self.pago - (self.cantidadd * 150)}")
        else:
            print("Gracias por su compra")

class VentaTarros(Productos):
    def __init__(self):
        self.leer = input
        self.leer2 = input

    def tarros(self):
        cantidadtar = int(input("Ingresa la cantidad de tarros a comprar: "))
        print(f"Total: ${100 * cantidadtar}")

        pago = int(input("¿Cuánto deseas pagar? "))
        while pago != (100 * cantidadtar):
            if pago > (100 * cantidadtar):
                print("Pago exitoso")
                print(f"Su cambio: {pago - (100 * cantidadtar)}")
                break
            else:
                print("Cantidad inválida, paga de nuevo")
                pago = int(input("¿Cuánto deseas pagar? "))

        print("¿Deseas imprimir tu ticket?")
        print("1-----Si")
        print("2-----No")
        sel = int(input())
        if sel == 1:
            print("Vendedor: Tadeo")
            print("Producto: Tarros")
            print(f"Cantidad: {cantidadtar}")
            print(f"Total: ${cantidadtar * 100}")
            print(f"Pago: ${pago}")
            print(f"Cambio: ${pago - (cantidadtar * 100)}")
        else:
            print("Gracias por su compra")

class VentaTazas(Productos):
    def __init__(self):
        self.leer = input
        self.leer2 = input

    def tazas(self):
        cantidadt = int(input("Ingresa la cantidad de tazas a comprar: "))
        print(f"Total: ${80 * cantidadt}")

        pago = int(input("¿Cuánto deseas pagar? "))
        while pago != (80 * cantidadt):
            if pago > (80 * cantidadt):
                print("Pago exitoso")
                print(f"Su cambio: {pago - (80 * cantidadt)}")
                break
            else:
                print("Cantidad inválida, paga de nuevo")
                pago = int(input("¿Cuánto deseas pagar? "))

        print("¿Deseas imprimir tu ticket?")
        print("1-----Si")
        print("2-----No")
        sel = int(input())
        if sel == 1:
            print("Vendedor: Tadeo")
            print("Producto: Tazas")
            print(f"Cantidad: {cantidadt}")
            print(f"Total: ${cantidadt * 80}")
            print(f"Pago: ${pago}")
            print(f"Cambio: ${pago - (cantidadt * 80)}")
        else:
            print("Gracias por su compra")

def main():
    leer = input
    sel = 0
    salir = 0
    f = "Saliendo del programa"
    inicio = Login()
    inicio.usuario()

    while True:
        print("-------MENÚ-------")
        print("1-------Tazas-------")
        print("2-------Tarros-------")
        print("3-------Discos-------")
        sel = int(input("Ingresa qué deseas comprar: "))

        if sel == 1:
            Tazas = VentaTazas()
            Tazas.tazas()
        elif sel == 2:
            Tarros = VentaTarros()
            Tarros.tarros()
        elif sel == 3:
            Discos = VentaDiscos()
            Discos.discos()
        else:
            print("Opción no válida")

        print("¿Deseas salir?")
        print("2----------Sí")
        print("1----------No")
        salir = int(input())
        if salir == 2:
            print(f)
            break

if __name__ == "__main__":
    main()
