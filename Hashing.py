def bucket_sort(lista, num_buckets):
    if not lista:
        return lista


    min_val, max_val = min(lista), max(lista)
    intervalo = (max_val - min_val + 1) / num_buckets


    # Crear cubetas vacías
    buckets = [[] for _ in range(num_buckets)]
   
    # Distribuir valores en cubetas por rango
    for n in lista:
        # Asegurar que el mayor valor caiga en la última cubeta
        idx = int((n - min_val) / intervalo)
        if idx == num_buckets:  
            idx -= 1
        buckets[idx].append(n)
   
    # Ordenar e ir concatenando
    resultado = []
    for b in buckets:
        resultado.extend(sorted(b))
    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    lista = [29, 25, 3, 49, 9, 37, 21, 43]
    ordenada = bucket_sort(lista, num_buckets=5)
    print("Original:", lista)
    print("Ordenada:", ordenada)