def bubble_sort(arr):
    n = len(arr)
    # Recorremos todos los elementos del arreglo
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Intercambiamos si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Simulación de un problema real:
# Un negocio recibe pedidos con distintos tiempos de entrega estimados (en días).
# Se desea ordenarlos de menor a mayor para planificar las entregas.

print("----- PLANIFICADOR DE ENTREGAS -----")
entrada = input("Ingrese los tiempos estimados de entrega separados por coma (ej: 5,2,8,1,3): ")
# Convertimos la entrada en una lista de enteros
tiempos = [int(x.strip()) for x in entrada.split(',')]

print("\nTiempos de entrega recibidos:", tiempos)

# Ordenamos usando bubble sort
tiempos_ordenados = bubble_sort(tiempos.copy())

print("Tiempos de entrega ordenados:", tiempos_ordenados)

# Mostramos una planificación sencilla
print("\nPLAN DE ENTREGAS:")
for i, tiempo in enumerate(tiempos_ordenados, start=1):
    print(f"Día {i}: Entrega con tiempo estimado de {tiempo} días")
