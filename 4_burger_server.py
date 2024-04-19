from fastapi import FastAPI
import asyncio

app = FastAPI()

async def prepare_burger(num: int):
    wait_time = 4.0  # Tiempo fijo para hamburguesas
    print(f"Preparando {num} hamburguesa(s), esto tomará {wait_time:.2f} segundos.")
    await asyncio.sleep(wait_time)
    return f"{num} hamburguesa(s) preparada(s)"

async def prepare_drink(type: str):
    wait_time = 1.0  # Tiempo fijo para bebidas
    print(f"Preparando {type}, esto tomará {wait_time:.2f} segundos.")
    await asyncio.sleep(wait_time)
    return f"{type} preparado"

@app.get("/order/burgers/{number_of_burgers}")
async def order_burgers(number_of_burgers: int):
    burgers = await prepare_burger(number_of_burgers)
    return {"message": f"Orden de hamburguesas completa: {burgers}"}

@app.get("/order/drinks/{type}")
async def order_drinks(type: str):
    drink = await prepare_drink(type)
    return {"message": f"Orden de bebidas completa: {drink}"}
