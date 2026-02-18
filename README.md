# Proyecto Google GenAI Taller

Este proyecto tiene como objetivo implementar un conjunto de scripts en Python que utilizan la librería `google-genai` para realizar diversas tareas relacionadas con la inteligencia artificial, incluyendo consultas, procesamiento de textos y un sistema de chat interactivo.

---

## 📋 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

1. **Python 3.9 o superior** instalado en tu sistema.
2. **API Key de Google Gemini** (puedes obtenerla en Google AI Studio).
3. **Librerías necesarias instaladas** (ver sección de instalación).

---

## ⚙️ Instalación

Sigue estos pasos para configurar el entorno y preparar el proyecto:

1. **Clona el repositorio**:
   ```bashs
   git clone https://github.com/Vivi271/ACTIVIDAD_CHAT.git
   cd ACTIVIDAD_CHAT
   ```

2. **Crea un entorno virtual** (opcional, pero recomendado):
   ```bash
   python3 -m venv env
   source env/bin/activate  # En Linux/Mac
   env\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu API Key**:
   - Crea un archivo llamado `.env` en la raíz del proyecto.
   - Dentro del archivo `.env`, agrega tu clave de API:
     ```
     GEMINI_API_KEY=tu_clave_api_aqui
     ```

---

## 🚀 Ejecución de Scripts

### **Ejercicio 1: Conexión y Petición Básica**
- **Descripción**: Este script inicializa el cliente de Gemini y realiza una consulta simple para explicar qué es la "Inferencia en IA" en menos de 50 palabras.
- **Ejecución**:
   ```bash
   python src/ejercicio1.py
   ```

---

### **Ejercicio 2: Procesador de Textos Inteligente**
- **Descripción**: Este script contiene la función `procesar_articulo(texto, tarea)` que permite:
  - Resumir un texto.
  - Editar un texto para que suene más formal y técnico.
- **Ejecución**:
   ```bash
   python src/ejercicio2.py
   ```

---

### **Ejercicio 3: Chat de Soporte con Historial**
- **Descripción**: Este script implementa un sistema de chat para una tienda de tecnología, donde la IA actúa como un vendedor amable. Permite al usuario interactuar hasta que escriba "finalizar".
- **Ejecución**:
   ```bash
   python src/ejercicio3.py
   ```

---

## 🛠️ Solución de Problemas Comunes

- **Error de API Key**: Asegúrate de que el archivo `.env` esté bien escrito y que la variable se llame `GEMINI_API_KEY`.
- **ModuleNotFoundError**: Verifica que activaste el entorno virtual y ejecutaste `pip install -r requirements.txt`.
- **Error al procesar la solicitud**: Revisa tu conexión a internet y asegúrate de que tu API Key sea válida.

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.

---

## 📷 Capturas de Pantalla

### Ejercicio 1: Conexión y Petición Básica
<img width="1792" height="1120" alt="Actividad1" src="https://github.com/user-attachments/assets/8f131c10-e71a-4ee5-add4-0c48cd739e0c" />


### Ejercicio 2: Procesador de Textos Inteligente
<img width="1792" height="1116" alt="Actividad2" src="https://github.com/user-attachments/assets/cfb98b9b-5f26-46ca-8556-0c19f3940cd1" />


### Ejercicio 3: Chat de Soporte con Historial
<img width="1790" height="1120" alt="Actividad3" src="https://github.com/user-attachments/assets/57c4ea11-286e-4745-83d2-2c5455a0ef6b" />
