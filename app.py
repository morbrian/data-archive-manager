import os
from flask import Flask
from apis import api

app = Flask(__name__)
api.init_app(app)

if __name__ == "__main__":
    # if you are running from the commandline using "flask run"
    # then this is NOT used
    # instad you can do: flask run -h localhost -p 5001
    app.run(host=os.getenv('DARCHMAN_IP', '0.0.0.0'), 
            port=int(os.getenv('DARCHMAN_PORT', 5000)),
            debug=False)