# EduBotPy – Chatbot educativo sin conexión

**EduBotPy** es un chatbot desarrollado en Python puro que responde preguntas básicas sobre tecnología y educación digital. Está diseñado especialmente para comunidades con acceso limitado a internet, permitiendo el aprendizaje de conceptos fundamentales de informática, redes, seguridad digital y programación desde un entorno local y accesible.

## Objetivo

Facilitar el acceso a información básica sobre tecnología en comunidades rurales y de bajos recursos en Colombia, mediante una herramienta educativa local, sin conexión a internet, fácil de usar y ejecutar desde cualquier equipo con Python instalado.

---

## Características

- Chatbot educativo funcional sin conexión a internet.
- Interfaz local basada en navegador (HTML + Flask).
- Base de datos de preguntas y respuestas ampliable.
- Imágenes explicativas integradas para reforzar el aprendizaje.
- Registro local de conversaciones.

---

## Tecnologías utilizadas

- Python 3.x
- Flask
- JSON (para preguntas y respuestas)
- HTML/CSS
- Ejecutable desde terminal o navegador local

---

## Instalación y ejecución

### 1. Clonar el repositorio

git clone https://github.com/carlosdiamon/RDC

### 2. Crear entorno virtual
python -m venv env
source env/bin/activate  # En Linux/Mac
env\Scripts\activate     # En Windows

### 3. Instalación y ejecución
pip install -r requirements.txt

### 4. Ejecutar y levantar Docker
(Previamente tener instalado Docker[https://www.docker.com/])
docker compose up --build