from flask import Flask, g

import db
from routes.addresses import addresses_bp
from routes.transactions import transactions_bp

app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(
    DATABASE='cttk.db',
))

DATABASE = "cttk.db"

URI_PREFIX = "/api/v1"


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


with app.app_context():
    db.init_db()
    app.register_blueprint(addresses_bp, url_prefix=URI_PREFIX + "/addresses")
    app.register_blueprint(transactions_bp, url_prefix=URI_PREFIX + "/transactions")

