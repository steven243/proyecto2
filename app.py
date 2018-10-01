import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Enlace a PUERTO si está definido, de lo contrario será 5000 por defecto.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
