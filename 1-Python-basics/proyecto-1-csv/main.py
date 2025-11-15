import csv
import json

def leer_csv(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)

def generar_reporte(datos):
    total_items = sum(int(item["cantidad"]) for item in datos)
    total_valor = sum(int(item["cantidad"]) * float(item["precio"]) for item in datos)
    
    return {
        "total_items": total_items,
        "total_valor": total_valor,
        "productos": datos
    }

def guardar_json(reporte, ruta="reporte.json"):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    datos = leer_csv("data.csv")
    reporte = generar_reporte(datos)
    guardar_json(reporte)
    print("Reporte generado en reporte.json")
