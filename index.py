from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="plantillas")

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["pet_shop"]
coleccion = db["productos"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/productos")
def productos():
    documentos = list(coleccion.find({"categoria": "Producto"}))

    for doc in documentos:
        doc["_id"] = str(doc["_id"])
    return render_template("productos.html", productos=documentos)

@app.route("/servicios")
def servicios():
    documentos = list(coleccion.find({"categoria": "Servicio"}))

    for doc in documentos:
        doc["_id"] = str(doc["_id"])
    return render_template("servicios.html", servicios=documentos)

if __name__ == "__main__":
    app.run(debug=True)
