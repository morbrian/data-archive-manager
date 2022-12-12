import os
from flask import Flask
from apis import api
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_for=1, x_port=1, x_prefix=1)

# TODO: this next line didn't throw errors, but curren_app never had the loaded config, tried json and yaml
# app.config.from_file('./darchman.json', load=json.load)
api.init_app(app)

if __name__ == "__main__":
    # if you are running from the commandline using "flask run"
    # then this is NOT used
    # instad you can do: flask run -h localhost -p 5001
    app.run(host=os.getenv('DARCHMAN_IP', '0.0.0.0'), 
            port=int(os.getenv('DARCHMAN_PORT', 5000)),
            debug=False)