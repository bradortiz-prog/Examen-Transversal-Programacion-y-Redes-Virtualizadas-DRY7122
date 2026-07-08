import requests

API_KEY = "56fb65dc-ece8-4bc9-8da4-0e16cf9f475b"


def obtener_coordenadas(ciudad):
    url = "https://graphhopper.com/api/1/geocode"

    parametros = {
        "q": ciudad,
        "limit": 1,
        "locale": "es",
        "key": API_KEY
    }

    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code != 200:
        return None

    datos = respuesta.json()

    if len(datos["hits"]) == 0:
        return None

    lat = datos["hits"][0]["point"]["lat"]
    lng = datos["hits"][0]["point"]["lng"]

    return lat, lng


print("=" * 60)
print("CALCULADORA DE DISTANCIA CHILE - ARGENTINA")
print("=" * 60)

while True:

    origen = input("\nCiudad de origen (s para salir): ")

    if origen.lower() == "s":
        print("Programa finalizado.")
        break

    destino = input("Ciudad de destino: ")

    print("\nSeleccione el medio de transporte")
    print("1. Automóvil")
    print("2. Bicicleta")
    print("3. Caminando")

    opcion = input("Opción: ")

    if opcion == "1":
        vehiculo = "car"
    elif opcion == "2":
        vehiculo = "bike"
    elif opcion == "3":
        vehiculo = "foot"
    else:
        print("Opción inválida.")
        continue

    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)

    if coord_origen is None:
        print("No se encontró la ciudad de origen.")
        continue

    if coord_destino is None:
        print("No se encontró la ciudad de destino.")
        continue

    url = "https://graphhopper.com/api/1/route"

    parametros = {
        "point": [
            f"{coord_origen[0]},{coord_origen[1]}",
            f"{coord_destino[0]},{coord_destino[1]}"
        ],
        "vehicle": vehiculo,
        "locale": "es",
        "instructions": "true",
        "calc_points": "false",
        "key": API_KEY
    }

    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code != 200:
        print("\nError al consultar la API")
        print("Código:", respuesta.status_code)
        print(respuesta.text)
        continue

    datos = respuesta.json()

    distancia = datos["paths"][0]["distance"] / 1000
    millas = distancia * 0.621371
    tiempo = datos["paths"][0]["time"] / 1000 / 60 / 60

    print("\n" + "=" * 60)
    print("RESULTADO DEL VIAJE")
    print("=" * 60)

    print(f"Ciudad de origen : {origen}")
    print(f"Ciudad destino   : {destino}")
    print(f"Transporte       : {vehiculo}")
    print(f"Distancia        : {distancia:.2f} km")
    print(f"Distancia        : {millas:.2f} millas")
    print(f"Duración         : {tiempo:.2f} horas")

    print("\nNarrativa del viaje")

    for paso in datos["paths"][0]["instructions"]:
        print("-", paso["text"])
