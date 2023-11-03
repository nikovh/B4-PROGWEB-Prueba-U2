def agregar_compra(lista_compras):
    producto = float(input("Ingrese el monto de la compra: "))
    lista_compras.append(producto)
    print("Nueva compra agregada correctamente.")

def mostrar_compras(lista_compras):
    if not lista_compras:
        print("No hay compras registradas.")
    else:
        for i, producto in enumerate(lista_compras, start=1):
            print(f"{i}. ${producto:,.2f}")

def mostrar_total(lista_compras):
    total_gastado = sum(lista_compras)
    print(f"El total gastado hasta el momento es de : ${total_gastado:,.2f}")

def main():
    compras = []
    total_gastado = 0
    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Favor, seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
main()