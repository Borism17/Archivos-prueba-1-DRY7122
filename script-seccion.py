# Función para solicitar información al usuario
def solicitar_informacion():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    codigo_seccion = input("Ingrese su código de sección (por ejemplo, DRY7122-003V): ")
    sede = input("Ingrese su sede: ")
    return nombre, apellido, codigo_seccion, sede

# Función para validar la sección del alumno
def validar_seccion(codigo_seccion):
    seccion_valida = "DRY7122-003V"
    if codigo_seccion == seccion_valida:
        return True
    else:
        return False

# Función para imprimir la información del alumno
def imprimir_informacion(nombre, apellido, codigo_seccion, sede):
    print("\nInformación del alumno:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Código de Sección:", codigo_seccion)
    print("Sede:", sede)

# Función principal
def main():
    # Solicitar información al usuario
    nombre, apellido, codigo_seccion, sede = solicitar_informacion()

    # Validar la sección del alumno
    if validar_seccion(codigo_seccion):
        # Si la sección es válida, imprimir la información del alumno
        imprimir_informacion(nombre, apellido, codigo_seccion, sede)
    else:
        # Si la sección no es válida, imprimir un mensaje de error
        print("\n¡Error! El código de sección ingresado no es válido.")

# Llamar a la función principal
main()

