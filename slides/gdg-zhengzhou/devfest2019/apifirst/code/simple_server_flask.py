
# from flask import Flask, jsonify

def index():
    return {
        'data': 'Hello World'
    }

def test_should_return_hello_world_when_access_index():
    assert 'Hello World' == index().get('data')


app = Flask(__name__)

@app.route("/")
def route_index():
    result = index()
    return jsonify(result)

if __name__ == "__main__":
    app.run()

