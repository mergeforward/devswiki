from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    html = "<h3>Hello {name}!</h3>" 
    return html.format(name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
