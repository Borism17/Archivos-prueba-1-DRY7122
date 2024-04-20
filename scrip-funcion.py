# Función para determinar el tipo de lista de control de acceso (ACL)
def determinar_tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Estándar Layer 3"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida Layer 3"
    elif numero_acl >= 1000 and numero_acl <= 1099:
        return "ACL Estándar Layer 2"
    elif numero_acl >= 1100 and numero_acl <= 1199:
        return "ACL Extendida Layer 2"
    else:
        return "El número de ACL no corresponde a una lista de control de acceso."

# Función principal del script
def main():
    # Solicitar al usuario el número de ACL IPv4
    numero_acl = int(input("Ingrese el número de ACL IPv4: "))

    # Determinar el tipo de ACL y mostrar el resultado
    tipo_acl = determinar_tipo_acl(numero_acl)
    print("Tipo de ACL:", tipo_acl)

# Llamar a la función principal
main()

