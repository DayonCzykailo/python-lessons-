from fastapi import FastAPI
import json

# uvicorn fast_api.main:app --reload -> http://127.0.0.1:8000
app = FastAPI()

@app.get('/')
def read_root(restaurante: str = None):
    with open('restaurantes.txt', 'r') as file:
        if restaurante:
            jsonRestaurantes = json.loads(file.read())

            for r in jsonRestaurantes:
                if r['company'] == restaurante:
                    return r
                
            return {'message': 'Restaurante não encontrado'}
        return json.loads(file.read())