# Grafo del Metro de Santiago de Chile

Este proyecto consiste en la construcción de un grafo que representa las estaciones del metro de Santiago de Chile, con el objetivo de encontrar la ruta más corta entre dos estaciones basándose en la distancia. Utiliza un algoritmo de Dijkstra para calcular el mejor camino y lo grafica en un mapa a partir de las coordenadas geográficas.

## Descripción

El programa procesa una plantilla de Excel que contiene la información de las estaciones del metro de Santiago, incluyendo:

- Estación de origen
- Estación de destino
- Color de la línea
- Número de línea
- Longitud de la estación (en metros)
- Coordenadas geográficas (latitud y longitud)

### Ejemplo de datos:

| Estación Origen  | Estación Destino  | Color | Línea | Longitud de Estación | Lat Origen | Long Origen | Lat Destino | Long Destino |
|------------------|-------------------|-------|-------|----------------------|------------|-------------|-------------|--------------|
| San Pablo        | Neptuno           | Rojo  | 1     | 690                  | -33.445367 | -70.723160  | -33.451554  | -70.722668   |
| Neptuno          | Pajaritos         | Rojo  | 1     | 1030                 | -33.451554 | -70.722668  | -33.456570  | -70.715493   |

## Funcionalidad

1. **Cálculo del camino más corto**: Usando el algoritmo de Dijkstra, se calcula la ruta más corta entre una estación de origen y una de destino. 
   - Ejemplo: Ruta desde `Santiago Bueras` hasta `Plaza Egaña`:
     ```python
     source = 'Santiago Bueras'
     target = 'Plaza Egaña'
     djk_path = nx.dijkstra_path(METRO, source=source, target=target, weight=True)
     print(djk_path)
     ```

     Resultado:
     ```
     ['Santiago Bueras', 'Del Sol', 'Monte Tabor', ... , 'Plaza Egaña']
     ```

2. **Visualización**: El grafo generado se visualiza en un mapa utilizando las coordenadas geográficas de cada estación.

3. **Implementación web**: El grafo se ha integrado en una página web mediante HTML, CSS y JavaScript para que los usuarios puedan interactuar con él en tiempo real.

## Tecnologías utilizadas

- **Python**: Para el procesamiento de datos y la implementación del algoritmo de Dijkstra.
- **NetworkX**: Librería utilizada para la creación y manipulación del grafo.
- **Matplotlib**: Para la visualización gráfica del grafo.
- **HTML/CSS/JavaScript**: Implementación de una interfaz web para visualizar y manipular el grafo.
- **Excel**: Archivo de entrada con los datos de las estaciones del metro.

## Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/skantos/metro-de-santiago-de-chile


1. Clona el repositorio:
   ```bash
   git clone https://github.com/skantos/metro-de-santiago-de-chile.git

