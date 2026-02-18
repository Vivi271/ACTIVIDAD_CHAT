import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Inicializar el cliente de Gemini
client = genai.Client(api_key=API_KEY)

def procesar_articulo(texto, tarea):
    """
    Procesa un artículo según la tarea especificada.

    Args:
        texto (str): El texto largo que se desea procesar.
        tarea (str): La tarea a realizar, puede ser "resumir" o "profesionalizar".

    Returns:
        str: El texto procesado según la tarea.
    """
    # Validar entrada
    if not texto.strip():
        return "El texto no puede estar vacío."

    # Definir la system_instruction
    system_instruction = "Eres un Editor Editorial de prestigio."

    # Crear el prompt según la tarea
    if tarea == "resumir":
        prompt = f"Por favor, resume el siguiente texto:\n{texto}"
    elif tarea == "profesionalizar":
        prompt = f"Por favor, edita el siguiente texto para que suene formal y técnico:\n{texto}"
    else:
        return "Tarea no válida. Debe ser 'resumir' o 'profesionalizar'."

    # Configuración del modelo
    configuration = types.GenerateContentConfig(
        max_output_tokens=1000,  # Aumenta el límite de tokens
        system_instruction=system_instruction
    )

    try:
        # Realizar la petición a la API
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config=configuration,
            contents=prompt
        )
        return response.text.strip()  # Devolver el texto procesado
    except Exception as e:
        return f"❌ Error al procesar el artículo: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    texto = """
La inteligencia artificial (IA) está revolucionando múltiples industrias, desde la salud hasta la educación. En el ámbito de la salud, la IA se utiliza para analizar grandes cantidades de datos médicos, identificar patrones y ayudar en el diagnóstico de enfermedades. Por ejemplo, los algoritmos de aprendizaje automático pueden detectar anomalías en imágenes médicas, como radiografías y resonancias magnéticas, con una precisión comparable a la de los médicos especialistas. En la educación, la IA está transformando la forma en que los estudiantes aprenden, proporcionando herramientas personalizadas que se adaptan a las necesidades individuales de cada estudiante. Los sistemas de tutoría basados en IA pueden identificar áreas de dificultad y ofrecer explicaciones adicionales o ejercicios específicos para reforzar el aprendizaje. Además, la IA también está desempeñando un papel crucial en la automatización de tareas repetitivas, como la calificación de exámenes, lo que permite a los profesores dedicar más tiempo a la enseñanza. Sin embargo, a pesar de sus beneficios, la IA también plantea desafíos éticos y sociales, como la privacidad de los datos y el impacto en el empleo. A medida que la tecnología avanza, es fundamental encontrar un equilibrio entre aprovechar sus beneficios y mitigar sus riesgos.
"""
    tarea = "resumir"  # Cambiar a "profesionalizar" para probar
    print(f"Tarea seleccionada: {tarea}")
    resultado = procesar_articulo(texto, tarea)
    print("\nResultado:")
    print(resultado)