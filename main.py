from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>This is Index Page</h1>"


@app.route("/test/<int:id>")
def test(id):
    return f"<h1>输入的id{id}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)



