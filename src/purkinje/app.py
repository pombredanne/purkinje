import logging
import sys
import httplib
from flask import Flask, render_template
from flask_sockets import Sockets
from assets import register_assets


app = Flask(__name__)
sockets = Sockets(app)


def configure_app(app_):
    """Configures application logging etc.
    """
    app_.logger.setLevel(logging.DEBUG)
    register_assets(app)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.formatter = logging.Formatter(
        fmt=u"%(asctime)s level=%(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )
    app_.logger.addHandler(handler)


def get_app():
    """Configures and provides application object
    """
    configure_app(app)
    return app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/trigger_error', methods=['GET'])
def trigger_error():
    raise Exception('Intentional error')


@app.errorhandler(httplib.NOT_FOUND)
def page_not_found(error):
    return render_template('404.html', error=error)


@sockets.route('/subscribe')
def subscribe(ws):
    while True:
        message = ws.receive()
        ws.send('Response to "%s"', message)