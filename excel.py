import openpyxl
import pandas as pd

# Datos extraídos de tu archivo Python como ejemplo
datos_metro =  [
    # Línea 1 (Rojo)
    ('San Pablo', 'Neptuno', 'Rojo'),
    ('Neptuno', 'Pajaritos', 'Rojo'),
    ('Pajaritos', 'Las Rejas', 'Rojo'),
    ('Las Rejas', 'Ecuador', 'Rojo'),
    ('Ecuador', 'San Alberto Hurtado', 'Rojo'),
    ('San Alberto Hurtado', 'Universidad de Santiago', 'Rojo'),
    ('Universidad de Santiago', 'Estación Central', 'Rojo'),
    ('Estación Central', 'ULA', 'Rojo'),
    ('ULA', 'República', 'Rojo'),
    ('República', 'Los Héroes', 'Rojo'),
    ('Los Héroes', 'La Moneda', 'Rojo'),
    ('La Moneda', 'Universidad de Chile', 'Rojo'),
    ('Universidad de Chile', 'Santa Lucía', 'Rojo'),
    ('Santa Lucía', 'Universidad Católica', 'Rojo'),
    ('Universidad Católica', 'Baquedano', 'Rojo'),
    ('Baquedano', 'Salvador', 'Rojo'),
    ('Salvador', 'Manuel Montt', 'Rojo'),
    ('Manuel Montt', 'Pedro de Valdivia', 'Rojo'),
    ('Pedro de Valdivia', 'Los Leones', 'Rojo'),
    ('Los Leones', 'Tobalaba', 'Rojo'),
    ('Tobalaba', 'El Golf', 'Rojo'),
    ('El Golf', 'Alcántara', 'Rojo'),
    ('Alcántara', 'Escuela Militar', 'Rojo'),
    ('Escuela Militar', 'Manquehue', 'Rojo'),
    ('Manquehue', 'Hernando de Magallanes', 'Rojo'),
    ('Hernando de Magallanes', 'Los Dominicos', 'Rojo'),

    # Línea 2 (Amarillo)
    ('Vespucio Norte', 'Zapadores', 'Amarillo'),
    ('Zapadores', 'Dorsal', 'Amarillo'),
    ('Dorsal', 'Einstein', 'Amarillo'),
    ('Einstein', 'Cementerios', 'Amarillo'),
    ('Cementerios', 'Patronato', 'Amarillo'),
    ('Patronato', 'Puente Cal y Canto', 'Amarillo'),
    ('Puente Cal y Canto', 'Santa Ana', 'Amarillo'),
    ('Santa Ana', 'Los Héroes', 'Amarillo'),
    ('Los Héroes', 'Toesca', 'Amarillo'),
    ('Toesca', 'Parque O\'Higgins', 'Amarillo'),
    ('Parque O\'Higgins', 'Rondizzoni', 'Amarillo'),
    ('Rondizzoni', 'Franklin', 'Amarillo'),
    ('Franklin', 'El Llano', 'Amarillo'),
    ('El Llano', 'San Miguel', 'Amarillo'),
    ('San Miguel', 'Lo Vial', 'Amarillo'),
    ('Lo Vial', 'Departamental', 'Amarillo'),
    ('Departamental', 'Ciudad del Niño', 'Amarillo'),
    ('Ciudad del Niño', 'Lo Ovalle', 'Amarillo'),
    ('Lo Ovalle', 'El Parrón', 'Amarillo'),
    ('El Parrón', 'La Cisterna', 'Amarillo'),

    # Línea 3 (Café)
    ('Los Libertadores', 'Cardenal Caro', 'Café'),
    ('Cardenal Caro', 'Vivaceta', 'Café'),
    ('Vivaceta', 'Conchalí', 'Café'),
    ('Conchalí', 'Plaza Chacabuco', 'Café'),
    ('Plaza Chacabuco', 'Hospitales', 'Café'),
    ('Hospitales', 'Puente Cal y Canto', 'Café'),
    ('Puente Cal y Canto', 'Universidad de Chile', 'Café'),
    ('Universidad de Chile', 'Plaza de Armas', 'Café'),
    ('Plaza de Armas', 'Santa Isabel', 'Café'),
    ('Santa Isabel', 'Irarrázaval', 'Café'),
    ('Irarrázaval', 'Monseñor Eyzaguirre', 'Café'),
    ('Monseñor Eyzaguirre', 'Ñuñoa', 'Café'),
    ('Ñuñoa', 'Chile España', 'Café'),
    ('Chile España', 'Villa Frei', 'Café'),
    ('Villa Frei', 'Plaza Egaña', 'Café'),
    ('Plaza Egaña', 'Los Orientales', 'Café'),
    ('Los Orientales', 'Fernando Castillo Velasco', 'Café'),

    # Línea 4 (Azul)
    ('Tobalaba', 'Cristóbal Colón', 'Azul'),
    ('Cristóbal Colón', 'Francisco Bilbao', 'Azul'),
    ('Francisco Bilbao', 'Príncipe de Gales', 'Azul'),
    ('Príncipe de Gales', 'Simón Bolívar', 'Azul'),
    ('Simón Bolívar', 'Plaza Egaña', 'Azul'),
    ('Plaza Egaña', 'Los Presidentes', 'Azul'),
    ('Los Presidentes', 'Quilín', 'Azul'),
    ('Quilín', 'Las Torres', 'Azul'),
    ('Las Torres', 'Macul', 'Azul'),
    ('Macul', 'Vicuña Mackenna', 'Azul'),
    ('Vicuña Mackenna', 'Vicente Valdés', 'Azul'),
    ('Vicente Valdés', 'Rojas Magallanes', 'Azul'),
    ('Rojas Magallanes', 'Trinidad', 'Azul'),
    ('Trinidad', 'San José de la Estrella', 'Azul'),
    ('San José de la Estrella', 'Los Quillayes', 'Azul'),
    ('Los Quillayes', 'Elisa Correa', 'Azul'),
    ('Elisa Correa', 'Hospital Sótero del Río', 'Azul'),
    ('Hospital Sótero del Río', 'Protectora de la Infancia', 'Azul'),
    ('Protectora de la Infancia', 'Las Mercedes', 'Azul'),
    ('Las Mercedes', 'Plaza de Puente Alto', 'Azul'),

    # Línea 4A (Gris)
    ('Vicuña Mackenna', 'Santa Julia', 'Gris'),
    ('Santa Julia', 'La Granja', 'Gris'),
    ('La Granja', 'San Ramón', 'Gris'),
    ('San Ramón', 'Santa Rosa', 'Gris'),
    ('Santa Rosa', 'La Cisterna', 'Gris'),

    # Línea 5 (Verde)
    ('Plaza de Maipú', 'Santiago Bueras', 'Verde'),
    ('Santiago Bueras', 'Del Sol', 'Verde'),
    ('Del Sol', 'Monte Tabor', 'Verde'),
    ('Monte Tabor', 'Las Parcelas', 'Verde'),
    ('Las Parcelas', 'Laguna Sur', 'Verde'),
    ('Laguna Sur', 'Barrancas', 'Verde'),
    ('Barrancas', 'Pudahuel', 'Verde'),
    ('Pudahuel', 'Lo Prado', 'Verde'),
    ('Lo Prado', 'Blanqueado', 'Verde'),
    ('Blanqueado', 'Gruta de Lourdes', 'Verde'),
    ('Gruta de Lourdes', 'Quinta Normal', 'Verde'),
    ('Quinta Normal', 'Cumming', 'Verde'),
    ('Cumming', 'Santa Ana', 'Verde'),
    ('Santa Ana', 'Plaza de Armas', 'Verde'),
    ('Plaza de Armas', 'Bellas Artes', 'Verde'),
    ('Bellas Artes', 'Baquedano', 'Verde'),
    ('Baquedano', 'Parque Bustamante', 'Verde'),
    ('Parque Bustamante', 'Irarrázaval', 'Verde'),
    ('Irarrázaval', 'Santa Isabel', 'Verde'),
    ('Santa Isabel', 'Ñuble', 'Verde'),
    ('Ñuble', 'Rodrigo de Araya', 'Verde'),
    ('Rodrigo de Araya', 'Carlos Valdovinos', 'Verde'),
    ('Carlos Valdovinos', 'Camino Agrícola', 'Verde'),
    ('Camino Agrícola', 'San Joaquín', 'Verde'),
    ('San Joaquín', 'Pedrero', 'Verde'),
    ('Pedrero', 'Mirador', 'Verde'),
    ('Mirador', 'Bellavista de la Florida', 'Verde'),
    ('Bellavista de la Florida', 'Vicente Valdés', 'Verde'),

    # Línea 6 (Morado)
    ('Cerrillos', 'Lo Valledor', 'Morado'),
    ('Lo Valledor', 'Franklin', 'Morado'),
    ('Franklin', 'Biobío', 'Morado'),
    ('Biobío', 'Ñuble', 'Morado'),
    ('Ñuble', 'Estadio Nacional', 'Morado'),
    ('Estadio Nacional', 'Ñuñoa', 'Morado'),
    ('Ñuñoa', 'Inés de Suárez', 'Morado'),
    ('Inés de Suárez', 'Los Leones', 'Morado'),

]



# Crear un DataFrame con los datos
df = pd.DataFrame(datos_metro, columns=["Estación Origen", "Estación Destino", "Color"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("plantilla_metro.xlsx", index=False)

print("Archivo Excel generado exitosamente.")
