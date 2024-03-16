import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# Cargar el conjunto de datos generado por el scraper
data = pd.read_csv('tiendas_madrid.csv')

# Preprocesamiento de datos
# Codificar las etiquetas categóricas como números
le_tienda = LabelEncoder()
le_tipo = LabelEncoder()
data['Tienda'] = le_tienda.fit_transform(data['Tienda'])
data['Tipo de Tienda'] = le_tipo.fit_transform(data['Tipo de Tienda'])

# DataFrame 'compras_clientes' que contiene las compras de los clientes
# DataFrame con los datos de tus clientes
compras_clientes = pd.read_csv('compras_clientes.csv')

# Unir los DataFrames 'data' y 'compras_clientes' en base a una columna en común, por ejemplo 'Tienda'
df_merged = pd.merge(compras_clientes, data, on='Tienda')

# Dividir los datos en características y etiquetas
X = df_merged.drop(['Ubicación'], axis=1)  # Características
y = df_merged['Ubicación']  # Etiqueta

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_train, y_train)

# Hacer una predicción para un nuevo cliente
nuevo_cliente_compras = [datos_de_compras]  # Reemplaza con los datos reales del nuevo cliente
ubicacion_predicha = modelo.predict([nuevo_cliente_compras])

# Imprimir la ubicación predicha
print(f"Ubicación recomendada para comprar: {ubicacion_predicha}")
