from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return send_file('index.html')

if __name__ == "__main__":
    @app.route('/<path:filename>')
    def serve_static(filename):
        print(filename)
        return send_file(filename)

    app.run(debug=True, port=4000)

__author__ = 'Lena'
