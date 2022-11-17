from flask import Flask, jsonify, request

app = Flask(__name__)
#request : para interactuar con valores que vengan en las peticiones, ej: inputs,bodys
@app.post('/')
# devuelve un objeto json que es enviado por body
def root():
    request_data = request.get_json()
    return jsonify(request_data)

@app.get('/')
# ruta raiz del proyecto
def home():
    return jsonify({"response": "prueba scotiabank"})

if __name__ == '__main__':
    # para ser accedida de cualquier direcion 0.0.0.0, puerto establecido para la app, debug True para el momento de hacer cambios el servidor se reinicie solo
    app.run(host="0.0.0.0", port=4000, debug=True)