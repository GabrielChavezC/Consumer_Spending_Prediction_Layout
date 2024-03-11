# 💸Consumer Spending Prediction Layout💳

![](https://img.shields.io/badge/python-3.10+-sucess?style=for-the-badge&logo=python)![](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)![](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)![](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Objetivo 👈

La necesidad de **prever y optimizar** el gasto de sus usuarios ha llevado a una empresa de comercio electrónico a buscar soluciones innovadoras🧮

## Problemática 🚧

El porcentaje de compradores que **no realizaron una compra** es de más del 90% en comparación de aquellos que si realizaron una compra, gracias a un análisis previo de los datos pudimos conocer esta métrica,  como científicos de datos hemos sido convocados para desarrollar y dar solución a dicho problema asi mismo creando un modelo de machine learning que pueda predecir con precisión cuánto gastará un usuario al visitar dicho sitio web🌐

## Conociendo a los datos 🗺️

| Columna | Tipo de Dato | Descripción | 
| :---: | :---: | :--- | 
| `transactionRevenue` | Float | Gasto del cliente en esa interacción |

El dato estrella y el más relevante del proyecto es `transactionRevenue` en la cual trabajaremos para hacer la predicción🎇

![dispersion](https://i.imgur.com/obCvHUk.png)

Podemos observar que la mayoría de las personas no realizaron ninguna compra, fue tanta la cantidad que se genero un línea recta en 0. Tambien vemos valores que están por encima de esta línea, pero muy escasos, esto indica las pocas personas que realizaron compras. Haciendo un conteo encontramos con esto:

| transactionRevenue | Clientes | Porcentaje | 
| :---: | :---: | :---: | 
| Los que no compraron | 12119 | `98.66%` |
| Los que sí compraron | 164 | `1.34%` |

Lo preocupante es que la página no tiene una buena conversión de compra a las visitas que genera. Además lo confirma el histograma en realidad no es una actividad común que la gente compre en la tienda📉

![histograma](https://i.imgur.com/CVIJC00.png)


## Resultados y Conclusiones 📊

Para preparar el modelo haciendo las relaciones entre las variables que recolecta la tienda, lo primordial era clasificar quien compraría y quien no y a partir de ahí predecir con regresiones cuánto gastarían en la siguiente visita a la página👀

| Métrica | Para que sirve | 
| :---: | :--- |
| `R²` | Calidad del modelo para replicar los resultados |
| `MSE` | Diferencia **cuadrada** promedio entre los valores predichos por el modelo |
| `RMSE` | Diferencia promedio entre los valores predichos por el modelo |


![comparacion_modelos](https://i.imgur.com/YezxPet.png)

Como conclusión el modelo a utilizar por ser el mejor es uno de `LightGBM` con una relación a los datos reales del 50% y en producción del 79%, realiza una predicción de los precios que gastará el cliente está `±13,78` dólares de variación y realizando la producción está en `±9.51` dólares de variación💰

> [!NOTE]
> [![](https://img.shields.io/badge/acceso%20a%20la%20producción-Consumer__Spending__Prediction__Layout.ipynb-sucess?style=for-the-badge&logo=google-colab&color=ff8000)](https://drive.google.com/file/d/1tw9m_-HJm_5SabOrnxMEAAYZoWrFr4zH/view?usp=sharing)

https://github.com/luceldasilva/Consumer_Spending_Prediction_Layout/assets/81886133/7f517bc9-c8c3-4287-b058-b70c68982e91

> [!IMPORTANT]
> Esto fue un proyecto que participamos los miembros del canal del
> 
>[![](https://img.shields.io/youtube/channel/subscribers/UCuerQOTskuNkddcT738357g?style=for-the-badge&logo=youtube&label=ElProfeAlejo)](https://www.youtube.com/@ElProfeAlejo)
