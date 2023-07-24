import threading
import schedule
import time
from services.incripcion_automatica_services import crear_nueva_inscripcion
from app import app, port
import uvicorn

# Función para ejecutar el servidor con uvicorn en un hilo separado
def run_server():
    uvicorn.run(app, port=int(port), host='localhost', reload=True)

# Utiliza threading para ejecutar la función en un hilo separado
creacion_inscripciones_thread = threading.Thread(target=crear_nueva_inscripcion)
creacion_inscripciones_thread.start()

# Programo la ejecución de la función cada día a la medianoche
schedule.every().day.at("00:00").do(crear_nueva_inscripcion)

# Ejecuto el servidor en un hilo separado
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Mantengo el programa en ejecución para que las tareas programadas se ejecuten
while True:
    schedule.run_pending()
    time.sleep(1)