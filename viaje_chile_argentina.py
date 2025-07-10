# viaje_chile_argentina.py

import time

# Ciudades con distancias simuladas (en km) y tiempos (en horas)
rutas = {
    ("Santiago", "Buenos Aires"): (1400, 18),
    ("Valparaíso", "Mendoza"): (400, 6),
    ("Concepción", "Córdoba"): (1100, 14),
    ("Puerto Montt", "Bariloche"): (320, 5),
    ("La Serena", "San Juan"): (630, 8)
}

medios_transporte = {
    "auto": 1,
    "bus": 1.2,
    "avión": 0.25
}

def main():
    while True:
        print("\n--- Planificador de Viajes Chile ↔ Argentina ---")
        origen = input("Ingrese la *Ciudad de Origen* (o 's' para salir): ").title()
        if origen.lower() == 's':
            print("¡Hasta luego!")
            break

        destino = input("Ingrese la *Ciudad de Destino* (o 's' para salir): ").title()
        if destino.lower() == 's':
            print("¡Hasta luego!")
            break

        ruta = (origen, destino)
        if ruta not in rutas:
            print("Ruta no disponible o datos no cargados.")
            continue

        distancia_km, tiempo_horas = rutas[ruta]
        distancia_millas = round(distancia_km * 0.621371, 2)

        print("Seleccione medio de transporte: auto, bus o avión")
        medio = input("→ Medio: ").lower()

        if medio not in medios_transporte:
            print("Medio no reconocido.")
            continue

        factor = medios_transporte[medio]
        tiempo_real = round(tiempo_horas * factor, 1)

        print(f"\n🧭 Ruta: {origen} → {destino}")
        print(f"📏 Distancia: {distancia_km} km / {distancia_millas} millas")
        print(f"🕒 Duración estimada en {medio}: {tiempo_real} horas")
        print(f"📘 Narrativa del viaje: Saldrás desde {origen}, cruzarás la cordillera hacia {destino} en un viaje de aproximadamente {tiempo_real} horas en {medio}.\n")

        time.sleep(1)

if __name__ == "__main__":
    main()
