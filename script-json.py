import json
import time

# Ruta al archivo JSON en la máquina virtual
ruta_archivo_json = "/home/devasc/Documents/myfile.json"

# Función para abrir el archivo JSON y cargarlo en un string
def cargar_json_a_string(ruta):
    try:
        with open(ruta, 'r') as archivo:
            datos_json = json.load(archivo)
        return datos_json
    except FileNotFoundError:
        print("¡Error! No se pudo encontrar el archivo:", ruta)
        return None
    except json.JSONDecodeError:
        print("¡Error! El archivo JSON está mal formateado.")
        return None

# Función para imprimir el valor del token y el tiempo restante antes de que caduque
def imprimir_token_y_tiempo_restante(datos_json):
    if "token" in datos_json and "expira_en" in datos_json:
        token = datos_json["token"]
        expira_en = datos_json["expira_en"]

        # Calcular el tiempo restante antes de que caduque el token
        tiempo_restante = expira_en - time.time()

        # Imprimir el valor del token
        print("Valor del token:", token)

        # Imprimir el tiempo restante antes de que caduque el token
        print("Tiempo restante antes de que caduque el token:", tiempo_restante, "segundos")
    else:
        print("El archivo JSON no contiene la información necesaria.")

# Abrir el archivo JSON y cargarlo en un string llamado ourjson
ourjson = cargar_json_a_string(ruta_archivo_json)

# Verificar si se pudo cargar el archivo JSON correctamente
if ourjson is not None:
    imprimir_token_y_tiempo_restante(ourjson)
else:
    print("No se pudo cargar el archivo JSON.")


