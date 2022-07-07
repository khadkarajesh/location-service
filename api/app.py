from flask import Flask

from api.extensions import db
from api.models import Todo

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "testing", "host": "mongo"}


@app.route('/')
def todo():
    bulk = (Todo(title="Bulk 1"), Todo(title="Bulk 2"))
    Todo.objects().insert(bulk)
    return Todo.objects.to_json()


db.init_app(app)
