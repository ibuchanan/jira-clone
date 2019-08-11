from flask import Flask, request, make_response, jsonify
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def webhook():
    try:
        req = request.get_json()
        return make_response('', status.HTTP_204_NO_CONTENT)
    except Exception as e:
        http_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return make_response(jsonify(message='Webhook failed', error=e.message), http_code) 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
