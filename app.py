from flask import Flask

from routes.addresses import addresses_bp
from routes.transactions import transactions_bp

app = Flask(__name__)

URI_PREFIX = "/api/v1"


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(addresses_bp, url_prefix=URI_PREFIX + "/addresses")
app.register_blueprint(transactions_bp, url_prefix=URI_PREFIX + "/transactions")

if __name__ == '__main__':
    app.run(debug=True)
