# 🗺️ Grafo del Metro de Santiago de Chile 🚇

Este proyecto consiste en la construcción de un **grafo** que representa las estaciones del **Metro de Santiago de Chile**, con el objetivo de encontrar la **ruta más corta** entre dos estaciones. Utiliza el **algoritmo de Dijkstra** para calcular el mejor camino y lo visualiza en un **mapa interactivo** a partir de las coordenadas geográficas de las estaciones.

---

## 📝 Descripción

El programa procesa una plantilla de **Excel** que contiene información detallada sobre las estaciones del metro, incluyendo:

- 🚉 **Estación de origen**
- 🚉 **Estación de destino**
- 🎨 **Color de la línea**
- 🔢 **Número de línea**
- 📏 **Longitud de la estación** (en metros)
- 🌐 **Coordenadas geográficas** (latitud y longitud)

### 📊 Ejemplo de los datos:

| Estación Origen  | Estación Destino  | Color | Línea | Longitud de Estación | Lat Origen | Long Origen | Lat Destino | Long Destino |
|------------------|-------------------|-------|-------|----------------------|------------|-------------|-------------|--------------|
| San Pablo        | Neptuno           | Rojo  | 1     | 690                  | -33.445367 | -70.723160  | -33.451554  | -70.722668   |
| Neptuno          | Pajaritos         | Rojo  | 1     | 1030                 | -33.451554 | -70.722668  | -33.456570  | -70.715493   |

---

## 🚀 Funcionalidades

1. **🔍 Cálculo del camino más corto**: Utilizando el **algoritmo de Dijkstra**, el programa calcula la ruta óptima entre una estación de origen y una de destino.

   - Ejemplo de ruta desde `Santiago Bueras` hasta `Plaza Egaña`:
     ```python
     source = 'Santiago Bueras'
     target = 'Plaza Egaña'
     djk_path = nx.dijkstra_path(METRO, source=source, target=target, weight=True)
     print(djk_path)
     ```

     **Resultado**:
     ```
     ['Santiago Bueras', 'Del Sol', 'Monte Tabor', ... , 'Plaza Egaña']
     ```

2. **🗺️ Visualización en Mapa**: El grafo generado se muestra en un mapa interactivo, utilizando las coordenadas geográficas de cada estación para la representación visual.

3. **🌐 Implementación Web**: El grafo ha sido integrado en una **página web** con **HTML, CSS y JavaScript**, permitiendo a los usuarios visualizar e interactuar con el mapa en tiempo real.

---

## 🛠️ Tecnologías Utilizadas

- **Python**: Para el procesamiento de los datos y la implementación del algoritmo de Dijkstra.
- **NetworkX**: Librería para la creación y manipulación del grafo.
- **HTML/CSS/JavaScript**: Desarrollo de la interfaz web interactiva.
- **Excel**: Contiene los datos de entrada de las estaciones.

---

## 📦 Instalación y Uso

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/skantos/metro-de-santiago-de-chile.git
2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt


