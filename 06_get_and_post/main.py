from flask import Flask, request, jsonify

app = Flask(__name__)

DATA = [{
    'name': 'Vasya',
    'age': 43,
}]


@app.route("/", methods=["GET"])
def get_handler():
    return jsonify(DATA)


@app.route("/", methods=["POST"])
def post_handler():
    DATA.append(request.get_json())
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
