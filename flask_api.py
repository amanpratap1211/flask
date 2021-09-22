from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/user/<name>")
def index_new(name):
    return "<h1>Hello %s</h1>" % name


@app.route("/headers")
def headers():
    user_agent = request.headers.get('User-Agent')
    return "<h1>Your Browser is %s</h1>" % user_agent


a = [{'name': "Aman", "income": 50000}]


@app.route("/income", methods=["POST"])
def post():
    a.append(request.get_json())
    return "created", 204


@app.route("/income")
def get():
    return make_response(jsonify(a), 200)


stock = {
    'name': 'Aman',
    'income': 50000
}


@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        stock[collection] = req[collection]
        res = make_response(jsonify({"msg": "collection updated.."}), 200)
        return res
    # either create or we need send error saying record not found for updation
    stock[collection] = req
    res = make_response(jsonify({"msg": "collection created..."}), 201)
    return res


@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    req = request.get_json()
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"msg": "collection deleted.."}), 200)
        return res
    # either create or we need send error saying record not found for updation
    res = make_response(jsonify({"error": "collection not found..."}), 404)
    return res


if __name__ == '__main__':
    app.run(debug=True)