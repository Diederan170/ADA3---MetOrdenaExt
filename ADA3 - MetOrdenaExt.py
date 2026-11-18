def ordenamiento_intercalacion(lista_a, lista_b):
    """
    Combina dos listas previamente ordenadas (lista_a y lista_b)
    en una sola lista ordenada mediante el método de Intercalación.
    """
    i, j = 0, 0
    resultado = []
    paso = 1

    print(f"\nLista Ordenada A (Sucursal Norte): {lista_a}")
    print(f"Lista Ordenada B (Sucursal Sur):   {lista_b}\n")

    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            resultado.append(lista_a[i])
            print(f"Paso {paso}: Se toma {lista_a[i]} de Lista A -> {resultado}")
            i += 1
        else:
            resultado.append(lista_b[j])
            print(f"Paso {paso}: Se toma {lista_b[j]} de Lista B -> {resultado}")
            j += 1
        paso += 1

    while i < len(lista_a):
        resultado.append(lista_a[i])
        print(f"Paso {paso}: Se agrega restante {lista_a[i]} de Lista A -> {resultado}")
        i += 1
        paso += 1

    while j < len(lista_b):
        resultado.append(lista_b[j])
        print(f"Paso {paso}: Se agrega restante {lista_b[j]} de Lista B -> {resultado}")
        j += 1
        paso += 1

    return resultado


def ordenamiento_mezcla_directa(lista):
    """
    Ordena una lista utilizando el método de Mezcla Directa,
    repartiendo en bloques de tamaño fijo (1, 2, 4, 8...) en dos
    listas auxiliares (F1 y F2) y fusionándolos en cada pasada.
    """
    datos = lista.copy()
    n = len(datos)
    tamano_bloque = 1
    pasada = 1

    print(f"\nLista inicial desordenada: {datos}\n")

    while tamano_bloque < n:
        f1 = []
        f2 = []
        indice = 0
        enviar_a_f1 = True

        while indice < n:
            bloque = datos[indice:indice + tamano_bloque]
            if enviar_a_f1:
                f1.extend(bloque)
            else:
                f2.extend(bloque)
            enviar_a_f1 = not enviar_a_f1
            indice += tamano_bloque

        print(f"--- Pasada {pasada} (tamaño de bloque = {tamano_bloque}) ---")
        print(f"  Auxiliar F1: {f1}")
        print(f"  Auxiliar F2: {f2}")

        fusionada = []
        idx1, idx2 = 0, 0
        while idx1 < len(f1) or idx2 < len(f2):
            fin1 = min(idx1 + tamano_bloque, len(f1))
            fin2 = min(idx2 + tamano_bloque, len(f2))

            while idx1 < fin1 and idx2 < fin2:
                if f1[idx1] <= f2[idx2]:
                    fusionada.append(f1[idx1])
                    idx1 += 1
                else:
                    fusionada.append(f2[idx2])
                    idx2 += 1

            while idx1 < fin1:
                fusionada.append(f1[idx1])
                idx1 += 1

            while idx2 < fin2:
                fusionada.append(f2[idx2])
                idx2 += 1

        datos = fusionada
        print(f"  Resultado tras fusionar: {datos}\n")
        tamano_bloque *= 2
        pasada += 1

    return datos


def obtener_tramos_naturales(arr):
    """Detecta las secuencias (tramos) que ya están ordenadas de forma natural."""
    if not arr:
        return []
    tramos = []
    tramo_actual = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            tramo_actual.append(arr[i])
        else:
            tramos.append(tramo_actual)
            tramo_actual = [arr[i]]
    tramos.append(tramo_actual)
    return tramos


def ordenamiento_mezcla_equilibrada(lista):
    """
    Ordena una lista utilizando el método de Mezcla Equilibrada Natural,
    detectando tramos ya ordenados, repartiéndolos en F1 y F2 y fusionándolos
    hasta obtener un único tramo ordenado.
    """
    datos = lista.copy()
    pasada = 1

    print(f"\nLista inicial desordenada: {datos}\n")

    while True:
        tramos = obtener_tramos_naturales(datos)
        print(f"--- Pasada {pasada} ---")
        print(f"  Tramos naturales detectados ({len(tramos)}): {tramos}")

        if len(tramos) <= 1:
            print("  -> Solo queda 1 tramo: la lista ya está completamente ordenada.\n")
            break

        f1_tramos = []
        f2_tramos = []
        for idx, tramo in enumerate(tramos):
            if idx % 2 == 0:
                f1_tramos.append(tramo)
            else:
                f2_tramos.append(tramo)

        print(f"  Auxiliar F1 (tramos): {f1_tramos}")
        print(f"  Auxiliar F2 (tramos): {f2_tramos}")

        nueva_lista = []
        max_pares = max(len(f1_tramos), len(f2_tramos))
        for k in range(max_pares):
            t1 = f1_tramos[k] if k < len(f1_tramos) else []
            t2 = f2_tramos[k] if k < len(f2_tramos) else []

            i, j = 0, 0
            while i < len(t1) and j < len(t2):
                if t1[i] <= t2[j]:
                    nueva_lista.append(t1[i])
                    i += 1
                else:
                    nueva_lista.append(t2[j])
                    j += 1
            nueva_lista.extend(t1[i:])
            nueva_lista.extend(t2[j:])

        datos = nueva_lista
        print(f"  Resultado tras fusionar tramos: {datos}\n")
        pasada += 1

    return datos


def solicitar_cantidad(mensaje, minimo=2):
    """Solicita y valida la cantidad de elementos a ingresar."""
    while True:
        entrada = input(mensaje).strip()
        try:
            cantidad = int(entrada)
            if cantidad >= minimo:
                return cantidad
            print(f"Error: Debes ingresar un número entero mayor o igual a {minimo}.")
        except ValueError:
            print("Error: Entrada no válida. Escribe únicamente un número entero.")


def capturar_lista_positivos(nombre_lista="la lista", exigir_orden=False):
    """
    Solicita los números al usuario verificando que sean positivos (> 0).
    Si exigir_orden=True, verifica que cada número sea >= al anterior.
    """
    minimo = 1 if exigir_orden else 2
    cantidad = solicitar_cantidad(
        f"\n¿Cuántos números deseas ingresar para {nombre_lista}? (mínimo {minimo}): ",
        minimo=minimo
    )
    numeros = []

    for i in range(cantidad):
        while True:
            aviso_orden = ""
            if exigir_orden and numeros:
                aviso_orden = f" (debe ser >= {numeros[-1]})"
            entrada = input(f"Ingresa el número #{i + 1}{aviso_orden}: ").strip()
            try:
                valor = float(entrada)
                if valor <= 0:
                    print("Error: El valor debe ser mayor a 0 (no se aceptan negativos ni cero).")
                    continue
                valor_limpio = int(valor) if valor.is_integer() else valor
                if exigir_orden and numeros and valor_limpio < numeros[-1]:
                    print(f"Error: Para Intercalación la lista debe estar ordenada (ingresa un número >= {numeros[-1]}).")
                    continue
                numeros.append(valor_limpio)
                break
            except ValueError:
                print("Error: Entrada no válida. Ingresa un valor numérico.")

    return numeros


def mostrar_instrucciones(titulo, descripcion, permitidos, no_permitidos):
    """Muestra las reglas claras sobre qué datos puede y no puede ingresar el usuario."""
    print("\n" + "=" * 68)
    print(f" {titulo}")
    print("=" * 68)
    print(f"Contexto: {descripcion}")
    print("\nINSTRUCCIONES DE CAPTURA DE DATOS:")
    print(f"  [+] SÍ puedes ingresar: {permitidos}")
    print(f"  [-] NO puedes ingresar: {no_permitidos}")
    print("-" * 68)


def menu_principal():
    """Controla el menú interactivo hasta que el usuario decida salir."""
    while True:
        print("\n" + "#" * 68)
        print("    SISTEMA INTERACTIVO DE MÉTODOS DE ORDENAMIENTO EXTERNO")
        print("#" * 68)
        print("1. Ejercicio 1 - Intercalación      (Ventas de dos sucursales)")
        print("2. Ejercicio 2 - Mezcla Directa     (Consumos eléctricos en kWh)")
        print("3. Ejercicio 3 - Mezcla Equilibrada (Tiempos de llegada en carrera)")
        print("4. Salir del programa")
        print("#" * 68)

        opcion = input("Selecciona el ejercicio que deseas ejecutar (1-4): ").strip()

        if opcion == "1":
            mostrar_instrucciones(
                titulo="EJERCICIO 1: INTERCALACIÓN - VENTAS DE DOS SUCURSALES",
                descripcion="Une dos listas ya ordenadas de ventas en un único reporte ordenado.",
                permitidos="Números enteros o decimales positivos mayores a 0, ingresados de menor a mayor en cada sucursal.",
                no_permitidos="Números negativos, el número 0, letras, símbolos o números desordenados dentro de la misma lista."
            )
            lista_a = capturar_lista_positivos("Sucursal Norte (Lista A)", exigir_orden=True)
            lista_b = capturar_lista_positivos("Sucursal Sur (Lista B)", exigir_orden=True)
            resultado = ordenamiento_intercalacion(lista_a, lista_b)
            print(f"\n>>> Reporte final intercalado (Intercalación): {resultado}")

        elif opcion == "2":
            mostrar_instrucciones(
                titulo="EJERCICIO 2: MEZCLA DIRECTA - CONSUMOS ELÉCTRICOS (kWh)",
                descripcion="Ordena lecturas de medidores dividiendo en bloques de tamaño fijo en F1 y F2.",
                permitidos="Números enteros o decimales positivos mayores a 0 en cualquier orden (ej. 145, 82.5, 310).",
                no_permitidos="Números negativos, el número 0, letras o caracteres especiales."
            )
            datos = capturar_lista_positivos("los medidores", exigir_orden=False)
            resultado = ordenamiento_mezcla_directa(datos)
            print(f">>> Consumos finales ordenados (Mezcla Directa): {resultado}")

        elif opcion == "3":
            mostrar_instrucciones(
                titulo="EJERCICIO 3: MEZCLA EQUILIBRADA - TIEMPOS DE CARRERA (seg)",
                descripcion="Detecta tramos ya ordenados de forma natural y los fusiona usando F1 y F2.",
                permitidos="Números enteros o decimales positivos mayores a 0 en cualquier orden (ej. 54.2, 61, 49.8).",
                no_permitidos="Números negativos, el número 0, letras o espacios vacíos."
            )
            datos = capturar_lista_positivos("los corredores", exigir_orden=False)
            resultado = ordenamiento_mezcla_equilibrada(datos)
            print(f">>> Tiempos finales ordenados (Mezcla Equilibrada): {resultado}")

        elif opcion == "4":
            print("\nPrograma finalizado por el usuario. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 4.")


if __name__ == "__main__":
    menu_principal()