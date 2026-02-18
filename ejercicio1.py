import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
client = genai.Client(api_key=clave_api)

def explicar_inferencia_ia():
    print("🚀 Conectando con el motor de Gemini para explicar 'Inferencia en IA'...")

    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Explica qué es la inferencia en inteligencia artificial en menos de 50 palabras."
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")

if __name__ == "__main__":
    explicar_inferencia_ia()