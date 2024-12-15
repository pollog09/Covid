# Proyecto de Análisis de Datos de COVID-19

![Icono del Proyecto](icon.webp)

## Descripción
Este proyecto tiene como objetivo analizar los datos de COVID-19 para proporcionar información y visualizaciones. El conjunto de datos incluye información sobre casos de COVID-19, recuperaciones y muertes en diferentes regiones. El análisis ayudará a comprender la propagación y el impacto del virus.

## Instalación

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/pollog09/Covid.git
```

### Paso 2: Crear un Entorno Virtual
Se recomienda crear un entorno virtual con Python 3.10:
```bash
python3.10 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### Paso 3: Instalar Requisitos
Asegúrate de tener Python instalado. Luego, instala los paquetes requeridos usando `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Paso 4: Descargar el Conjunto de Datos
Descarga el conjunto de datos usando el [ImagePreparation.ipynb](ImagePreparation.ipynb) y preparalos para el procesamiento siguiendo el python notebook.

## Uso
Ejecuta el script de para comprobar si se utiliza el gpu:
```bash
python check_gpu.py
```