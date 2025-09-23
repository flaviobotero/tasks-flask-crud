from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre"

# algo apenas para o desenvolvimento local - executado o arquivo de forma manual
if __name__ == "__main__":
    app.run(debug=True)

