from flask import Flask

app: Flask = Flask(__name__)


@app.route("/")
def hello_world():
    age: int = 19
    return "<h1>あなたの年齢は" + age + "歳です。</h1>"


if __name__ == "__main__":
    app.run(debug=True)
