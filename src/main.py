# Importamos la librería pandas para manejo de datos tabulares
import pandas as pd
import matplotlib.pyplot as plt

# Configuramos pandas para que imprima hasta 9999 filas completas si es necesario
pd.options.display.max_rows = 9999

# Leemos el archivo CSV con datos de ventas y lo guardamos en el DataFrame 'df'
df = pd.read_csv("C:\\Users\\jquiros\\Desktop\\POO\\pandas\\anailisis_de_datos_con_pandas_06_08_25\src\\ventas_practica.csv")

# Creamos un diccionario para convertir cantidades escritas como texto a números
texto_a_numero = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5
}

# Eliminamos filas con valores nulos y hacemos una copia del DataFrame limpio
new_df = df.dropna().copy()

# Normalizamos el texto de la columna "Pago" para que empiece en mayúscula (Ej: "efectivo" → "Efectivo")
new_df["Pago"] = new_df["Pago"].str.capitalize()

# Unificamos el formato de la fecha cambiando '/' por '-' (Ej: "2024/01/01" → "2024-01-01")
new_df["Fecha"] = new_df["Fecha"].str.replace("/", "-", regex=False)

# Convertimos la columna "Fecha" a tipo datetime; si hay errores se ponen como NaT (valor nulo para fechas)
new_df["Fecha"] = pd.to_datetime(new_df["Fecha"], errors='coerce')

# Ordenamos las filas por la columna "Fecha" de forma ascendente
new_df = new_df.sort_values(by="Fecha", ascending=True)

# Reemplazamos los textos como "dos" por sus equivalentes numéricos en la columna "Cantidad"
new_df["Cantidad"] = new_df["Cantidad"].replace(texto_a_numero)

# Convertimos la columna "Cantidad" a tipo numérico; si algún valor no es convertible, se convierte en NaN
new_df["Cantidad"] = pd.to_numeric(new_df["Cantidad"], errors='coerce')

# Creamos un DataFrame con solo las filas en las que el método de pago fue "Tarjeta"
df_tarjeta = new_df[new_df["Pago"] == "Tarjeta"]

# Creamos un DataFrame con solo las filas en las que el método de pago fue "Transferencia"
df_Transferencia = new_df[new_df["Pago"] == "Transferencia"]

# Imprimimos todo el DataFrame limpio
print(new_df)

# Imprimimos el DataFrame filtrado por pagos con tarjeta
print("DataFrame de Tarjeta:")
print(df_tarjeta)

# Imprimimos el DataFrame filtrado por pagos con transferencia
print("DataFrame de Transferencia:")
print(df_Transferencia)

# Sumamos los valores de la columna "Precio" para los pagos hechos con tarjeta
suma_precio_tarjeta = df_tarjeta['Precio'].sum()
print("Suma del precio en Tarjeta:", suma_precio_tarjeta)

# Sumamos los valores de la columna "Precio" para los pagos hechos con transferencia
suma_precio_transferencia = df_Transferencia['Precio'].sum()
print("Suma del precio en Transferencia:", suma_precio_transferencia)

# Agrupamos los pagos con tarjeta por producto y sumamos los precios; ordenamos de mayor a menor
ventas_por_producto_tarjeta = df_tarjeta.groupby('Producto')['Precio'].sum().sort_values(ascending=False).reset_index()
print("Ventas por producto en Tarjeta:")
print(ventas_por_producto_tarjeta)

# Agrupamos los pagos con transferencia por producto y sumamos los precios; ordenamos de mayor a menor
ventas_por_producto_transferencia = df_Transferencia.groupby('Producto')['Precio'].sum().sort_values(ascending=False).reset_index()
print("Ventas por producto en Transferencia:")
print(ventas_por_producto_transferencia)

# Obtenemos el producto con mayor venta por tarjeta (primer fila del DataFrame ordenado)
producto_mas_vendido_tarjeta = ventas_por_producto_tarjeta.iloc[0]
print("Producto más vendido en Tarjeta:", producto_mas_vendido_tarjeta['Producto'], "con ventas de", producto_mas_vendido_tarjeta['Precio'])

# Obtenemos el producto con mayor venta por transferencia (primer fila del DataFrame ordenado)
producto_mas_vendido_transferencia = ventas_por_producto_transferencia.iloc[0]
print("Producto más vendido en Transferencia:", producto_mas_vendido_transferencia['Producto'], "con ventas de", producto_mas_vendido_transferencia['Precio'])
# Imprimimos el DataFrame final con todas las modificaciones
print("DataFrame final:")
print(new_df)

total_ventas= new_df["Precio"].sum()
print(f"El total de ventas es  {total_ventas}")

ventas_por_cliente= new_df.groupby("Cliente")['Precio'].sum().sort_values(ascending=False).reset_index()

print(f"El total de ventas es por cliente  {ventas_por_cliente}")
cliente_con_mas_ventas= ventas_por_cliente.iloc[0]

print(f"el cliente con mas ventas es {cliente_con_mas_ventas['Cliente']} , por ventas de {cliente_con_mas_ventas['Precio']}")

cantidad_por_producto= new_df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False)
print(f"cantidad total por peoducto: {cantidad_por_producto}")
producto_mas_vendido= cantidad_por_producto.index[0]

print(f'producto mas vendido {producto_mas_vendido}')

#Pago mas utilizado
metodo_mas_utilizado= new_df['Pago'].value_counts().idxmax()
print(f"El metodo mas utilizado fue {metodo_mas_utilizado}")


promedio_ventas= round(new_df["Precio"].mean(),0)
print(f'El promedio de ventas fue {promedio_ventas:.0f}')

promedio_cantidad= new_df["Cantidad"].mean()
print(f'El promedio de cantidades fue {promedio_cantidad: .0f}')

total_ventas_por_pago= new_df["Pago"].value_counts()
print('Cantidad por forma de pago')
print(total_ventas_por_pago)



print('---------------------')
ventas_por_producto= new_df.groupby('Producto')['Precio'].sum().sort_values(ascending=False).reset_index()
print(f'Ventas por producto {ventas_por_producto}')

new_df['Total a Pagar']= new_df["Cantidad"]* new_df["Precio"]
print(new_df)

ventas_por_producto_tarjeta.plot(kind= 'bar', title= 'ventas por producto tarjeta', ylabel= 'Precio')
plt.tight_layout()
plt.show()

ventas_por_producto.plot(kind='bar', title= 'Ventas por producto', ylabel='Precio')
plt.tight_layout()
plt.show()

