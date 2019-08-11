import logging
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods = ['POST'])
def webhook():
    logging.debug('received webhook')
    try:
        req = request.get_json()
        logging.debug(req)
        return make_response('', 204)
    except Exception as e:
        http_code = 500

    return make_response(jsonify(message='Webhook failed', error=e.message), http_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    logging.debug('waiting for webhook')
