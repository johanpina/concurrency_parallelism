from fastapi import FastAPI
import threading
import time
import paho.mqtt.client as mqtt

app = FastAPI()

# Configurar el cliente MQTT para RabbitMQ (conectado en localhost)
mqtt_client = mqtt.Client()

# Trabajador que procesa las bebidas al recibir mensajes de MQTT
def drink_worker():
    def on_message(client, userdata, message):
        # Procesar el mensaje recibido desde MQTT (tipo de bebida)
        drink_type = message.payload.decode('utf-8')
        print(f"Preparando bebida: {drink_type}...")
        time.sleep(2)  # Simula el tiempo de preparación
        print(f"Bebida {drink_type} preparada")

    mqtt_client.on_message = on_message
    mqtt_client.connect("localhost", 1883, 60)  # Conectar a RabbitMQ en el puerto MQTT 1883
    mqtt_client.subscribe("drink_orders")  # Suscribirse al tópico 'drink_orders'
    mqtt_client.loop_forever()  # Mantener la conexión MQTT abierta

# Iniciar el trabajador de bebidas en un hilo para que escuche mensajes MQTT
threading.Thread(target=drink_worker, daemon=True).start()

@app.get("/order/drinks/{drink_type}")
def order_drinks(drink_type: str):
    # Publicar el pedido de bebida en el tópico 'drink_orders'
    mqtt_client.publish("drink_orders", drink_type)
    return {"message": f"Tu pedido de bebida {drink_type} está siendo preparado"}