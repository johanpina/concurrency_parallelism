import threading
import queue
import time

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        time.sleep(3)  # Retraso de 4 segundos para procesar el elemento
        print(f'Finished {item}')
        q.task_done()

# Iniciar el hilo del trabajador.
threading.Thread(target=worker, daemon=True).start()

# Enviar treinta solicitudes de tareas al trabajador con un retardo de 1 segundo entre cada envío.
for item in range(20):
    q.put(item)
    print(f"put item {item} in queue!")
    time.sleep(1)  # Retraso de 1 segundo antes de enviar el próximo elemento

# Bloquear hasta que todas las tareas estén completadas.
q.join()
print('All work completed')
