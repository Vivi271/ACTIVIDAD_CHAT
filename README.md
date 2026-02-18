# Proyecto Google GenAI Taller

Este proyecto tiene como objetivo implementar un conjunto de scripts en Python que utilizan la librería `google-genai` para realizar diversas tareas relacionadas con la inteligencia artificial, incluyendo consultas, procesamiento de textos y un sistema de chat interactivo.

## Estructura del Proyecto

```
google-genai-taller
├── src
│   ├── ejercicio1.py
│   ├── ejercicio2.py
│   ├── ejercicio3.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Ejecución de Scripts

### Ejercicio 1: Conexión y Petición Básica

Este script inicializa el cliente de Gemini y realiza una consulta simple para explicar qué es la "Inferencia en IA" en menos de 50 palabras. Para ejecutarlo, utiliza el siguiente comando:

```
python src/ejercicio1.py
```

### Ejercicio 2: Procesador de Textos Inteligente

Este script contiene la función `procesar_articulo(texto, tarea)` que permite resumir un texto o editarlo para que suene más formal y técnico. Para ejecutarlo, utiliza el siguiente comando:

```
python src/ejercicio2.py
```

### Ejercicio 3: Chat de Soporte con Historial

Este script implementa un sistema de chat para una tienda de tecnología, donde la IA actúa como un vendedor amable. Permite al usuario interactuar hasta que escriba "finalizar". Para ejecutarlo, utiliza el siguiente comando:

```
python src/ejercicio3.py
```

## Ejemplos de Uso

- **Ejercicio 1**: Al ejecutar el script, se espera recibir una breve explicación sobre la inferencia en IA.
- **Ejercicio 2**: Al proporcionar un texto y la tarea de "resumir", se obtendrá un resumen ejecutivo.
- **Ejercicio 3**: El usuario puede hacer preguntas sobre productos y recibir respuestas detalladas hasta que decida finalizar la conversación.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request con tus mejoras o correcciones.

## Licencia

Este proyecto está bajo la Licencia MIT.