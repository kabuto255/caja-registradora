productos = {
    "001": {"nombre": "Leche", "precio": 25.0},
    "002": {"nombre": "Pan", "precio": 15.0},
    "003": {"nombre": "Jugo de naranja", "precio": 30.0},
    "004": {"nombre": "Café", "precio": 80.0},
    "005": {"nombre": "Azúcar", "precio": 50.0},
    "006": {"nombre": "Arroz", "precio": 40.0},
    "007": {"nombre": "Frijoles", "precio": 60.0},
    "008": {"nombre": "Aceite", "precio": 90.0},
    "009": {"nombre": "Sal", "precio": 20.0},
    "010": {"nombre": "Harina", "precio": 35.0},
    "011": {"nombre": "Mantequilla", "precio": 70.0},
    "012": {"nombre": "Queso", "precio": 100.0},
    "013": {"nombre": "Yogur", "precio": 45.0},
    "014": {"nombre": "Huevos", "precio": 55.0},
    "015": {"nombre": "Jabón", "precio": 25.0},
    "016": {"nombre": "Shampoo", "precio": 120.0},
    "017": {"nombre": "Pasta dental", "precio": 35.0},   
    "018": {"nombre": "Desodorante", "precio": 80.0},
    "019": {"nombre": "Detergente", "precio": 150.0},
    "020": {"nombre": "Limpiador multiusos", "precio": 90.0},
}

carrito = []
total = 0.0

print("--- CAJA REGISTRADORA ---")
print("Códigos disponibles: 001 (Leche), 002 (Pan), 003 (Jugo de naranja), 004 (Café), 005 (Azúcar), 006 (Arroz), 007 (Frijoles), 008 (Aceite), 009 (Sal), 010 (Harina), 011 (Mantequilla), 012 (Queso), 013 (Yogur), 014 (Huevos), 015 (Jabón), 016 (Shampoo), 017 (Pasta dental), 018 (Desodorante), 019 (Detergente), 020 (Limpiador multiusos)")
print("Escribe 'fin' para terminar la compra.\n")

while True:
    codigo = input("Ingrese el código del producto: ")
    if codigo.lower() == "fin":
        break
    
    if codigo in productos:
        prod = productos[codigo]
        carrito.append(prod)
        total += prod["precio"]
        print(f"Agregado: {prod['nombre']} - ${prod['precio']:.2f}")
    else:
        print("Código no válido. Intente de nuevo.")

print("\n--- RESUMEN DE COMPRA ---")
for item in carrito:
    print(f"- {item['nombre']}: ${item['precio']:.2f}")
print(f"Total a pagar: ${total:.2f}")
