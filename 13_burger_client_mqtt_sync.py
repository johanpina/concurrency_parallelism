import httpx
import time

def make_order(path: str):
    # Enviar una solicitud HTTP al servidor para realizar un pedido
    with httpx.Client() as client:
        response = client.get(f'http://localhost:8000{path}')
        print(response.json())

def main():
    t0 = time.time()
    # Realizar pedidos de varias bebidas
    orders = [
        "/order/drinks/coke",
        "/order/drinks/water",
        "/order/drinks/lemonade"
    ]
    for order in orders:
        make_order(order)
    print(f"Orders took {time.time()-t0:.2f} seconds")

if __name__ == '__main__':
    main()