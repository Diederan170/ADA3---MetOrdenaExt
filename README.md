[readme_m_todos_de_ordenamiento_externo.md](https://github.com/user-attachments/files/35051011/readme_m_todos_de_ordenamiento_externo.md)
# Métodos de Ordenamiento Externo en Python

Programa interactivo con menú de opciones que integra tres ejercicios de ordenamiento basados en dividir y fusionar listas auxiliares (`metodos_ordenamiento_externo.py`). Antes de capturar los valores, indica las reglas de entrada permitidas y muestra el avance de cada pasada en consola.

## Ejercicios incluidos

1. **Intercalación – Ventas de dos sucursales:** Combina dos listas de ventas que ya vienen ordenadas de menor a mayor para generar un único reporte general ordenado en una sola pasada.
2. **Mezcla Directa – Consumos eléctricos (kWh):** Ordena lecturas desordenadas repartiéndolas en bloques de tamaño fijo (`1, 2, 4, 8...`) entre dos listas auxiliares (`F1` y `F2`) y fusionándolas en cada vuelta.
3. **Mezcla Equilibrada – Tiempos de carrera:** Detecta automáticamente los grupos de tiempos que ya vienen ordenados de forma natural, los reparte entre `F1` y `F2` y los une hasta obtener la lista final ordenada.

## Requisitos
* Tener instalado **Python 3**.

## Cómo ejecutarlo
1. Abre una terminal en la carpeta donde guardaste el archivo `metodos_ordenamiento_externo.py`.
2. Ejecuta el comando:
   ```bash
   python metodos_ordenamiento_externo.py
   ```
3. Elige en el menú el método que deseas ejecutar (opciones `1` a `3`), revisa las instrucciones sobre los datos permitidos e ingresa los números solicitados. Para cerrar el programa, selecciona la opción `4`.
