from flask import Flask
from routes.sync import sync_bp
from routes.status import status_bp

app = Flask(__name__)

# Registrar Blueprints (rotas)
app.register_blueprint(sync_bp)
app.register_blueprint(status_bp)

if __name__ == '__main__':
    app.run(debug=True)
