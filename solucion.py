# Inicialización de variables
reporte_jugadores = "Listado de Jugadores\n"
reporte_edades = "Listado de Edades\n"
suma_edades = 0
suma_estaturas = 0
contador = 0  # Contador para numeración de jugadores
bandera = True

# Bucle para ingreso de datos
while bandera:
    print("\nIngrese la información del jugador:")
    nombre = input("Nombre del jugador: ")
    posicion = input("Posición en el campo de juego: ")
    edad = input("Edad del jugador: ")
    edad = int(edad)
    estatura = input("Estatura del jugador (en metros): ")
    estatura = float(estatura)

    # Acumulación de datos en cadenas
    contador = contador + 1
    reporte_jugadores = f"{reporte_jugadores}{contador}. {nombre} -{posicion}, edad {edad}, estatura {estatura:.2f}\n"
    reporte_edades = f"{reporte_edades}{edad}\n"
    
    # Acumulación de sumas para promedio
    suma_edades = suma_edades + edad
    suma_estaturas = suma_estaturas + estatura

    # Preguntar al usuario si desea continuar
    continuar = input("¿Desea ingresar otro jugador? (Sí/No): ")
    if continuar != "si":
        bandera = False

# Cálculo de promedios
if contador > 0:
    promedio_edades = suma_edades / contador
    promedio_estaturas = suma_estaturas / contador
else:
    promedio_edades = 0
    promedio_estaturas = 0

# Impresión del reporte final
print(reporte_jugadores)
print(reporte_edades)
print(f"Promedio de edades: {promedio_edades:.1f}")
print(f"Promedio de estaturas: {promedio_estaturas:.2f}")
