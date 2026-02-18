import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

# Configuración del modelo y rol
system_instruction = """Eres un vendedor amable y experto en tecnología en una tienda de productos electrónicos. 
Tu objetivo es ayudar a los clientes respondiendo preguntas exclusivamente sobre productos y temas relacionados con tecnología. 
Si el cliente hace una pregunta que no está relacionada con tecnología, responde: 
'Lo siento, solo puedo responder preguntas relacionadas con tecnología.' 
Proporciona explicaciones completas y ejemplos cuando sea necesario.'"""

# Historial de ejemplos (Few-shot learning) con nuevos ejemplos
historial_ejemplos = [
    types.Content(
        role="user",
        parts=[types.Part(text="¿Qué características tiene una Smart TV 4K?")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="Una Smart TV 4K ofrece una resolución de 3840 x 2160 píxeles, lo que proporciona imágenes nítidas y detalladas. Además, incluye funciones inteligentes como acceso a aplicaciones de streaming (Netflix, YouTube), conectividad Wi-Fi y control por voz en algunos modelos.")]
    ),
    types.Content(
        role="user",
        parts=[types.Part(text="¿Qué diferencia hay entre un disco duro y un SSD?")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="Un disco duro (HDD) utiliza partes mecánicas para almacenar datos, mientras que un SSD (unidad de estado sólido) utiliza memoria flash, lo que lo hace mucho más rápido y resistente. Los SSD son ideales para mejorar el rendimiento de tu computadora.")]
    )
]

# Configuración de generación
configuration = types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.7,
    max_output_tokens=2000
)

# Inicialización del chat con historial
chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=configuration,
    history=historial_ejemplos,
)


print("--- Chat de Ventas (Escribe 'finalizar' para terminar) ---")
print("Vendedor: ¡Hola! ¿En qué puedo ayudarte hoy?\n")

while True:
    user_input = input("Cliente: ")

    if user_input.lower() == "finalizar":
        print("Vendedor: ¡Gracias por tu visita! Esperamos verte pronto.")
        break

    try:
        # Envío del mensaje
        response = chat.send_message(user_input)
        print(f"Vendedor: {response.text}\n")
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")