# IA07 - Proyecto - Neural Covid-19

## Universidad Creativa  
**Certificación Profesional en Inteligencia Artificial**  

**IA07 - Fundamentos de Deep Learning y Aprendizaje Automático**  

**Proyecto Final:**  
**Neural Covid-19**

**Fecha de asignación:** 03 Diciembre, 2024  
**Fecha de entrega:** 19 Diciembre, 2024  
**Grupos:** Parejas  
**Profesor:** Angelo Ortiz Vega  

---

## 1. Objetivo  
El objetivo principal de este proyecto es aplicar redes neuronales convolucionales (CNN) para la clasificación multiclase de imágenes utilizando aprendizaje supervisado. Se pretende explorar el uso de filtros en imágenes como parte del preprocesamiento de datos, así como técnicas de aumento de datos y herramientas de monitoreo del proceso de entrenamiento.

---

## 2. Motivación  
Este proyecto permite aplicar redes neuronales convolucionales (CNN) en la clasificación de imágenes, utilizando el **dataset Covid-19 Image Dataset**. Este conjunto de datos contiene imágenes de rayos X clasificadas en tres categorías: **Covid-19**, **Neumonía**, y **Normal**.  
Los objetivos incluyen:  
- Construir modelos con alta precisión.  
- Experimentar con técnicas de preprocesamiento de imágenes.  
- Usar herramientas avanzadas como **PyTorch** y **Weights and Biases** para monitoreo del entrenamiento.  

---

## 3. Herramientas recomendadas  
- **PyTorch:** Framework para el desarrollo de redes neuronales.  
- **Weights and Biases:** Monitoreo y visualización de métricas de entrenamiento.  
- **Google Colab:** Plataforma para ejecutar el proyecto en caso de no contar con GPU local.  
- **OpenCV:** Para aplicar filtros de imagen y transformaciones.

---

## 4. Pasos a seguir  

### 4.1 Selección del modelo  
Seleccionar dos modelos de convolución preexistentes (ej., **ResNet**, **AlexNet**, **VGG16**). Realizar **fine-tuning** para adaptarlos al problema y justificar la elección.

### 4.2 Preprocesamiento de imágenes  
Entrenar los modelos con tres conjuntos de datos:  
1. **Conjunto 1:** Imágenes sin procesar (crudas).  
2. **Conjunto 2:** Imágenes con filtro bilateral para suavizar y reducir ruido.  
3. **Conjunto 3:** Imágenes con filtro Canny Edge para detectar bordes.  

### 4.3 Data Augmentation  
Aplicar transformaciones aleatorias como rotación o cambio de colores para aumentar la cantidad de ejemplos disponibles y prevenir el sobreajuste.

### 4.4 Entrenamiento del modelo  
- Entrenar desde cero o usar **fine-tuning** para adaptar los modelos preentrenados.  
- Probar ambos modelos con los tres conjuntos de datos.  
- Presentar métricas y matriz de confusión.

### 4.5 Evaluación del modelo  
Visualizar métricas en tiempo real con **Weights and Biases** y justificar la elección del mejor modelo.

### 4.6 Silency Maps  
Aplicar **Silency Maps** para visualizar las áreas importantes de las imágenes utilizadas por el modelo para la clasificación. Comparar activaciones antes y después de aplicar los filtros.

### 4.7 Interfaz  
Diseñar una UI para:  
- Cargar imágenes nuevas o seleccionar imágenes del dataset.  
- Mostrar imágenes procesadas con predicción de clases y métricas de evaluación.  

---

## 5. Entregables  
- **Jupyter notebook** con la exploración de datos, visualizaciones, resultados de modelos y evaluación de métricas.  
- Código de la interfaz.  
- Presentación en formato PowerPoint, PDF o enlace.

---

## 6. Presentación  
### Estructura:  
1. **Portada:** Nombre del proyecto, autor, tutor, institución.  
2. **Planteamiento del problema:** Descripción clara del problema.  
3. **Descripción de la solución:** Análisis, herramientas utilizadas, resultados comparativos.  
4. **Conclusiones:** Evaluación objetiva del proyecto.  
5. **Recomendaciones:** Trabajo futuro relacionado.

**Duración máxima:** 20 minutos.  
**Formato de entrega:** Classroom.

---

## 7. Rúbrica de evaluación  

| **Criterios**                        | **Puntuación máxima** |
|--------------------------------------|------------------------|
| Preprocesamiento aplicando filtros   | 10                     |
| Data Augmentation                    | 10                     |
| Entrenamiento con datasets           | 20                     |
| Presentación de métricas y matriz    | 15                     |
| Comparación de resultados            | 15                     |
| Interfaz                             | 20                     |
| Presentación                         | 10                     |

---

## 8. Anexos  
Para cualquier duda, contactar al profesor por correo electrónico o Telegram.  

---
