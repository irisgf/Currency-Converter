import requests

def obtener_tipo_cambio(base, simbolo):
    url = f"https://v6.exchangerate-api.com/v6/cd91ebeb1564fb5de5dd4103/latest/{base}"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        if respuesta.status_code == 200:
            return datos["conversion_rates"].get(simbolo, None)
        else:
            print(f"Error al obtener los datos: {datos['error-type']}")
            return None
    except Exception as e:
        print(f"Error en la conexión: {e}")
        return None

def conversor_divisas():
    print("=== Conversor de Divisas ===")
    base = input("Introduce la moneda base (por ejemplo, USD): ").upper()
    simbolo = input("Introduce la moneda a convertir (por ejemplo, EUR): ").upper()
    cantidad = float(input(f"¿Cuántos {base} deseas convertir? "))

    tipo_cambio = obtener_tipo_cambio(base, simbolo)

    if tipo_cambio:
        resultado = cantidad * tipo_cambio
        print(f"{cantidad} {base} son {resultado:.2f} {simbolo} al tipo de cambio actual.")
    else:
        print("No se pudo obtener el tipo de cambio. Revisa los datos ingresados.")

if __name__ == "__main__":
    conversor_divisas()
