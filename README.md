Descripción del proyecto

Este proyecto tiene como objetivo analizar los datos de clientes de la empresa ficticia Telecom X para identificar patrones de evasión de clientes (Churn). A través de este análisis, se busca comprender qué factores influyen en que un cliente abandone el servicio y obtener insights que puedan apoyar decisiones estratégicas para reducir la evasión.

Se utilizan datos en formato JSON proporcionados por la API de Telecom X y se realiza un análisis completo utilizando Python y Pandas.

Contenido del proyecto

challange2.py: Script principal que realiza:

Carga de datos desde la API.

Limpieza y transformación de los datos.

Creación de nuevas variables, como la facturación diaria.

Transformación de variables categóricas a valores binarios.

Análisis descriptivo y exploratorio de la evasión.

Visualización de la distribución de Churn y su relación con variables categóricas y numéricas.

Requisitos

Python 3.8 o superior

Librerías necesarias:

pandas

requests

matplotlib

Instalación de librerías:

pip install pandas requests matplotlib

Estructura del dataset

El dataset contiene información de 7,267 clientes con las siguientes características principales:

customerID: Identificador único del cliente.

Churn: Indica si el cliente abandonó el servicio (Yes) o permaneció (No).

Genero: Género del cliente.

SeniorCitizen: Indicador si el cliente es mayor de 60 años.

Partner, Dependents: Información sobre si el cliente tiene pareja o dependientes.

tenure: Meses que el cliente ha estado con la compañía.

Servicio_Internet: Tipo de servicio de internet contratado.

Contract: Tipo de contrato (mensual, anual, etc.).

PaymentMethod: Método de pago utilizado.

Cobro_Mensual, Cobro_Total: Facturación mensual y total.

Cuentas_Diarias: Nueva columna calculada para estimar facturación diaria.

Variables binarias creadas para análisis: Churn_Binario, Partner_Binario, Dependents_Binario, etc.

Uso

Activar el entorno virtual (opcional):

& ".venv/Scripts/Activate.ps1"


Ejecutar el script principal:

python challange2.py


El script imprimirá en consola:

Información del dataset.

Estadísticas descriptivas.

Distribución de la evasión de clientes.

Distribución de clientes por tipo de servicio.

Información sobre valores ausentes, duplicados e inconsistencias.

También generará gráficos para analizar la evasión según variables categóricas y numéricas.

Limpieza y transformación de datos

Se eliminaron duplicados.

Se corrigieron valores numéricos y se convirtieron columnas como Cobro_Total a tipo float.

Se rellenaron valores nulos en columnas categóricas con Desconocido.

Se eliminaron espacios en blanco y se normalizaron valores inconsistentes en columnas categóricas.

Se crearon columnas binarias para facilitar el análisis y posibles modelos predictivos.

Se calculó la facturación diaria (Cuentas_Diarias) a partir de la mensual.

Análisis realizado

Estadísticas descriptivas de variables numéricas: media, mediana, desviación estándar.

Distribución de clientes que permanecieron vs. clientes que abandonaron el servicio.

Exploración de la evasión según variables categóricas (género, tipo de contrato, método de pago, etc.).

Exploración de la evasión según variables numéricas (meses de contrato, cobro mensual, cuentas diarias).
