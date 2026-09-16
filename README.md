Calculadora Automatizada con CI/CD

Integrantes del Equipo
Integrante 1: 250526 Nicolay Caballero Ibarra
Integrante 2: 250263 Brandon Alexis Nava Segura
Integrante 3: 250421 Ernesto Muñoz Mendez
Integrante 4: 250902 Carlos Armando Martinez Meza

Requisitos e Instalación
Para ejecutar este proyecto de forma local en su dispositivo, se necesita Python 3.10+

1. Clonar el repositorio:
   ```bash
   git clone [PEGAR_AQUÍ_EL_LINK_DE_SU_REPOSITORIO]
   cd [NOMBRE_DE_SU_CARPETA]
   ```
2. Instalar las dependencias (Pytest):
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la calculadora manualmente:
   ```bash
   python main.py
   ```
4. Ejecutar las pruebas locales:
   ```bash
   pytest test_main.py
   ```

Estructura de Automatización (CI/CD)
El flujo de trabajo automatizado está configurado en `.github/workflows/ci.yml` y realiza los siguientes pasos en la nube de GitHub de forma automática:
1. Crea un entorno virtual basado en **Ubuntu Linux
2. Descarga el código fuente del repositorio.
3. Configura el entorno con **Python 3.10
4. Instala las dependencias listadas en `requirements.txt`
5. Ejecuta el comando `pytest` para validar que todas las operaciones matemáticas funcionen correctamente
