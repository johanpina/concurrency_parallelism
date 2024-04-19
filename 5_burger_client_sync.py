import httpx
import time

def make_order(path: str):
    with httpx.Client() as client:
        response = client.get(f'http://127.0.0.1:8000{path}')
        print(response.json())

def main():
    t0 = time.time()
    orders = [
        "/order/burgers/2",
        "/order/drinks/coke",
        "/order/burgers/3",
        "/order/drinks/water",
        "/order/burgers/1",
        "/order/drinks/lemonade"
    ]
    for order in orders:
        make_order(order)
    print(f"Orders took {time.time()-t0:.2f} seconds")
    
if __name__ == '__main__':
    main()
