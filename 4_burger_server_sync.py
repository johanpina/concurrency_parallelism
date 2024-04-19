from fastapi import FastAPI
import time
import random

app = FastAPI()

def prepare_burger(num: int):
    wait_time = 4.0  # Tiempo fijo para hamburguesas
    print(f"Preparando {num} hamburguesa(s), esto tomará {wait_time:.2f} segundos.")
    time.sleep(wait_time)
    return f"{num} hamburguesa(s) preparada(s)"

def prepare_drink(type: str):
    wait_time = 1.0  # Tiempo fijo para bebidas
    print(f"Preparando {type}, esto tomará {wait_time:.2f} segundos.")
    time.sleep(wait_time)
    return f"{type} preparado"

@app.get("/order/burgers/{number_of_burgers}")
def order_burgers(number_of_burgers: int):
    burgers = prepare_burger(number_of_burgers)
    return {"message": f"Orden de hamburguesas completa: {burgers}"}

@app.get("/order/drinks/{type}")
def order_drinks(type: str):
    drink = prepare_drink(type)
    return {"message": f"Orden de bebidas completa: {drink}"}
