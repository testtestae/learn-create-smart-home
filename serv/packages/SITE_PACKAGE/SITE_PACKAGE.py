from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "SITE_PACKAGE":
    app.run(host='127.0.0.1', port=5500)
