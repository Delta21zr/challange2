import pandas as pd
import requests
import matplotlib.pyplot as plt

# URL del archivo JSON en GitHub
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"

# Obtener los datos desde la API
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data)
    print("Datos cargados correctamente.\n")
else:
    print(f"Error al cargar los datos: {response.status_code}")
    exit()

# Mostrar las primeras filas
print("Primeras filas del DataFrame:")
print(df.head(), "\n")

# Información general del DataFrame
print("Información del DataFrame:")
print(df.info(), "\n")

# Estadísticas descriptivas de las columnas numéricas
print("Estadísticas descriptivas:")
print(df.describe(), "\n")

# -----------------------------
# Análisis de evasión de clientes
# -----------------------------
clientes_evasion = df[df['Churn'] == 'Yes']
clientes_no_evasion = df[df['Churn'] == 'No']

print(f"Cantidad de clientes en evasión: {clientes_evasion.shape[0]}")
print(f"Cantidad de clientes sin evasión: {clientes_no_evasion.shape[0]}\n")

# -----------------------------
# Distribución por tipo de servicio
# -----------------------------
distribucion_servicio = df['internet.InternetService'].value_counts()
print("Distribución de clientes por tipo de servicio de internet:")
print(distribucion_servicio)

# Mostrar todas las columnas y sus tipos
print("Columnas del dataset:")
print(df.columns.tolist(), "\n")

print("Tipos de datos de cada columna:")
print(df.dtypes, "\n")

# -----------------------------
# Revisar valores ausentes y duplicados
# -----------------------------
print("Valores ausentes por columna:")
print(df.isnull().sum(), "\n")

duplicados = df.duplicated().sum()
print(f"Cantidad de filas duplicadas: {duplicados}\n")

# -----------------------------
# Revisar y corregir formatos de columnas numéricas
# -----------------------------
print("Tipo de dato de account.Charges.Total:", df['account.Charges.Total'].dtype)
df['account.Charges.Total'] = pd.to_numeric(df['account.Charges.Total'], errors='coerce')
print("Valores ausentes en account.Charges.Total tras conversión:",
      df['account.Charges.Total'].isnull().sum(), "\n")

# -----------------------------
# Revisar inconsistencias en columnas categóricas
# -----------------------------
columnas_categoricas = df.select_dtypes(include='object').columns.tolist()
for col in columnas_categoricas:
    print(f"Valores únicos en '{col}': {df[col].unique()}\n")

# -----------------------------
# Eliminar duplicados
# -----------------------------
filas_antes = df.shape[0]
df = df.drop_duplicates()
filas_despues = df.shape[0]
print(f"Se eliminaron {filas_antes - filas_despues} filas duplicadas.\n")

# -----------------------------
# Rellenar valores faltantes en columnas numéricas
# -----------------------------
df['account.Charges.Monthly'].fillna(df['account.Charges.Monthly'].median(), inplace=True)
df['account.Charges.Total'].fillna(df['account.Charges.Monthly'] * df['customer.tenure'], inplace=True)

# -----------------------------
# Rellenar valores faltantes en columnas categóricas
# -----------------------------
for col in columnas_categoricas:
    nulos = df[col].isnull().sum()
    if nulos > 0:
        df[col].fillna('Desconocido', inplace=True)
        print(f"Se rellenaron {nulos} valores nulos en '{col}' con 'Desconocido'.")

# -----------------------------
# Normalizar valores de categorías
# -----------------------------
df['Churn'] = df['Churn'].str.strip().str.capitalize()
df['Churn'] = df['Churn'].replace({'Si': 'Yes', 'No ': 'No'})
for col in columnas_categoricas:
    df[col] = df[col].str.strip()

# -----------------------------
# Verificación final de limpieza
# -----------------------------
print("Valores ausentes por columna después de la limpieza:")
print(df.isnull().sum(), "\n")
print("Filas y columnas finales del DataFrame:", df.shape)

# -----------------------------
# Crear columna de facturación diaria
# -----------------------------
df['Cuentas_Diarias'] = df['account.Charges.Monthly'] / 30
print("Primeras filas con la nueva columna 'Cuentas_Diarias':")
print(df[['customerID', 'account.Charges.Monthly', 'Cuentas_Diarias']].head(), "\n")
print("Estadísticas descriptivas de 'Cuentas_Diarias':")
print(df['Cuentas_Diarias'].describe(), "\n")

# -----------------------------
# Transformar variables categóricas a binarias
# -----------------------------
df['Churn_Binario'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['Partner_Binario'] = df['customer.Partner'].map({'Yes': 1, 'No': 0})
df['Dependents_Binario'] = df['customer.Dependents'].map({'Yes': 1, 'No': 0})
df['PhoneService_Binario'] = df['phone.PhoneService'].map({'Yes': 1, 'No': 0})
df['PaperlessBilling_Binario'] = df['account.PaperlessBilling'].map({'Yes': 1, 'No': 0})

# -----------------------------
# Renombrar columnas para mayor claridad
# -----------------------------
df.rename(columns={
    'customer.gender': 'Genero',
    'customer.SeniorCitizen': 'Mayor_60',
    'customer.tenure': 'Meses_Contrato',
    'internet.InternetService': 'Servicio_Internet',
    'account.Charges.Monthly': 'Cobro_Mensual',
    'account.Charges.Total': 'Cobro_Total'
}, inplace=True)

print("Primeras filas tras estandarización y transformación:")
print(df.head())
print("\nTipos de datos tras transformación:")
print(df.dtypes)

# -----------------------------
# Análisis descriptivo
# -----------------------------
print("Estadísticas descriptivas de columnas numéricas:")
print(df.describe(), "\n")
print("Medianas de las columnas numéricas:")
print(df.median(numeric_only=True), "\n")
print("Desviación estándar de las columnas numéricas:")
print(df.std(numeric_only=True), "\n")

# -----------------------------
# Distribución de variables categóricas
# -----------------------------
columnas_categoricas = df.select_dtypes(include='object').columns.tolist()
for col in columnas_categoricas:
    print(f"Distribución de '{col}':")
    print(df[col].value_counts(), "\n")

# -----------------------------
# Análisis de la variable Churn
# -----------------------------
total_clientes = df.shape[0]
clientes_evasion = df['Churn_Binario'].sum()
clientes_no_evasion = total_clientes - clientes_evasion
print(f"Total de clientes: {total_clientes}")
print(f"Clientes en evasión: {clientes_evasion} ({clientes_evasion/total_clientes:.2%})")
print(f"Clientes sin evasión: {clientes_no_evasion} ({clientes_no_evasion/total_clientes:.2%})\n")

# -----------------------------
# Visualización de Churn
# -----------------------------
labels = ['Permanecieron', 'Abandonaron']
valores = [clientes_no_evasion, clientes_evasion]
colores = ['#4CAF50', '#F44336']

plt.figure(figsize=(6,4))
plt.bar(labels, valores, color=colores)
plt.title('Distribución de Churn (evasión de clientes)')
plt.ylabel('Cantidad de clientes')
plt.show()

plt.figure(figsize=(6,6))
plt.pie(valores, labels=labels, autopct='%1.1f%%', colors=colores, startangle=90, shadow=True)
plt.title('Proporción de clientes que permanecieron y abandonaron')
plt.show()

# -----------------------------
# Churn según variables categóricas
# -----------------------------
categoricas = [
    'Genero', 
    'customer.Partner', 
    'customer.Dependents', 
    'Servicio_Internet', 
    'account.Contract', 
    'account.PaymentMethod'
]

def grafico_churn_por_categoria(columna):
    tabla = pd.crosstab(df[columna], df['Churn_Binario'])
    tabla.columns = ['Permanecieron', 'Abandonaron']
    tabla.plot(kind='bar', stacked=True, figsize=(8,5), color=['#4CAF50','#F44336'])
    plt.title(f'Evasión según {columna}')
    plt.ylabel('Cantidad de clientes')
    plt.xlabel(columna)
    plt.xticks(rotation=45)
    plt.legend(title='Estado')
    plt.show()

for col in categoricas:
    grafico_churn_por_categoria(col)

# -----------------------------
# Distribución de variables numéricas según Churn
# -----------------------------
numericas = [
    'Meses_Contrato',      
    'Cobro_Mensual',       
    'Cuentas_Diarias'      
]

def grafico_numericas_por_churn(columna):
    plt.figure(figsize=(8,5))
    df[df['Churn_Binario'] == 0][columna].hist(bins=30, alpha=0.6, color='#4CAF50', label='Permanecieron')
    df[df['Churn_Binario'] == 1][columna].hist(bins=30, alpha=0.6, color='#F44336', label='Abandonaron')
    plt.title(f'Distribución de {columna} según Churn')
    plt.xlabel(columna)
    plt.ylabel('Cantidad de clientes')
    plt.legend()
    plt.show()

for col in numericas:
    grafico_numericas_por_churn(col)
