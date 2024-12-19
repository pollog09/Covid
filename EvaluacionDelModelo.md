
### Training resnet on bilateral dataset

![Imagen 4](res/resnetbilateral.png)

### Training resnet on raw dataset

![Imagen 5](res/resnetraw.png)

## Training resnet on canny dataset
e
![Imagen 6](res/resnetcanny.png)

### Training vgg on bilateral dataset

![Imagen 7](res/vggbilateral.png)

### Training vgg on raw dataset

![Imagen 8](res/vggraw.png)

### Training vgg on canny dataset

![Imagen 9](res/vggcanny.png)

## Justificación de la Elección del Modelo VGG con el Filtro de Canny

La elección del modelo adecuado para resolver un problema de clasificación depende de métricas específicas, como precisión, recall, F1-Score y análisis de la matriz de confusión. En este caso, el modelo VGG con el filtro de Canny ha demostrado un desempeño superior en comparación con otros modelos evaluados.

Al aplicar el filtro de Canny a los datos de entrada y utilizar la arquitectura VGG, se observaron las siguientes mejoras significativas:

Mayor Precisión General: El modelo logra una precisión elevada, lo que indica que predice correctamente la mayoría de las clases. Esto se evidencia en la diagonal principal de la matriz de confusión, donde se encuentran la mayoría de los aciertos.

Reducción de Falsos Negativos: La combinación de VGG con el filtro de Canny disminuyó considerablemente los falsos negativos, como se aprecia en la matriz de confusión. Esto es crucial en problemas donde es más costoso no detectar una clase importante.

Mejor F1-Score: El F1-Score balanceado muestra que el modelo mantiene un equilibrio entre la precisión (precision) y el recall. Esto es especialmente valioso para evitar un sesgo hacia clases mayoritarias.

El filtro de Canny actúa como una etapa de preprocesamiento que resalta los bordes en las imágenes. Esto aporta los siguientes beneficios:

Reducción de Ruido: Al resaltar las características relevantes (bordes), se reduce la información innecesaria, facilitando la tarea del modelo para identificar patrones importantes.
Mejor Representación de los Datos: El filtro proporciona imágenes más simples y enfocadas en las características clave, lo que mejora el desempeño del modelo VGG.

La arquitectura VGG es conocida por su capacidad de capturar características profundas en imágenes debido a su uso de múltiples capas convolucionales.

## TL;TR
La combinación del modelo VGG con el filtro de Canny ofrece un equilibrio óptimo entre precisión, recall y generalización. Su capacidad para reducir el ruido en las imágenes y extraer características clave permite obtener predicciones más precisas, convirtiéndolo en la mejor opción para el problema evaluado.