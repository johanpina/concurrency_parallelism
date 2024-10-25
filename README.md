## Clase de concurrencia

Para más información sobre la clase de concurrencia, visita el [repositorio](https://bioaiteamlearning.github.io/ProgCD_2024_01_G1_Ucaldas/intro.html)


### Ejecución de los programas
Recuerda la forma de crear el ambiente de python y de ejecutar los programas.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

``` 

### Ejecución de los programas

Para ejecutar los programas, recuerda que debes activar el ambiente de python.

```bash
source .venv/bin/activate
python3 <nombre_programa>.py
```

### Ejecución de backend con FastAPI

Para ejecutar el backend con FastAPI, recuerda que debes activar el ambiente de python.

```bash
source .venv/bin/activate
uvicorn file_name:app_object_name_inside_program --reload
```

e.g.

```bash
uvicorn main:app --reload
```

brew install rabbitmq
brew services start rabbitmq
rabbitmq-plugins enable rabbitmq_mqtt
pip install -r requirements.txt

rabbitmq-plugins enable rabbitmq_management

http://localhost:15672/