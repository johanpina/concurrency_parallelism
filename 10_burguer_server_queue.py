from fastapi import FastAPI
import threading
import queue
import time
import random

app = FastAPI()
task_drink_queue = queue.Queue()
task_burguer_queue = queue.Queue()

def burger_worker():
    while True:
        num = task_burguer_queue.get()
        print(f"Preparando {num} hamburguesa(s)...")
        time.sleep(4)  # Simula el tiempo de preparación
        print(f"{num} hamburguesa(s) preparada(s)")
        task_burguer_queue.task_done()

def drink_worker():
    while True:
        drink_type = task_drink_queue.get()
        print(f"Preparando bebida: {drink_type}...")
        time.sleep(1)  # Simula el tiempo de preparación
        print(f"Bebida {drink_type} preparada")
        task_drink_queue.task_done()

# Iniciar los hilos de trabajadores
threading.Thread(target=burger_worker, daemon=True).start()
threading.Thread(target=drink_worker, daemon=True).start()

@app.get("/order/burgers/{number_of_burgers}")
def order_burgers(number_of_burgers: int):
    task_burguer_queue.put(number_of_burgers)
    return {"message": f"Tu pedido de {number_of_burgers} hamburguesa(s) está siendo preparado"}

@app.get("/order/drinks/{type}")
def order_drinks(type: str):
    task_drink_queue.put(type)
    return {"message": f"Tu pedido de bebida {type} está siendo preparado"}
