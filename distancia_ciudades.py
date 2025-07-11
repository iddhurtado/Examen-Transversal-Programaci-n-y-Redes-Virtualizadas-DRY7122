# distancia_ciudades.py

import requests

def obtener_datos(origen, destino, modo, api_key):
    url = "http://www.mapquestapi.com/directions/v2/route"
    params = {
        "key": api_key,
        "from": origen,
        "to": destino,
        "unit": "k",
        "routeType": modo
    }
    response = requests.get(url, params=params)
    return response.json()

modos = {
    "1": "fastest",
    "2": "shortest",
    "3": "pedestrian",
    "4": "bicycle"
}

api_key = "zpOdWMvpPhcb23zhyXXwVPgl8Pjqw9VF"

while True:
    print("\n--- CALCULADORA DE RUTAS CHILE - ARGENTINA ---")
    print("Escribe 's' en cualquier campo para salir.")

    origen = input("Ciudad de origen: ")
    if origen.lower() == 's':
        break

    destino = input("Ciudad de destino: ")
    if destino.lower() == 's':
        break

    print("\nElija el medio de transporte:")
    print("1 - Vehículo (rápido)")
    print("2 - Ruta más corta")
    print("3 - A pie")
    print("4 - Bicicleta")
    tipo = input("Opción: ")

    if tipo.lower() == 's' or tipo not in modos:
        break

    datos = obtener_datos(origen, destino, modos[tipo], api_key)

    try:
        distancia_km = datos["route"]["distance"]
        tiempo = datos["route"]["formattedTime"]
        distancia_mi = round(distancia_km * 0.621371, 2)

        print(f"\n📍 Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
        print(f"⏱ Duración estimada: {tiempo}")

        print("\n🛣 Narrativa del viaje:")
        for paso in datos["route"]["legs"][0]["maneuvers"]:
            print("-", paso["narrative"])

    except KeyError:
        print("\n❌ No se pudo calcular la ruta. Verifica las ciudades.\n")

