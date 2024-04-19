from fastapi import FastAPI, BackgroundTasks
import asyncio
app = FastAPI()

async def prepare_burger(num: int):
    wait_time = 4.0  # Tiempo fijo para hamburguesas
    print(f"Preparando {num} hamburguesa(s), esto tomará {wait_time:.2f} segundos.")
    await asyncio.sleep(wait_time)
    print(f"{num} hamburguesa(s) preparada(s)")
    return f"{num} hamburguesa(s) preparada(s)"

async def prepare_drink(type: str):
    wait_time = 1.0  # Tiempo fijo para bebidas
    print(f"Preparando {type}, esto tomará {wait_time:.2f} segundos.")
    await asyncio.sleep(wait_time)
    print(f"{type} preparado")
    return f"{type} preparado"

async def background_prepare_burger(background_tasks: BackgroundTasks, num: int):
    background_tasks.add_task(prepare_burger, num)

async def background_prepare_drink(background_tasks: BackgroundTasks, type: str):
    background_tasks.add_task(prepare_drink, type)

@app.get("/order/burgers/{number_of_burgers}")
async def order_burgers(background_tasks: BackgroundTasks, number_of_burgers: int):
    await background_prepare_burger(background_tasks, number_of_burgers)
    return {"message": f"Tu pedido de {number_of_burgers} hamburguesa(s) está siendo preparado en segundo plano"}

@app.get("/order/drinks/{type}")
async def order_drinks(background_tasks: BackgroundTasks, type: str):
    await background_prepare_drink(background_tasks, type)
    return {"message": f"Tu pedido de bebida {type} está siendo preparado en segundo plano"}
