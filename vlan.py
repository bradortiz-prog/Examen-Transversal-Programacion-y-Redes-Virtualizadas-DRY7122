print("=" * 45)
print("VERIFICADOR DE RANGO DE VLAN")
print("=" * 45)

while True:
    dato = input("\nIngrese el número de VLAN (o 's' para salir): ")

    if dato.lower() == "s":
        print("\nPrograma finalizado.")
        break

    if not dato.isdigit():
        print("Error: Debe ingresar un número válido.")
        continue

    vlan = int(dato)

    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} pertenece al RANGO NORMAL.")

    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} pertenece al RANGO EXTENDIDO.")

    else:
        print("La VLAN ingresada está fuera del rango permitido.")
