import os
from dotenv import load_dotenv
import google.generativeai as genai

#cargar la clave API desde .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

#hacer una llamada a la API
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Cual es el clima en la ciudad de Tarija, Bolivia?")
print(response.text)