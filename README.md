# Stori Software Engineer Technical Challenge

Este proyecto implementa una solución para el desafío técnico de Stori. Procesa un archivo CSV con transacciones, calcula un resumen y envía los resultados por correo electrónico

## Instrucciones de uso

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/AguilaMike/Stori_Challenge_Python.git
    cd Stori_Challenge_Python
    ```

2.  **Crear un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv venv
    venv/Scripts/activate ** Solo windows
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar:**
    *   Crea un archivo `data/transactions.csv` con tus datos de transacciones.
    *   Actualiza la configuración en `config.py` y `docker-compose.yml` con tus credenciales de correo electrónico y base de datos (si aplica).

5.  **Ejecutar con Docker Compose:**

    ```bash
    docker-compose up --build
    ```

## Estructura del proyecto

*   `src/`: Contiene el código fuente de la aplicación.
*   `templates/`: Directorio para almacenar templates (por ejemplo, `email_template.html`).
*   `config.py`: Configuración de la aplicación.
*   `docker-compose.yml`: Configuración para ejecutar la aplicación con Docker Compose.
*   `Dockerfile`: Configuración para construir la imagen de Docker.
*   `requirements.txt`: Dependencias de Python.
*   `README.md`: Este archivo con instrucciones.
*   `data/`: Directorio para almacenar archivos de datos (por ejemplo, `transactions.csv`).